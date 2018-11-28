#include <stdio.h>
#include <stdlib.h>

int t,r,k,n;
int table[1005],money[1005],to[1005];

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j,l;
    scanf("%d",&t);
    int count=0,remain,x;
    for(i=1;i<=t;i++){
        scanf("%d%d%d",&r,&k,&n);
    	for(j=1;j<=n;j++){
    		scanf("%d",&table[j]);
    	}
    	for(j=1;j<=n;j++){
    	    remain=k;
    	    money[j]=table[j];
    	    remain-=table[j];
    	    l=j+1;
    	    if(l>n){
    	    	l=1;
    	    }
    	    while(remain>=table[l] && l!=j){
    	        remain-=table[l];
    	        money[j]+=table[l];
    	        l++;
                if(l>n){
                    l=1;
                }
    	    }
    	    to[j]=l;
    	}
        count=0;
        x=1;
        for(j=r;j>=1;j--){
            count+=money[x];
            x=to[x];
        }
        printf("Case #%d: %d\n",i,count);
    }
	return 0;
}
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/
