#include <iostream>
#include <cstdio>

using namespace std;

int w[200];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,q,x,r,n,s,b,e,cost,i,j,m;
    double res,ti;
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>x>>s>>r>>ti>>n;
        for (i=0;i<200;i++)
          w[i]=0;
        m=0;
        for (i=0;i<n;i++)
        {
            cin>>b>>e>>cost;
            w[cost]+=e-b;
            m+=e-b;
        }
        w[0]=x-m;
        res=0.;
        for (i=0;i<200;i++)
        {
            if (ti<=0.)
            {
                res+=(double)w[i]/(s+i);
            }
            else if ((r+i)*ti>=w[i])
            {
                ti=ti-(double)w[i]/(r+i);
                res+=(double)w[i]/(r+i);
            }
            else
            {
                res+=ti+(double)(w[i]-(r+i)*ti)/(s+i);
                ti=0;
            }
        }
        printf("Case #%d: %.7lf\n",q+1,res);
    }
    return 0;
}
