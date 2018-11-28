#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>


#define try1(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define try2(a,b) try1( a, 0, ( b ) )
#define try3(a) try2( i, ( a ) )
#define try4(a) try2( j, ( a ) )
#define try5(a) try2( k, ( a ) )

using namespace std;

int n, m;
int main( )
{
	int i, j, k, try6, try7;
	int s,p,beg,ed,count,temp;
	
	scanf( "%d\n", &try7 );
	for( try6 = 1; try6 <= try7; ++ try6 )
	{
		
       	scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		beg=(3*p)-4;
		ed=3*(p-1);
		count=0;
		try3(n)
		{
            scanf("%d",&temp);
			if(temp>=p)
			{
            if(temp<beg) continue;
			else if(temp>ed) count++;
			else if(temp<=ed&&temp>=beg)
			{
			    if(s)
				{
				   count++;
				   s--;
			    }
			}
			}
        }
		printf( "Case #%d: %d\n", try6,count );
	}
	return 0;
}
