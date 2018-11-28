#include <stdio.h>
#include <string.h>
#include <memory.h>
#define LEN 19
char a[20] = "welcome to code jam";
long f[LEN*2],g[LEN*2];
long n;

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d\n",&n);
	for (long _=1;_<=n;_++) {
		memset(f,0,sizeof(f));
		char cur=getchar();
		while (cur!='\n') {
			memset(g,0,sizeof(g));
			for (long i=0;i<LEN;i++)
				if (a[i]==cur) 
					if (i) g[i] = f[i-1];
					else g[i] = 1;
			for (long i=0;i<LEN;i++) f[i] = (f[i]+g[i]) % 10000;
			cur = getchar();
		}			
		printf("Case #%d: %.4d\n",_,f[LEN-1]);
	}

	return 0;
}
