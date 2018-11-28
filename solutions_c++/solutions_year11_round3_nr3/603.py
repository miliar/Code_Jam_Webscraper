#include<stdlib.h>
#include<stdio.h>

int main()
{
    int T,N;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("csmall-attempt.out","w",stdout);
    scanf("%d",&T);
    //printf("%d",T);
    for(int i=0;i<T;i++)
    {
            int N,L,H;
            scanf("%d%d%d",&N,&L,&H);
            int a[1000];
            for(int j=0;j<N;j++)
            {
                    scanf("%d",&a[j]);
            }
            int flag=1;
            int min=H;
            int flag2=1;
            for(int k=L;k<=H;k++)
            {
                    flag2=1;
                    for(int j=0;j<N;j++)         
                    {
                            if(a[j]%k==0||k%a[j]==0)
                                                    {
                                                        flag2*=1;
                                                    }
                            else
                                flag2*=0;
                    }
                    if(flag2==1)
                    {
                           min=k;
                           break;
                    }
                               
            }
            printf("Case #%d: ",i+1);
            if(flag2==0)
                       printf("NO\n");
            else
                       printf("%d\n",min);
    }
   // system("pause");
}
            
            
            
