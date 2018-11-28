#include <cstdio>
int T,n,k;
int main(){
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", i, (k%(1<<n))^((1<<n)-1)?"OFF":"ON");
	}
}
