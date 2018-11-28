#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>


#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

using namespace std;
int n, m;
int main( )
{
	int i, j, k, t, tt;
	int s,p,limit1,limit2,count,temp;
	
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		
        scanf( "%d", &n );
		scanf( "%d", &s );
		scanf( "%d", &p );
		limit1=(3*p)-4;
		limit2=3*(p-1);
		count=0;
		fi(n)
		{
            scanf( "%d", &temp );
			if(temp>=p)
			{
            if(temp<limit1) continue;
			else if(temp>limit2) count++;
			else 
			{
			    if(s)
				{
				   count++;
				   s--;
			    }
			}
			}
        }
		printf( "Case #%d: %d\n", t,count );
	}
	return 0;
}
