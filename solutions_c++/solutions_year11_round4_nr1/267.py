#include<iostream>
using namespace std;
const int maxn=3000;
pair<double,double> d[maxn];
int m;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    double v1,v2,lim,ans;
    int L,n,cases,tt,i,a,b,c;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d%lf%lf%lf%d",&L,&v1,&v2,&lim,&n);
        m=0;
        c=0;
        while (n)
        {
              n--;
              scanf("%d%d",&a,&b);
              if (a!=c)
              {
                       d[m].first=0;
                       d[m].second=a-c;
                       m++;
              }
              d[m].second=b-a;
              scanf("%lf",&d[m].first);
              m++;
              c=b;
        }
        if (c<L) 
        {
           d[m].first=0;
           d[m].second=L-c;
           m++;
        }
        sort(d,d+m);
        ans=0;
        for (i=0;i<m;i++)
        if (lim>0)
        {
           if (d[i].second/(v2+d[i].first)<=lim)
           {
              ans+=d[i].second/(v2+d[i].first);
              lim-=d[i].second/(v2+d[i].first);
           }
           else
           {
               d[i].second-=lim*(v2+d[i].first);
               ans+=lim;
               ans+=d[i].second/(v1+d[i].first);
               lim=0;
           }
        }
        else ans+=d[i].second/(v1+d[i].first);
        printf("Case #%d: %.10lf\n",tt+1,ans);
    }
    return 0;
}
