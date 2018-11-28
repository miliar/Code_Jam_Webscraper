//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


int ar[109],res,n;

void recur(int par[],int cur)
{
    int x=-1,y=-1,a=0,b=0;
    for(int i=0;i<n;i++)
    {
        if(par[i]==0)
        {
            if(x==-1)x=ar[i];
            else x=x^ar[i];
            a+=ar[i];

        }
        else{
            if(y==-1)y=ar[i];
            else y=y^ar[i];
            b+=ar[i];
        }
    }

    if(x==y&&x!=-1)res=max(res,max(a,b));

    for(int i=cur;i<n;i++)
    {
        if(par[i]==0)
        {
            int br[109],c=i;
            for(int j=0;j<n;j++)br[j]=par[j];
            br[i]=1;
            recur(br,i);
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int kas,cas;
    cin>>kas;
    for(cas=1;cas<=kas;cas++)
    {
        int cell[109];
        cin>>n;
        for(int i=0;i<n;i++)cin>>ar[i];
        res=-1;
        for(int i=0;i<n;i++)cell[i]=0;
        recur(cell,0);
        printf("Case #%d: ",cas);
        if(res>-1)
        cout<<res<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
