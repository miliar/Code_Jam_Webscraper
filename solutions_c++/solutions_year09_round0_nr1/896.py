#include <cstdio>
#include <algorithm>
using namespace std;

const int maxd = 5000;
const int maxl = 15;

int L, D, N;
int words[maxd][maxl];
bool pattern[maxl][26];

void init()
{
	char st[100];
	for (int i = 0; i < D; i++) {
		scanf("%s\n", st);
		for (int j = 0; j < L; j++)
			words[i][j] = st[j] - 'a';
	}
}

int work() 
{
	char st[28 * maxl + 10];
	scanf("%s\n", st);
	for (int i = 0; i < L; i++)
		for (int j = 0; j < 26; j++)
			pattern[i][j] = false;
	int pos = 0;
	bool inside = false;
	for (int i = 0; st[i]; i++) 
	{
		if (st[i] == '(') inside = true;
		else if (st[i] == ')') 
		{
			inside = false;
			pos++;
		}
		else
		{
			pattern[pos][st[i] - 'a'] = true;	
			if (!inside) pos++;
		}
		
	}
	int count = 0;
	for (int i = 0; i < D; i++)
	{
		bool ok = true;
		for (int j = 0; j < L; j++)
			if (!pattern[j][words[i][j]])
			{
				ok = false;
				break;
			}
		if (ok) count++;
	}
	return count;
}

int main()
{
	scanf("%d %d %d\n", &L, &D, &N);
	init();
	for (int i = 0; i < N; i++)
	{
		printf("Case #%d: %d\n", i+1, work());	
	}
}
