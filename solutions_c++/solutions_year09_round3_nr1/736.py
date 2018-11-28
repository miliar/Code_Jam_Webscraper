#include <stdlib.h>
#include <stdio.h>

int c, N;
char n[200];
long long t;
int i, j, base;
char code[40];
char val[128];

int main() {
	scanf("%s", n);
	N=atoi(n);
	for (c=1; c<=N; c++) {
		scanf("%s", n);
		base=1;
		code[0]=n[0];
		for(i=1; n[i]; i++) {
			for(j=0; j<base; j++)
				if (n[i]==code[j]) break;
			if (j==base) {
				val[n[i]]=base;
				code[base++]=n[i];
			}
		}
		val[code[0]]=1;
		if (base<2) base=2;
		else val[code[1]]=0;

		t=0;
		for(i=0; n[i]; i++) {
			t=t*base+val[n[i]];
		}
		
		printf("Case #%d: %lld\n", c, t);
	}

}
