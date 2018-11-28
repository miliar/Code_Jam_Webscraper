/*
TASK: theme_park_google_code_jam_10
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int x,t,r,k,n,i,j;
    int g[1010];
    int calc[1010][2];
    int cur;
    
    long long ans,add;
    
    scanf("%d", &t);
    
    for(x=1;x<=t;x++)
    {
        ans = 0;
        scanf("%d%d%d", &r,&k,&n);
        
        add=0;
        
        for(i=0;i<n;i++)
        {
            scanf("%d", &g[i]); 
            add+=g[i];
        }
        
        if(add<=k)
        {
            ans = add*r;
            printf("Case #%d: ",x);
            printf("%I64d\n", ans);        
            continue;
        }

        for(i=0;i<n;i++) //calc : if begin with this, end where? how many ppl?
        {
            add=0;
            
            for(j=i;;)
            {
                add+=g[j];
                
                if(add>k)
                {
                    add-=g[j];
                    calc[i][0]=add; //how many ppl
                    calc[i][1]=j; //start anew at j
//                    printf("calc[%d][0]=%d\ncalc[%d][1]=%d\n",i,calc[i][0], i,calc[i][1]);
                    break;
                }
                
                j=((j+1)%n);
                if(j==i) //won't happen bcuz not everyone can be on it at same time
                    break;
            }
        }
        
        cur = 0;
        ans = 0;
        
        for(i=0;i<r;i++)
        {
            ans+=calc[cur][0];
            cur= calc[cur][1];
        }

        printf("Case #%d: ",x);
        printf("%I64d\n", ans);        
    }
    
    return 0;
}
