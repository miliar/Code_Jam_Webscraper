#include <stdio.h>
#include <string.h>
#include <memory.h>
#define L 22
#define D 5555
long l,d,n;
char a[D][L],b[11111];
bool can[L][255];

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d%d%d\n",&l,&d,&n);
	for (long i=0;i<d;i++) scanf("%s\n",&a[i]);
	
	for (long _=1;_<=n;_++) {
		long pos=0;
		scanf("%s\n",&b);
        	for (long i=0;i<l;i++)
        		if (b[pos]=='(') {
        			while (b[pos]!=')') can[i][b[pos++]] = 1;
        			pos++;
        		} else can[i][b[pos++]] = 1;

		long ans = 0;
		for (long i=0;i<d;i++) {
			long flag = 1;
                        for (long j=0;j<l;j++)
                        	if (!can[j][a[i][j]]) {
                        		flag = 0;
                        		break;
                        	}
			ans += flag;
		}

		printf("Case #%d: %d\n",_,ans);
		memset(can,0,sizeof(can));
	}

	return 0;
}

