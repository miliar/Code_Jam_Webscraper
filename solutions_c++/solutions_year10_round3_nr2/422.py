#include <iostream>
#include <math.h>
using namespace std;

int min(int a, int b)
{
	if (a < b) return a;
	return b;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("small.txt","w",stdout);
	__int64 L,P,C;
	__int64 cases,cas = 1,i,low;
	scanf("%I64d",&cases);
	while(cases --)
	{
		scanf("%I64d %I64d %I64d",&L,&P,&C);
		for( i = 0 ; ; i++ ) 
		{
			low = L * pow( C, pow( 2.0 , i ) ) ;
			if( low >= P )
				break ; 
		}
		printf("Case #%I64d: %I64d\n",cas++,i);
		
	}
	return 0;
}