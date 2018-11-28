
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long LL;
typedef unsigned long long ULL;

char wtcj[]="welcome to code jam";
const int ws = sizeof(wtcj)-1;

int main() {
	int N;
	scanf("%d ",&N);

	for( int n=0; n<N; n++ ) {
		char str[505];
		//scanf("%s ",str);
		fgets(str,505,stdin);
		int sl = strlen(str);
		if(str[sl-1]=='\n'){
			sl--;
		}

		unsigned table[ws+1];
		memset(table,0,sizeof(table));
		table[ws]=1;

		for(int s=sl-1;s>=0;s--){
			for(int w=0;w<ws;w++) {
				if(wtcj[w]==str[s]) {
					table[w]+=table[w+1];
				}
			}
		}

		printf("Case #%d: %.4d\n",n+1,table[0]%10000);
	}

	return 0;
}

