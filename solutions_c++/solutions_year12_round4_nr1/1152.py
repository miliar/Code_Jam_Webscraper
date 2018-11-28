#include <stdio.h>

#define INF 1999999999

struct Vine{
	int po;
	int le;
	int max;
};

int min(int a,int b){
    if(a<b){
    	return a;
    }
    return b;
}

int n;
Vine vine[10005];
int L;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int zz,xx;

    int a,b;
    scanf("%d",&xx);
    for(zz=1;zz<=xx;zz++){
        scanf("%d",&n);
        for(i=1;i<=n;i++){
        	scanf("%d%d",&vine[i].po,&vine[i].le);
        	vine[i].max=0;
        }
        vine[1].max=vine[1].po;
        scanf("%d",&L);
        int temp;
        for(i=2;i<=n;i++){
            for(j=1;j<i;j++){
                if(vine[i].po<=vine[j].po+vine[j].max){
                    temp=min(vine[i].po-vine[j].po,vine[i].le);
                	if(vine[i].max<temp){
                		vine[i].max=temp;
                	}
                }
            }
        }
    	printf("Case #%d: ",zz);
    	for(i=1;i<=n;i++){
    	    //printf("%d %d %d\n",i,vine[i].po,vine[i].max);
            if(vine[i].po+vine[i].max>=L){
                printf("YES\n");
                break;
            }
    	}
    	if(i==n+1){
    		printf("NO\n");
    	}
    }
	return 0;
}
/*
4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
*/
