#include <cstdio>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)

char s[5010][20];

int main()
{
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	FOR(i,0,D)
		scanf("%s", s[i]);

	FOR(i,0,N)
	{
		char ts[20*30];
		scanf("%s", ts);
		vector< vector<bool> > used(L, vector<bool>(30));
		for (int k=0, j=0; ts[j]; ++j)
			if (ts[j] == '(')
			{
				for (++j; ts[j] != ')'; ++j)
					used[k][ts[j]-'a'] = true;
				++k;
			}
			else
			{
				used[k++][ts[j]-'a'] = true;
			}
		int res = 0;
		
		FOR(j,0,D)
		{
			//fprintf(stderr, "%s\n", s[j]);
			bool ok=1;
			FOR(t,0,L)
				ok &= used[t][s[j][t]-'a'];
			res += ok;
		}

		fprintf(stderr, "Case #%d: %d\n", i+1, res);
		printf("Case #%d: %d\n", i+1, res);
	}

	return 0;
}
