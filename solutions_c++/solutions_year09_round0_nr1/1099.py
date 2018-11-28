#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int L, D, N;
char dic[5000][20];

int main()
{
	int i, j, k;
	scanf("%d %d %d", &L, &D, &N);
	for( i = 0; i < D; ++i)
		scanf("%s", dic[i]);

	for( i = 1; i <= N; ++i)
	{
		char pt[2000];
		scanf("%s", pt);
		int m = strlen(pt);

		set<char> chk[15];
		j = k = 0;
		while(j < m)
		{
			if( pt[j] == '(' )
			{
				while(pt[++j] != ')')
				{
					chk[k].insert(pt[j]);
				}
				j++;
				k++;
			}
			else
			{
				chk[k++].insert(pt[j++]);
			}
		}

		int sol = 0;
		for( j = 0; j < D; ++j )
		{
			for( k = 0; k < L; ++k)
				if( chk[k].count(dic[j][k]) == 0 )
					break;

			if( k == L )
				sol++;
		}
		
		printf("Case #%d: %d\n", i, sol);
	}
	return 0;
}
