#include<stdio.h>
#include<math.h>

int main() 
{
    freopen("A-large.in","rt",stdin);
   	freopen("A-large.out","wt",stdout);
	int total_cases;	
    int i,value,power_flag;
	scanf("%d",&total_cases);
	for (i=0; i<total_cases; i++) 
    {
		int n, k;
		scanf("%d",&n);
		scanf("%d",&k);
		printf("\nCase #%d: ",i+1);		
        value = int(pow(2,n)) - 1;
        power_flag = 0;
        while(value <= k)
        {
           if(value==k)
           {
                printf("ON");
                power_flag = 1;
           }
                value = value + int(pow(2,n));                      
        }
        if(power_flag == 0)
                printf("OFF");               
	}
    return 0;
}

