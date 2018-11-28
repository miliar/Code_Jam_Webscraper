#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;
int a,b,c,d,e,g,h,i;
double f,ans,sem;
pair<double,pair<int,int> > p[1005];
int main()
{
    freopen("airport.in","r",stdin);
    freopen("airport.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        ans=0;
        i=0;
        scanf("%d%d%d%lf%d",&c,&d,&e,&f,&g);
        for (h=1;h<=g;h++)
        {
            scanf("%d%d%lf",&p[h].second.first,&p[h].second.second,&p[h].first);
            i+=p[h].second.second-p[h].second.first;  
        }
        i=c-i;
        sort(p+1,p+g+1);
        if ((double)i/e <=f)
        {
           f-=(double)i/e;
           ans+=(double)i/e;                
        }
        else
        {
           ans+=f;
           sem=(double)i-(double)e*f;
           ans+=sem/(double)d;  
           f=0;  
        }
        for (h=1;h<=g;h++)
        {
            if (f>0)
            {
               sem=(double)p[h].second.second-(double)p[h].second.first;
               if (sem/(p[h].first+e) <=f)
               {
                  f-=sem/(p[h].first+e);
                  ans+=sem/(p[h].first+e);                       
               }
               else
               {
                   ans+=f;
                   sem=sem-(p[h].first+(double)e)*f;
                   ans+=sem/((double)d+p[h].first);
                   f=0;    
               }
            }
            else
            {
                ans+=((double)p[h].second.second-(double)p[h].second.first)/(p[h].first+(double)d);
            }
        }
        printf("Case #%d: %.9lf\n",b,ans);
    }
}
