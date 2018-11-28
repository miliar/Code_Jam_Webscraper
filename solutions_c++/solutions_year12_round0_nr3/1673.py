#include<iostream>
#include<cstring>
#include<cstdio>
int aa[10];
using namespace std;
int main()
{
	int cas;
	int a,b;
	scanf( "%d", &cas );
	for ( int i = 1; i <= cas; i++ )
	{
		int ans = 0;
		scanf( "%d%d", &a, &b );
		for ( int j = a; j <= b; j++ )
		{
			int k = j;
			int l = j;
			int t = 1;
			while ( k != 0 )
			{
				t = t * 10;
				k = k /10;
			}
			k = j;
			t = t / 10;
			aa[0] = 0;
			while ( k != 0 )
			{
				int l1 = l % 10;
				l = l / 10;
				l = l + l1 * t;
				if ( l > j && l <= b ) 
				{
//					printf("%d %d\n",j,l);
					bool u = true;
					for ( int lll = 1; lll <= aa[0]; lll++ )
					{
						if ( l == aa[lll] )
						{
							u = false;
							break;
						}
					}
					if ( u )
					{
						aa[++aa[0]] = l;
						ans++;
					}
				}
				k /= 10;
			}
		}
			printf( "Case #%d: %d\n",i,ans);
	}
	return 0;
}