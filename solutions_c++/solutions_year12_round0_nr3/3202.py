#include<stdio.h>
#include<math.h>
int a,b,t,T,sum;
int main()
{
   freopen("C-small-attempt0.in", "r", stdin);
   freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d",&t);
    T=1;
    while(t--)
    {
        sum=0;
        scanf("%d %d",&a,&b);
        if(a<10) printf("Case #%d: 0\n",T++);
        else if(b<100)
        {
            for(int i=a;i<b;++i)
            {
                int tmp=(i%10)*10+i/10;
                if((tmp>i)&&(tmp<=b)) {sum++;}
            }
            printf("Case #%d: %d\n",T++,sum);
        }
        else if(b<=1000)
        {
            if(a<100)
            {
                for(int i=a;i<100;++i)
            {
                int tmp=(i%10)*10+i/10;
                if(tmp>i) sum++;
            }
                printf("Case #%d: %d\n",T++,sum);
            }
            else
            {
                for(int i=a;i<b;++i)
                {
                    int tmp=(i%100)*10+i/100;
                    int tmp1=(i%10)*100+i/10;
                    if(tmp>i&&tmp<=b) {sum++;}
                    if(tmp1>i&&tmp1<=b) {sum++;}
                }
                printf("Case #%d: %d\n",T++,sum);
            }
        }
    }
    return 0;
}
