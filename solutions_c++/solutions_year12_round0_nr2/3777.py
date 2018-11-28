#include<cstdio>
using namespace std;
int num[205];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,n,s,p;
    scanf("%d",&t);
    for(int ti=1;ti<=t;++ti)
    {
            scanf("%d%d%d",&n,&s,&p);
            for(int i=0;i<n;++i)
               scanf("%d",&num[i]);
            int summ=0;
            for(int i=0;i<n;++i)
            {
                    if(p==1)
                    {
                            if(num[i]!=0)
                               summ++;
                            continue;
                    }
                    if(p==0)
                    {
                            summ++;
                            continue;
                    }
                    if(num[i]>=(3*p-2))
                      summ++;
                    else if((3*p-4)<=num[i]&&num[i]<(3*p-2))
                    {
                         if(s>0)
                         {
                                summ++;
                                s--;
                         }
                    }
            }
            printf("Case #%d: %d\n",ti,summ);
    }
    return 0;
}
            
