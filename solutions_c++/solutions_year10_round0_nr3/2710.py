#include<stdlib.h>
#include<stdio.h>
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int i,j,T,R,K,N,a[50],w;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        int sum=0,t=0,k=0;
        scanf("%d%d%d",&R,&K,&N);    
        for(j=0;j<N;j++)
           {
               scanf("%d",&a[j]);
           }
    for(w=0;w<R;w++)
    {int q=0;
         do
            {
                t=t+a[k];k++;q++;
                if(k>=N)k=k%N;
            }while(t+a[k]<=K&&q<N);
     sum+=t;t=0;q=0;
    }
    printf("Case #%d: %d\n",i,sum);
    k=0;
    sum=0;
    }
    
   // system("pause");
    return 0;
}
