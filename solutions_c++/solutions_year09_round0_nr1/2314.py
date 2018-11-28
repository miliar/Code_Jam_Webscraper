#include <stdio.h>
#include <string.h>
#include <memory.h>
const long maxd = 5555;
const long maxl = 22;
long l,d,n,p,ans;
char sample[11111],str[maxd][maxl];
bool can[maxl]['z'];

int main(void) {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d%d%d\n",&l,&d,&n);
	for (long i=0;i<d;i++) scanf("%s\n",&str[i]);
	
	for (long T=1;T<=n;T++) {
		p = 0;
		scanf("%s\n",&sample);
        	for (long i=0;i<l;i++)
        		if (sample[p++]=='(') while (!p || sample[p-1]!=')') can[i][sample[p++]] = 1;
        		else can[i][sample[p-1]] = 1;

		ans = 0;
		for (long i=0;i<d;i++) {
			long flag = 1;
                        for (long j=0;j<l;j++)
                        	if (!can[j][str[i][j]]) {
                        		flag = 0;
                        		break;
                        	}
			ans += flag;
		}

		printf("Case #%d: %d\n",T,ans);
		memset(can,0,sizeof(can));
	}

	return 0;
}

