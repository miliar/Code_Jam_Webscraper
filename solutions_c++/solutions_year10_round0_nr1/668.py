#include<stdio.h>
#include<memory.h>
int T,n,k;
int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",_,(((k+1)&((1<<n)-1))==0)?"ON":"OFF");
	}
	return 0;
}
