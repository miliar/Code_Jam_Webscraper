#include <stdio.h>
#include <string.h>

int n;
int pO,pB;
int lenO,lenB;
int posO[110], posB[110];
char control[110];

int main() {
	int t;
	int c=0;
	
	scanf("%d",&t);
	while(t--) {
		lenO = lenB = pO = pB = 0;
		memset(control,0,sizeof(control));

		scanf("%d",&n);
		
		for(int i=0;i<n;++i) {
			int num;
			char op[10];
			
			scanf("%s",op);
			scanf("%d",&num);
			if( strcmp(op, "O") == 0) {
				control[i] = 0;
				posO[lenO++] = num;
			} else {
				control[i] = 1;
				posB[lenB++] = num;
			}
		}
		
		int ans=0;
		int ct=0;
		int nowO,nowB;
		nowO = nowB = 1;
		while( ct < n ) {
			bool press=false;
			++ans;
			//printf("%d: %d %d %d %d %d\n",ans,nowO,nowB,pO,pB,ct);
			//scanf("%*d");
			if(pB < lenB) {
				if(nowB > posB[pB]) {
					--nowB;
				} else if(nowB < posB[pB]) {
					++nowB;
				} else {
					if(control[ct] == 1) {
						++pB;
						++ct;
						press = true;
					}
				}
			}
			if(pO < lenO) {
				if(nowO > posO[pO]) {
					--nowO;
				} else if(nowO < posO[pO]) {
					++nowO;
				} else {
					if(!press && control[ct] == 0) {
						++pO;
						++ct;
					}
				}
			}
		}
		
		printf("Case #%d: %d\n",++c,ans);
	}
	
	return 0;
}
