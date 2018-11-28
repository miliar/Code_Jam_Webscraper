#include <iostream>
using namespace std;

char word[5000][16];
char pattern[1000];
int flag[15];

int main()
{
	int L, D, N;
	int i, j, k;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d %d %d", &L, &D, &N);
	for (i = 0; i < D; ++i) scanf("%s", word[i]);
	for (k = 1; k <= N; ++k)
	{
		scanf("%s", pattern);
		memset(flag, 0, sizeof(flag));
		j = 0;
		for (i = 0; pattern[i]; ++i, ++j)
		{
			if (pattern[i] == '(')
			{
				for (++i; pattern[i] != ')'; ++i)
					flag[j] |= 1 << (pattern[i] - 'a');
			}
			else
			{
				flag[j] |= 1 << (pattern[i] - 'a');
			}
		}
		int cnt = 0;
		for (i = 0; i < D; ++i)
		{
			for (j = 0; j < L; ++j)
				if (!(flag[j] & (1 << (word[i][j] - 'a')))) break;
			if (j == L) cnt++;
		}
		printf("Case #%d: %d\n", k, cnt);
	}	
	return 0;
}
