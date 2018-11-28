
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int U32;

int main() {
	int N;
	scanf("%d",&N);

	for( int n=0; n<N; n++ ) {
		char buf[30];
		scanf("%s",buf);

		int nc[10];
		memset(nc,0,sizeof(nc));

		char *c =buf;
		while(*c!=0) {
			c++;
		}

		c--;
		while(c >= buf) {
			int s = *c-'0';
			nc[s]++;
			int a;
			for(a=s+1;a<10;a++) {
				if( nc[a] > 0 ) {
					*c = a+'0';
					nc[a]--;
					c++;
					a = 100;
					break;
				}
			}
			if( a == 100) break;
			c--;
		}

		if( c < buf ) {
			nc[0]++;
			c = buf;
			for(int a=1;a<10;a++) {
				if( nc[a] > 0 ) {
					*c = a+'0';
					nc[a]--;
					c++;
					break;
				}
			}
		}
		
		for(int a=0;a<10;a++) {
			while( nc[a] > 0 ) {
				*c = a+'0';
				nc[a]--;
				c++;
			}
		}
		*c = 0;

		printf("Case #%d: %s\n",n+1,buf);
	}

	return 0;
}

