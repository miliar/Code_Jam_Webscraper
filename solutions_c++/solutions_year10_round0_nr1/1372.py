#include <stdio.h>
#include <stdlib.h>

int t;
int n,k;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    scanf("%d",&t);
    int x,y;
    for(i=1;i<=t;i++){
    	scanf("%d%d",&n,&k);
    	x=1<<n;
    	y=k%x;
    	if(y!=x-1){
    		printf("Case #%d: OFF\n",i);
    	}else{
    		printf("Case #%d: ON\n",i);
    	}
    }
	return 0;
}
