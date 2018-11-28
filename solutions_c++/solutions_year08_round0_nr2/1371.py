#include <iostream>
#include <cstdlib>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
const double EPS=1e-6;
struct ss
{
    char sta,ev;
    double t;
}event[500];

int cmp(ss a,ss b)
{
    if(a.t==b.t)
        return a.ev<b.ev;
    return a.t<b.t;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

  //  freopen("my.in","r",stdin);
 //   freopen("my.out","w",d);
    int N,NA,NB,t,sen,tt,pe,a,b;
    double sa[510],sb[510],T;

    scanf("%d",&N);
    for(sen=1;sen<=N;sen++)
    {
        scanf("%lf",&T);
        T=T/60.0;
        scanf("%d%d",&NA,&NB);
        pe=0;
        for(t=0;t<NA;t++)
        {
            scanf("%d:%d",&a,&b);
            event[pe].sta='A';
            event[pe].ev='D';
            event[pe].t=(double)a+(double)b/60.0;
            pe++;
            scanf("%d:%d",&a,&b);

            event[pe].sta='B';
            event[pe].ev='A';
            event[pe].t=(double)a+(double)b/60.0;
            pe++;
        }
        for(t=0;t<NB;t++)
        {
            scanf("%d:%d",&a,&b);

            event[pe].sta='B';
            event[pe].ev='D';
            event[pe].t=(double)a+(double)b/60.0;
            pe++;
            scanf("%d:%d",&a,&b);

            event[pe].sta='A';
            event[pe].ev='A';
            event[pe].t=(double)a+(double)b/60.0;
            pe++;
        }

        sort(event,event+pe,cmp);

        int counta,countb,pa,pb,cura,curb;
        counta=countb=pa=pb=cura=curb=0;
        for(t=0;t<pe;t++)
        {
            if(event[t].ev=='D')
            {
                if(event[t].sta=='A')
                {
                   if(cura==0 || event[t].t-sa[pa-cura]<-EPS)
                        counta++;
                   else
                        cura--;
                }
                else
                {
                   if(curb==0 || event[t].t-sb[pb-curb]<-EPS)
                        countb++;
                   else
                        curb--;
                }
            }
            else
            {
                if(event[t].sta=='A')
                {
                    sa[pa]=event[t].t+(double)T;
                    pa++;
                    cura++;
                }
                else
                {
                    sb[pb]=event[t].t+(double)T;
                    pb++;
                    curb++;
                }
            }
        }
        printf("Case #%d: %d %d\n",sen,counta,countb);
    }
   // system("pause");
    return 0;
}
