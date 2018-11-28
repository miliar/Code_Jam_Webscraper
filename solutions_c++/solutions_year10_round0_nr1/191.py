#include<stdio.h>
int main(){
	int t,cas=1;
	scanf("%d",&t);
	while(t--){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",cas++,(k&((1<<n)-1))==((1<<n)-1)?"ON":"OFF");
	}
}
