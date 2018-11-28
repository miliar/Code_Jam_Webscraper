#include <iostream>
#include <vector>
#include <stack>
using namespace std;
#define MAXN 500
#define LOCAL

char C[MAXN][MAXN], D[MAXN][MAXN];
int element_exist[MAXN];

int index(char src_char)
{
	if(src_char <= 'z' && src_char >= 'a') return src_char - 'a';

	if(src_char <= 'Z' && src_char >= 'A') return 26 + src_char - 'A';

	return -1;
}

bool IsOpposed(stack<char>& s, char t)
{
	int p1 = index(t);
	for(int i = 0; i < 100; i++)
	{
		if(D[p1][i] && element_exist[i]) return true;
	}
	return false;
}

void TestCombine(stack<char>& s, char t)
{
	while(true)
	{
		if(s.empty()) break;
		int  p1 = index(s.top());
		int  p2 = index(t);
		if(C[p1][p2]) 
		{
			s.pop();
			element_exist[p1]--;
			t = C[p1][p2];
		}
		else
		{
			break;
		}
	}
	
	if(IsOpposed(s, t))
	{
		while(!s.empty()) s.pop();
		memset(element_exist, 0, sizeof(element_exist));
	}
	else
	{
		s.push(t);
		element_exist[index(t)]++;
	}
	return;
}


void recur_print(stack<char>& s)
{
	if(!s.empty())
	{
		char t  = s.top();
		s.pop();
		if(!s.empty()) recur_print(s);
		else{
			printf("%c", t);
			return;
		}
		printf(", %c", t);
	}
}
int main()
{
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif

	int iCaseTimes;

	scanf("%d", &iCaseTimes);
	int num_c, num_d;
	for(int k = 1; k <= iCaseTimes; k++)
	{
		memset(C, 0, sizeof(C));
		memset(D, 0, sizeof(D));
		memset(element_exist, 0, sizeof(element_exist));

		scanf("%d", &num_c);
		if(num_c > 0)
		{
			while(num_c--) 
			{
				char c_seq[20];
				scanf("%s", c_seq);
				int p1 = index(c_seq[0]), p2 = index(c_seq[1]);
				C[p1][p2] = c_seq[2], C[p2][p1] = c_seq[2];
			}
		}

		scanf("%d", &num_d);
		if(num_d > 0)
		{
			while(num_d--)
			{
				char d_seq[20];
				scanf("%s", d_seq);
				int p1 = index(d_seq[0]), p2 = index(d_seq[1]);
				D[p1][p2] = 1, D[p2][p1] = 1;
			}
		}

		char invoke_list[MAXN];
		stack<char> ret;
		while(!ret.empty()) ret.pop();
		int invoke_len;
		scanf("%d%s", &invoke_len, invoke_list);
		for(int i = 0; i < invoke_len; i++)
		{
			TestCombine(ret, invoke_list[i]);
		}

		printf("Case #%d: [", k);

		if(!ret.empty()) 
		{
			recur_print(ret);
		}
		printf("]\n");

	}

	return 0;
}