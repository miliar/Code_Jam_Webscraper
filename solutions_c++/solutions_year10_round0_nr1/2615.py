#include <stdio.h>

int s[35],n,k;

int pow(int a,int b){
	int re=1,i;
	for(i=0;i<b;i++) re*=a;
	return re;
}

int main(void){
	int tt,t;
	scanf("%d",&tt);
	for(t=0;t<tt;t++){
		scanf("%d %d",&n,&k);
		if((k+1)%pow(2,n) == 0){
			printf("Case #%d: ON\n",t+1);
		}else{
			printf("Case #%d: OFF\n",t+1);
		}
	}
	return 0;
}
