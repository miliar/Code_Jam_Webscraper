#include <cstdio>

int T, C, D, N;
int st[105], pz, viz[30];

int c[30][30], d[30][30];

void resetMat()
{
	for (int i = 0 ; i < 30; i++)
	{
		for (int j = 0; j < 30; j++) c[i][j] = d[i][j] = -1;
		viz[i] = 0;
	}
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int i, j, k;
	
	scanf("%d\n", &T);
	
	for (k = 1; k <= T; k++)
	{
		resetMat();
		scanf("%d ", &C);
		char s[101];
		for (i = 1; i <= C; i++)
		{
			scanf("%s ", s);
			c[s[0] - 'A'][s[1] - 'A'] = c[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		scanf("%d ", &D);
		for (i = 1; i <= D; i++)
		{
			scanf("%s ", s);
			d[s[0] - 'A'][s[1] - 'A'] = d[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		
		scanf("%d ", &N);
		scanf("%s", s);
		
		pz = 0;
		for (i = 0; i < N; i++)
		{
			if (pz == 0)
			{
				pz++;
				st[pz] = s[i] - 'A';
				viz[s[i] - 'A']++;
			}
			else
			{
				if (c[s[i] - 'A'][st[pz]] != -1)
				{
					viz[st[pz]]--;
					st[pz] = c[s[i] - 'A'][st[pz]];
					viz[st[pz]]++;
					while (pz > 1 && c[st[pz]][st[pz - 1]] != -1)
					{
						viz[st[pz]]--;
						st[pz - 1] = c[st[pz]][st[pz - 1]];
						pz--;
						viz[st[pz]]++;
					}
				}
				else
				{
					pz++;
					st[pz] = s[i] - 'A';
					viz[s[i] - 'A']++;
				}
				
				for (j = 0; j < 30; j++)
					if (viz[j] && d[st[pz]][j] != -1)
					{
						while (pz > 0)
						{
							viz[st[pz]]--;
							pz--;
						}
						break;
					}
			}
		}
		
		printf("Case #%d: [", k);
		for (i = 1; i <= pz - 1; i++)
		{
			printf("%c, ", st[i] + 'A');
		}
		if (pz > 0) printf("%c", st[pz] + 'A');
		printf("]\n");
	}
	return 0;
}
