#include <stdio.h>
#include <stdlib.h>

int freq[1001];

int compare (const void * a, const void * b)
{
  return -( *(int*)a - *(int*)b );
}


int main(){
    
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0_out.txt","w",stdout);
    
    int N;
    scanf("%d",&N);
    
    for(int i=0;i<N;i++)
    {
        int P,K,L;
        scanf("%d %d %d",&P,&K,&L);
        int j;
        for(j=0;j<L;j++)
        scanf("%d ",&freq[j]);
        
        qsort(freq,L,sizeof(int),compare);
        
        int sum=0;
        bool possible=false;
        for(j=0;j<P;j++)
        {
            for(int t=0;t<K;t++)
            {
                if(j*K+t==L)
                {
                    possible=true;
                    break;
                }
                sum+=freq[j*K+t]*(j+1);
            }
            if(possible)
            break;
        }
        printf("Case #%d: %d\n",i+1,sum);
    }
    
    return 0;
}
