#include <stdio.h>

int main(){
	int t,n,k,nn;
	scanf("%d",&t);
	for (int tc=1;tc<=t;tc++){
		scanf("%d %d",&n,&k);
		nn=(1<<n);k%=nn;
		if (k==(nn-1)) printf("Case #%d: ON\n",tc);
		else printf("Case #%d: OFF\n",tc);		
	}
}