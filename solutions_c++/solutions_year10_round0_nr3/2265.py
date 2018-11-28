#include<stdio.h>
#include<cmath>
#include <queue>
#include <cstring>
#include <cstdlib>

using namespace std;

int waitq[10000];

int main()
{
    #ifndef ONLINE_JUDGE 
    freopen("in.txt","r",stdin); 
    freopen("out.txt","w",stdout); 
    #endif

     
    int i,j,ii,r,k,n,case_num,temp,people_sum,stage;
    long int sum;    
    int groups[10];
    
    scanf("%d", &case_num);    
    for(i=1;i<=case_num;i++)
    {
        scanf("%d%d%d", &r, &k, &n);
        
        people_sum=0;
        for(j=0;j<n;j++)
        {
            scanf("%d", &groups[j]);
            people_sum+=groups[j];
        }
        
        for(ii=0;ii<r;ii++)
        {
            for(j=0;j<n;j++)
            {
                waitq[ii*n+j]=groups[j];
            }
        }
        
        if(people_sum<=k)
        {
            printf("Case #%d: %d\n", i, people_sum*r);
            continue;
        }
        
        temp=0;
        ii=0;
        sum=0;
        stage=1;
        while(stage<=r)
        {
            for(j=0;j<n;j++)
            {
                temp+=waitq[ii+j];
                if(temp>k)
                {
                    sum+=(temp-waitq[ii+j]);
                    temp=0;
                    ii+=j;
                    stage++;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", i, sum);                  
     }
    
    #ifndef ONLINE_JUDGE 
    fclose(stdin); 
    fclose(stdout); 
    #endif



 

    return 0;
}
