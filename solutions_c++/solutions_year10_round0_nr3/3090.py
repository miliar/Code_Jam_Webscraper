#include<iostream>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    long long T,R,k,N,g[1000],round[1000],flag[1000],E[1000],Euros=0,i,j,s,gn,nor,c,diffR;
    scanf("%lld",&T);
    for (i=1;i<=T;i++)
    {
        scanf("%lld%lld%lld",&R,&k,&N);
        for (j=0;j<N;j++)
        {
            scanf("%lld",&g[j]);
            flag[j]=0;
        }
         
        Euros=0; 
        gn=0;    
        nor=0;
        do
        {
            nor++;
            if (flag[gn%N]==0)
            {
               flag[gn%N]=1;
               round[gn%N]=nor;
               E[gn%N]=Euros;
            }
            s=0;
            c=0;
            while (c<N && s+g[gn%N]<=k)
            {
                  s+=g[gn%N];
                  gn++;   
                  c++;
            }
            Euros+=s;
        }while (nor<R && flag[gn%N]==0);
        if (nor<R)
        {
           diffR=(nor-round[gn%N])+1;
           Euros=E[gn%N]+((R-round[gn%N])/diffR)*(Euros-E[gn%N]);
        
           for (j=round[gn%N]-1+((R-round[gn%N])/diffR)*diffR;j<R;j++)
           {
               c=0;
               s=0;
               while (c<N && s+g[gn%N]<=k)
               {
                     s+=g[gn%N];
                     gn++;   
                     c++;
               }
               Euros+=s;
           }
        }
        printf("Case #%lld: %lld\n",i,Euros);
    }
}
