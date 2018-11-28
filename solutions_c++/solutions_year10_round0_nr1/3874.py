#include<cstdio>
int main(){
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	int T;
	int n,k;
	int i,j;
	int cnt = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&k);
		k%=(1<<n);
		printf("Case #%d: ",cnt++);
		if(k==((1<<n) - 1)){
			puts("ON");
		}else{
			puts("OFF");
		}
	}
	return 0;
}