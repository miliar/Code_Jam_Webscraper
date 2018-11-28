#include <iostream>
#define MAX 1000010

using namespace std;

int a[MAX];

int main()
{
    int T,x,s,r,n,b,e,w;
    int i,j,k;
    double total,t,tt;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>x>>s>>r>>t>>n;
        for(j=1;j<=x;j++)
            a[j]=s;
        for(j=1;j<=n;j++)
        {
            cin>>b>>e>>w;
            for(k=b+1;k<=e;k++)
                a[k]+=w;
        }
        sort(a+1,a+x+1);
        total=0;
        for(j=1;j<=x;j++)
        {
            if(t>0.000000001)
            {
                tt=1/((double)(a[j]+r-s));
                if(t-tt>0.000000001)
                {
                    total+=tt;
                    t-=tt;
                }
                else
                {
                    total+=t+(1-t*((double)(a[j]+r-s)))/((double)(a[j]));
                    t=-1;
                }
            }
            else
                total+=1/((double)(a[j]));
        }
        printf("Case #%d: %.7lf\n",i,total);
    }
    return 0;
}
