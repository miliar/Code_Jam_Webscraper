#include<iostream>
using namespace std;
int main()
{
    long long t,r,k,n,zz=0;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        zz=0;
        cin>>r>>k>>n;
        long long g[n],d[n],f[n+1];
        for(int j=0;j<n;j++)
        {
            cin>>g[j];
        }
        memset(d,0,sizeof(d));
        int stat=0,rs=0,c=1;
        while(d[stat%n]==0 && c<=r)    
        {
            rs=0;
            d[stat%n]=c;
            int statc=stat;
            while(g[(statc)%n]+rs<=k)
            {
                rs+=g[(statc)%n];
                statc++;
                if((statc)%n==stat%n)
                {
                    break;
                }
            }
            zz+=rs;
            f[c]=rs;
            c++;
            stat=statc;
        }
        r-=(c-1);
        long long ns=0,q1=c-d[stat%n];
        for(int j=d[stat%n];j<c;j++)
        {
            ns+=f[j];
        }
        zz+=ns*(r/q1);
        q1=r%q1;
        for(int j=d[stat%n];j<d[stat%n]+q1;j++)
        {
            zz+=f[j];
        }
        cout<<"Case #"<<i<<": "<<zz<<endl;
    }
  return 0;
}
