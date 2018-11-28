#include <stdio.h>

int l,p,c;
int main() {
	int id=1;int t;scanf("%d",&t);
	while(t--) {
		int wyn=0;
		scanf("%d%d%d",&l,&p,&c);
		int ile=0;
		long long pc=l;
		while(pc<p) {
			pc=pc*c;
			ile++;
		}
		int b=0;
		while(ile>1) {
			wyn++;
			if(ile%2!=0) b=1;
			ile/=2;
		}wyn+=b;
		printf("Case #%d: %d\n",id++,wyn);
	}
	return 0;
}
