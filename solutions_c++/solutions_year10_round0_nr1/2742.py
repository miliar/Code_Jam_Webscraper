#include<stdio.h>
#include<string.h>
#include<stdio.h>
//#include<algorithm>
#include<string.h>
#include <stdlib.h>
#include<ctype.h>
#include<vector>
#include<math.h>

int main()
{
    
  long long k;
    long n;
    long i=0,t;
   freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);  
    
    

    scanf("%ld",&t);

    
    for(i=0;i<t;i++)
       {
        scanf("%ld %lld",&n,&k);        
        
        
        
        printf("Case #%ld: ",i+1);
        if(k==0)
                {
                printf("OFF\n");
                continue;
                }
        
        k=k%(long)pow(2,n);
        if(k==pow(2,n)-1)
                    {
                    printf("ON\n");
                    }
        else
        {
        printf("OFF\n");
        }
            // printf("%d %ld\n",n,k);
       }
       
}

