#include<stdio.h>
#include<string.h>
#include<stdio.h>
//#include<algorithm>
#include<string.h>
#include <stdlib.h>
#include<ctype.h>
#include<vector>
#include<math.h>
int group[1001];

int main()
{
    
    int t;
     //  freopen("C-small-attempt0.in","r",stdin);
   // freopen("output.txt","w",stdout);  
        
    scanf("%d",&t);
        int i=0;
        int j=0;
        
      long r,k,n;
        
       long queue_start=0,x;
       long sum=0,total_sum=0;
        
    for(i=0;i<t;i++)
       {
        scanf("%ld %ld %ld",&r,&k,&n);        
        for(j=0;j<n;j++)
            {
            scanf("%d",&group[j]);
        //    printf("%d accptd  " ,group[j]);
            }
        group[j]=0;
       queue_start=0;
       total_sum=0;
       
       int counter;
       for(j=0;j<r;j++)
           {
           sum=0;  
           counter=0;  
           for(x=queue_start;(sum+group[x])<=k;)
                {
                
                
                sum=sum+group[x];
                x++;
                if(x>n)
                   x=0;
                
              
                counter++;
            //    printf("\n Counter %d\n",counter);
                if(counter>n)
                            {
                            x=0;
                             break;
                             }
                }
           
           total_sum+=sum;
          // printf("%d +",sum);
           queue_start=x;
           
        //   printf("\nQueu_start =%d \n",queue_start);
           }
           printf("Case #%ld: ",i+1);
       printf("%ld\n",total_sum);
       
       }
       
}
