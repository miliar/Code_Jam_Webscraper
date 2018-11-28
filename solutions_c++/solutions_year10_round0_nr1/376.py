#include<cstdio>
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int n,k,t,tt=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",tt++);
		puts(k%(1<<n)==(1<<n)-1?"ON":"OFF");
	}
	return 0;
}
