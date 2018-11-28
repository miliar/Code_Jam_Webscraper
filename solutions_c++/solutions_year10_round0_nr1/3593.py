#include<stdio.h>

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int n,k;
	int Test;
	scanf("%d", &Test);
	for(int i=1;i<=Test;++i){
		scanf("%d%d", &n, &k);
		if((k&((1<<n)-1))==((1<<n)-1))printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	return 0;
}
