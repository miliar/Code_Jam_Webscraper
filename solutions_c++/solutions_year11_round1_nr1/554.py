#include <stdio.h>

long long n,pd,pg;
long long maybe[9]={1,2,4,5,10,20,25,50,100};

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
    	scanf("%I64d%I64d%I64d",&n,&pd,&pg);
    	for(i=0;i<9;i++){
    		if((pd*maybe[i])%100==0){
    			break;
    		}
    	}
    	if(i==9 || maybe[i]>n){
    		printf("Case #%d: Broken\n",xx);
    	}else{
    	    if(pg==100 && pd!=100){
    		    printf("Case #%d: Broken\n",xx);
    	    }else if(pg==0 && pd!=0){
    		    printf("Case #%d: Broken\n",xx);
    	    }else{
    		    printf("Case #%d: Possible\n",xx);
    	    }
        }
    }
	return 0;
}
/*
3
1 100 50
10 10 100
9 80 56
*/
