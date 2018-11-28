#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>


#define cri(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define cri1(a,b) cri( a, 0, ( b ) )
#define cri2(a) cri1( i, ( a ) )
#define cri3(a) cri1( j, ( a ) )
#define cri4(a) cri1( k, ( a ) )

using namespace std;
int n, m;
int main( )
{
int i, j, k, temp1, temp2;
int s,p,begpoint,endpoint,count,temp;
scanf( "%d\n", &temp2 );
for( temp1 = 1; temp1 <= temp2; ++ temp1 )
{
scanf("%d",&n);
scanf("%d",&s);
scanf("%d",&p);
begpoint=(3*p)-4;
endpoint=3*(p-1);
count=0;
cri2(n)
{
scanf("%d",&temp);
if(temp>=p)
{
            if(temp<begpoint) continue;
else if(temp>endpoint) count++;
else if(temp<=endpoint&&temp>=begpoint)
{
   if(s)
{
  count++;
  s--;
   }
}
}
        }
printf( "Case #%d: %d\n", temp1,count );
}
return 0;
}
