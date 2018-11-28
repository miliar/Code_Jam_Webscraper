#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)

int main()
{
     freopen("inputA.txt","r",stdin);
     freopen("outputA.txt","w",stdout);

     long int x,n,cn=1,T,i;
     double s,r,b,e,w,sum,t;
     cin>>T;
     while(T--)
     {
         cin>>x>>s>>r>>t>>n;
         pair<double,double>p[1010];
         sum=0;
         FOR(i,n)
         {
             cin>>b>>e>>w;
             p[i].second=e-b;
             p[i].first=w;
             sum+=e-b;
         }
         p[i].first=0;
         p[i].second=x-sum;
         sort(p,p+n+1);
         double ans=0;
         FOR(i,n+1)
         {
            double sp=p[i].first;
            double dis=p[i].second;
            if(t>0)
            {
                double spd=sp+r;
                double tm=dis/spd;
                if(t>tm)
                {
                    t-=tm;
                    ans+=tm;
                }
                else
                {
                    dis-=t*spd;

                    ans+=t;
                    spd=sp+s;
                    tm=dis/spd;
                    ans+=tm;
                    t=0;
                }

            }
            else
            {
                  double spd=sp+s;
                  double tm=dis/spd;
                  ans+=tm;
            }
           // cout<<ans<<endl;
         }
        printf("Case #%ld: %.10lf\n",cn++,ans);
     }
    return 0;
}
