#include <stdio.h>

int f[100];

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		int n,l,h;
		scanf("%d%d%d", &n,&l,&h);
		for(int i=0;i<n;i++){
			scanf("%d", &f[i]);
		}
		int ret = -1;
		for(int ans=l;ans<=h;ans++){
			bool ok=1;
			for(int i=0;i<n;i++){
				if(!(ans % f[i] == 0 || f[i] % ans == 0)){
					ok=0;
					break;
				}
			}
			if(ok){
				ret=ans;
				break;
			}
		}
		printf("Case #%d: ", TT);
		if(ret==-1){
			printf("NO\n");
		}else{
			printf("%d\n", ret);
		}
	}
}