#include <memory.h>
#include <stdio.h>
#include <string.h>
const long N = 1111;
long ans[N],n;
char sample[N] = "welcome to code jam";
char q[N];

int main(void) {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d\n",&n);
	for (long T=1;T<=n;T++) {
		gets(q); memset(ans,0,sizeof(ans));
		long len = strlen(q);	
		for (long i=0;i<len;i++) {
			for (long j=19;j>0;j--)
				if (q[i]==sample[j]) ans[j] = (ans[j]+ans[j-1])%10000;
			if (q[i]==sample[0]) ans[0] = (ans[0]+1)%10000;
		}

		printf("Case #%d: %.4d\n",T,ans[18]);
	}

	return 0;
}
