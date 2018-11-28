#include<stdio.h>

int main(){
    //freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t,n,k,f=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",f++);
		if(k%(1<<n)==(1<<n)-1){
		    printf("ON\n");	
		}	
		else printf("OFF\n");
	}
	return 0;	
}
