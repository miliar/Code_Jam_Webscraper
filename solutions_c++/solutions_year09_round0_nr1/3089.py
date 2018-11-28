#include<iostream>
#include<string>

using namespace std;

char str[5001][16],pat[500];

int L,D,N;

bool check(char* str, char* pat)
{
	int len_pat = strlen(pat),now = 0;
	for (int i = 0; i < L; i++)
	{
		//cout << now << endl;
		if (pat[now] == '(')
		{
			now++;
			while(pat[now] != str[i] && pat[now] != ')' && now < len_pat) now++;
			if (now == len_pat || pat[now] == ')') return false;
			while(pat[now] != ')' && now < len_pat) now ++;
			if (now == len_pat) return false; 
			else
			{
				now++;
				continue;
			}
		}
		else
		{
			if (pat[now] != str[i]) return false;
			else
			{
				now++;
				continue;
			}
		}
	}
	return true;
}
		
int main()
{
	FILE* a = fopen("A-large.out","w");
	freopen("A-large.in","r",stdin);
	scanf("%d %d %d",&L,&D,&N);
	for (int i = 0; i < D; i++)
		scanf("%s",str[i]);
	int t = 0,ans = 0;
	while(t++ < N)
	{
		scanf("%s",pat);
		ans = 0;
		for (int i = 0; i < D; i++)
		{
			if (check(str[i],pat))
			{ 
				ans++;
				continue;
			}
		}
		fprintf(a,"Case #%d: %d\n",t,ans);
	}
	fclose(a);
	return 0;
}
