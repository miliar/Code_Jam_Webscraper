#include <stdio.h>

int a[1000];

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		int l,n,c;
		long long t;
		scanf("%d%lld%d%d", &l,&t,&n,&c);
		for(int i=0;i<c;i++){
			scanf("%d", &a[i]);
		}
		long long ret=0;
		if(l==0){
			for(int i=0;i<n;i++){
				ret+=a[i%c];
			}
			ret*=2;
		}else if(l==1||n==1){
			long long best=-1;
			for(int k=0;k<n;k++){
				ret=0;
				for(int i=0;i<n;i++){
					if(i == k){
						if(ret+a[i%c]>t){
							if(ret >= t){
								ret += a[i%c];
							}else{
								ret = t+a[i%c]-(t-ret)/2;
							}
						}else{
							ret += a[i%c]*2;
						}
					}else{
						ret+=a[i%c]*2;
					}
				}
				if(best==-1 || best>ret){
					best=ret;
				}
			}
			ret=best;
		}else if(l==2){
			long long best=-1;
			for(int k=0;k<n;k++){
				for(int k2=k+1;k2<n;k2++){
					ret=0;
					for(int i=0;i<n;i++){
						if(i == k||i==k2){
							if(ret+a[i%c]>t){
								if(ret >= t){
									ret += a[i%c];
								}else{
									ret = t+a[i%c]-(t-ret)/2;
								}
							}else{
								ret += a[i%c]*2;
							}
						}else{
							ret+=a[i%c]*2;
						}
					}
					if(best==-1 || best>ret){
						best=ret;
					}
				}
			}
			ret=best;
		}
		printf("Case #%d: %lld\n", TT, ret);
	}
}