#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>


#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
int n, m;
int main( )
{
	int i, j, k, t, tt;
	int s,p,begin,end,count,temp;
	
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		
        n = ni( );
		s=ni();
		p=ni();
		begin=(3*p)-4;
		end=3*(p-1);
		count=0;
		fi(n)
		{
            temp=ni();
			if(temp>=p)
			{
            if(temp<begin) continue;
			else if(temp>end) count++;
			else if(temp<=end&&temp>=begin)
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
