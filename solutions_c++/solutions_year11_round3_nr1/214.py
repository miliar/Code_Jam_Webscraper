#include<cstdio>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"
#define NMAX 51

void solve()
{
	int n, m;
	char S[NMAX][NMAX], ok = 1;

	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++i)
		scanf("%s", S[i]);
	for(int j = 0; j < m; ++j)
		S[n][j] = 0;

	for(int i = 0; i < n && ok; ++i)
		for(int j = 0; j < m; ++j)
		{
			if(S[i][j] != '#')
				continue;
			if(S[i][j + 1] != '#' || S[i + 1][j] != '#' || S[i + 1][j + 1] != '#')
			{
				ok = 0;
				break;
			}
			S[i][j] = '/';
			S[i][j + 1] = '\\';
			S[i + 1][j] = '\\';
			S[i + 1][j + 1] = '/';
		}
	if(!ok)
	{
		printf("Impossible\n");
		return;
	}

	for(int i = 0; i < n; ++i)
		printf("%s\n", S[i]);
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d:\n", t);
		solve();
	}

	return 0;
}
