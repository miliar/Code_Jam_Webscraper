#include <stdio.h>
#include <math.h>

static bool snapperChain(int n, int k);
static int t(int n);

int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int n,k;
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",i+1,snapperChain(n,k)?"ON":"OFF");
	}

	return 1;
}

static bool snapperChain(int n, int k){
	return (k+1)%(t(n)+1)==0;
}

static int t(int n){
	if(n<=0) return 0;
	if(n==1) return 1;
	return t(n-1)+(int)pow(2,n-1);
}
