#include<stdio.h>
#include<math.h>
	char table[200][200];
	int R, C;

bool proc()
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			if(table[i][j] == '#')
			{
				if( table[i][j+1] =='#' && table[i+1][j] == '#' && table[i+1][j+1] == '#' )
				{
					table[i][j] = '/';
					table[i][j+1] = '\\';
					table[i+1][j] = '\\';
					table[i+1][j+1] = '/';
				}
				else return false;
			}
		}
	}
	return true;
}


void solve()
{
	scanf("%d %d", &R, &C);
	for(int i = 0; i < R; i++)
	{
		scanf("%s", &table[i]);
	}

	if( proc() )
	{
		for(int i = 0; i < R; i++)
			printf("%s\n", table[i]);
	}
	else 
		printf("Impossible\n");


}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d\n", &T);
	for(int i = 1; i <= T; i++)
	{
		printf("Case #%d:\n", i);
		solve();
	}

	return 0;

}
