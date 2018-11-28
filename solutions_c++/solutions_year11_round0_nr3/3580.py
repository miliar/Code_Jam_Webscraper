#include <iostream>

using namespace std;

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int i,j,k,t,sum,minn,n,m;
    while(cin>>t)
    {
        for(i=1;i<=t;i++)
        {
            minn=INT_MAX;sum=0;
            cin>>k;
            cin>>n;
            sum+=n;
            if(minn>n)minn=n;

            for(j=1;j<k;j++)
            {
                scanf("%d",&m);
                if(minn>m)minn=m;
                sum+=m;
                n^=m;
            }
            if(n==0)printf("Case #%d: %d\n",i,sum-minn);
            else printf("Case #%d: NO\n",i);
        }
    }
    return 0;
}
