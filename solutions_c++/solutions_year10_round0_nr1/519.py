#include <stdio.h>

int main(){
	int t,n,k,u;
	scanf("%d",&t);
	for (u=1; u<=t ;u++){
		scanf("%d%d",&n,&k);
		while(n && k%2==1){
			n--;
			k/=2;
		}
		if (n) printf("Case #%d: OFF\n",u);
		else printf("Case #%d: ON\n",u);
	}
	return 0;	
}		
		
