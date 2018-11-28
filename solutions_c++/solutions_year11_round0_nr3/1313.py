#include<iostream>
#include<stdio.h>
#include<string.h>


using namespace std;

int main() {
	int test, i , j , n,tc = 1 ;
	freopen("cs.in","r",stdin);
	freopen("cs.out","w",stdout);
	scanf("%d",&test);
	while( test -- && scanf("%d",&n) != EOF ) {
		int sum = 0 , minv = 10000001 ,ans = 0;
		for( i = 0 ; i < n;i++) {
			scanf("%d",&j);
			ans += j;
			sum ^= j;
			if( j < minv ) minv = j;
		}
		printf("Case #%d: ",tc++);
		if( sum ) puts("NO");
		else printf("%d\n",ans - minv );
	}
	return 0;
}
