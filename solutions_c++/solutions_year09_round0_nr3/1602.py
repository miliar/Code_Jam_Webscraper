//C.cpp
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
const char pt[21] = " welcome to code jam";
int T , l;
char s[502];
int d[502][20];
int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	int cas = 0;
	for ( scanf("%d\n" , &T) ; T-- ; )
	{
		gets(s + 1);
		l = strlen(s + 1);
		memset(d , 0 , sizeof(d));
		d[0][0] = 1;
		for ( int i=1 ; i<=l ; ++i ) 
		{
			d[i][0] = 1;
			for ( int j=1 ; j<=19 ; ++j )
			{
				if ( pt[j]==s[i] ) 
					d[i][j] = (d[i-1][j-1] + d[i-1][j]) % 10000;
				else
					d[i][j] = d[i-1][j];
			}
		}
		printf("Case #%d: %04d\n" , ++cas , d[l][19]);
	}
	return 0;
}
