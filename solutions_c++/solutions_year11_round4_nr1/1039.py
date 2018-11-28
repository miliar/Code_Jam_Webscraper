#include<iostream>
#include<cstdlib>
#include<algorithm>

using namespace std;

const int xx=1000000+50;

struct tt
{
    double l,w;
};

tt a[xx];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ts;
    cin>>ts;
    for (int ti=0; ti<ts; ti++)
    {
        double x,s,r,t;
        int n;
        cin>>x>>s>>r>>t>>n;
        for (int i=0; i<n; i++)
        {
            double l1,l2;
            cin>>l1>>l2>>a[i].w;
            a[i].l=l2-l1;
            x=x-a[i].l;
        }
        a[n].l=x;
        a[n].w=0;
        n++;
        for (int i=0; i<n-1; i++)
            for (int j=i+1; j<n; j++)
                if (a[i].w>a[j].w)
                {
                    tt k=a[i];
                    a[i]=a[j];
                    a[j]=k;
                }
        double ans=0;
        for (int i=0; i<n; i++)
        {
            if (a[i].l/(a[i].w+r)<=t)
            {
                t-=a[i].l/(a[i].w+r);
                ans+=a[i].l/(a[i].w+r);
            }
            else
            {
                ans+=t;
                a[i].l-=(a[i].w+r)*t;
                t=0;
                ans+=a[i].l/(a[i].w+s);
            }
        }
        cout<<"Case #"<<ti+1<<": ";
        printf("%.7lf\n",ans);    
    }
    return 0;
}
