/*************************************
*Type         : Exam_Problem
*Task         : GCJ B
*Author       : This_poet
*Start Time   : 2012-4-14 13:20
*Finish Time  :
*Result       :
*Algorithm    : Greedy
*************************************/
# include <cstdio>
# include <cstring>
# include <algorithm>
# include <iostream>
# include <cmath>
# define Debug puts("Orz!")
# define outit(x) cout<<#x<<" = "<<x<<endl
# define ps system("pause")
using namespace std;
typedef long long ll;

int main()
{
	int t, n, s, p, a;
//	freopen( "in", "r", stdin );
//	freopen( "out", "w", stdout );
	scanf( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		scanf( "%d%d%d", &n, &s, &p );
		int ans = 0;
		while ( n -- )
		{
			scanf( "%d", &a );
			switch ( a % 3 )
			{
				case 0:
					if ( a / 3 >= p ) ans ++;
					else if ( a / 3 + 1 >= p && a / 3 > 0 && s > 0 ) ans ++, s --;
					break;
				case 1:
					if ( a / 3 + 1 >= p ) ans ++;
					break;
				case 2:
					if ( a / 3 + 1 >= p ) ans ++;
					else if ( a / 3 + 2 >= p && s > 0 ) ans ++, s --;
					break;
			}
		}
		printf( "Case #%d: %d\n", i, ans );
	}
	return 0;
}
