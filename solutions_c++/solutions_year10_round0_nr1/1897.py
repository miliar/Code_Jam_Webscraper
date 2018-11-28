#include <stdio.h>
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, n, k, ttt=1;
	for(scanf("%d",&T);T>0;T--){
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n", ttt++, k%(1<<n) == (1<<n) - 1?"ON":"OFF");
	}	
}