#include <stdio.h>

int main()
{
	int n, k, t, i, ans, tcnt=1;
	__int64 dy[31];
	scanf("%d",&t);
	dy[1]=1;
	for( i=2; i<=30; i++ )
		dy[i] = dy[i-1]*2+1;
	while( t-- ) { 
		scanf("%d %d",&n, &k);
		for( i=1; ; i++ ) {
			if( dy[n] * i + (i-1) ==  k ) {
				ans = 1;
				break;
			}
			else if(  dy[n] * (__int64)i +(__int64) (i-1) >  (__int64)k )
			{
				ans =0 ;
				break;
			}
		}
		printf("Case #%d: ", tcnt++);
		if( ans )
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
