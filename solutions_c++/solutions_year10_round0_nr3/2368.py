#include<iostream>
using namespace std;
int main()
{
    int t,r,k,n,ts,i,j,sum,s,pri;
    int g[1010],f[1010],next[1010];
    cin>>t;
    bool g0;
    for(ts=0;ts<t;ts++)
    {
        cin>>r>>k>>n;
        sum=0;
        pri=0;
        for(i=0;i<n;i++)
        {
            cin>>g[i];
            sum+=g[i];
        }
        cout<<"Case #"<<ts+1<<": ";
        if(k>sum)
        {
            cout<<sum*r<<endl;
            continue;
        }
        for(i=0;i<n;i++)
        {
            if(g[i]<=k)
            {
                for(j=(i+1)%n,s=g[i];s+g[j]<=k && j!=i;j=(j+1)%n) s+=g[j];
                f[i]=s;
                next[i]=j;
                //cout<<f[i]<<' '<<next[i]<<endl;
            }else
            {
                f[i]=0;
                next[i]=i;
            }
        }
        for(i=0,j=0;i<r;i++)
        {
            pri+=f[j];j=next[j];
            /*if(j==0)
            {
                pri*=r/(i+1);
                r=r%(i+1);
                i=-1;
            }*/
        }
        cout<<pri<<endl;
    }
}
