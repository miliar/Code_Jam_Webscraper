#include <stdio.h>

void sort(int &t1,int &t2,int &t3)
{
    int tt;
    if(t1<t2){tt=t1;t1=t2;t2=tt;}
    if(t2<t3){tt=t2;t2=t3;t3=tt;}
    if(t1<t2){tt=t1;t1=t2;t2=tt;}
}

int cdivisor(int m,int n)
{
    int t;
    if(m<n) {t=m;m=n;n=t;}
    while(m%n)
    {
        t=m%n;
        m=n;
        n=t;
    }
    return n;
}

int main()
{
  //  freopen("B-small-attempt2.in","r",stdin);
  //  freopen("B-small.out","w",stdout);

    int C,N;
    int t1,t2,t3,divisor,base,watcher;
    scanf("%d",&C);
    for(int i=0;i<C;i++)
    {
        printf("Case #%d: ",i+1);
        scanf("%d",&N);
        if(N==2)
        {
            scanf("%d%d",&t1,&t2);
            if(t1<t2)
            {
                t3=t1;
                t1=t2;
                t2=t3;
            }
            divisor=t1-t2;
            base=(t2-1)/divisor;
            printf("%d\n",watcher=(base+1)*divisor-t2);
        }
        else
        {
            scanf("%d%d%d",&t1,&t2,&t3);
            sort(t1,t2,t3);
            if(t1!=t2&&t2!=t3)
            {
              divisor=cdivisor(t1-t2,t2-t3);
              base=(t3-1)/divisor;
              printf("%d\n",watcher=(base+1)*divisor-t3);
            }
            else if(t1!=t2)
            {
              divisor=t1-t2;
              base=(t2-1)/divisor;
              printf("%d\n",watcher=(base+1)*divisor-t2);
            }
            else if(t2!=t3)
            {
              divisor=t2-t3;
              base=(t3-1)/divisor;
              printf("%d\n",watcher=(base+1)*divisor-t3);
            }
        }
    }
}
