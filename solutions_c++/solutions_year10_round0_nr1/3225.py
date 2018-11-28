#include<stdio.h>
#include<math.h>

int main() 
{
    freopen("A-large.in","rt",stdin);
   	freopen("A-large.out","wt",stdout);
	int T;	int i,x,flag;
	scanf("%d",&T);
	for (i=0; i<T; i++) {
		int n, k;
		scanf("%d",&n);
		scanf("%d",&k);
		printf("\nCase #%d: ",i+1);		
        x = int(pow(2,n)) - 1;
        flag = 0;
        while(x <= k){
                if(x==k){
                         printf("ON");
                         flag = 1;
                         }
                x = x + int(pow(2,n));                      
        }
        if(flag == 0)
                printf("OFF");               
	}
    return 0;
}

