#include<stdio.h>
int main(){
	int n,k;
	int cases=0;
	int T;
//	freopen("g:\\A-large.in","r",stdin);
//	freopen("g:\\A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",++cases);
		if((k&((1<<n)-1))==((1<<n)-1)) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}