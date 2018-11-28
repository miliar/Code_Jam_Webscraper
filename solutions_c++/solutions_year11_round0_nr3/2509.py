#include <stdio.h>

#define INF 1999999999

int n;
int min;
int sum;
int sumAnd;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
        sum=0;
        sumAnd=0;
        min=INF;
    	scanf("%d",&n);
    	int x;
    	for(i=1;i<=n;i++){
    		scanf("%d",&x);
    		sum+=x;
            sumAnd=(sumAnd^x);
            if(min>x){
            	min=x;
            }
    	}
    	printf("Case #%d: ",xx);
    	if(sumAnd!=0){
    		printf("NO\n");
    	}else{
    	    printf("%d\n",sum-min);
        }
    }
	return 0;
}
/*
2
5
1 2 3 4 5
3
3 5 6
*/
