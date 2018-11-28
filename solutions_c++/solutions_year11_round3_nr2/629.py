#include<stdlib.h>
#include<stdio.h>
#include<algorithm>

int main()
{
    int T,N;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("bsmall-attempt.out","w",stdout);
    scanf("%d",&T);
    //printf("%d",T);
    for(int i=0;i<T;i++)
    {
            int L,t,N,C;
            int a[1050];
            scanf("%d%d%d%d",&L,&t,&N,&C);
            for(int j=0;j<C;j++)
            {
                    scanf("%d",&a[j]);
            }
            int b[10500][10];
            memset(b,-1,sizeof(b));
            b[0][0]=0;
            for(int j=0;j<N;j++)
            {
                    int x=2*a[j%C];
                    for(int k=0;k<=L;k++)
                    {
                            if(b[j][k]==-1) 
                                            continue;                            
                            if(b[j+1][k]==-1||b[j+1][k]>b[j][k]+x)
                            {
                                      b[j+1][k]=b[j][k]+x;
                            }   
                            if(k==L)
                                    continue;
                            int wait=t-b[j][k];
                            if(wait<0)
                                      wait=0;
                            int add=(x-wait)/2+wait;
                            if(b[j+1][k+1]==-1||b[j+1][k+1]>b[j][k]+add)
                            {
                                 b[j+1][k+1]=b[j][k]+add;
                            }
                    }
            }
            printf("Case #%d: %d\n",i+1,b[N][L]);
    }
    //system("pause");
}        
                                    
                                    
                                    
                                    
                                    
                                    
