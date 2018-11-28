#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("ouptut.txt","wr",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        long long l,t,n,c;
        cin>>l>>t>>n>>c;
        long long a[1000];
        for(int i=0;i<c;i++)
            cin>>a[i];
        int b[1000],q[1000];
        long long sum[1000];

        int k=n/c;
        int ost=n%c;
        for(int i=0;i<c;i++)
            b[i]=q[i]=k;
        for(int i=0;i<ost;i++)
            b[i]++,q[i]++;
        sum[0]=a[0];
        for(int i=0;i<c;i++)sum[i]=sum[i-1]+a[i];
        t/=2;
        for(int i=0;i<l;i++)
        {
            int nmax=-1;
            long long max=-1;
            for(int j=0;j<c;j++)
            if(b[j]>0)
            {
                long long s=0;
                s=sum[c-1]*(b[j]-1)+sum[j];
                if(s>t)
                {
                    long long cur;
                    if(s-a[j]<t)
                        cur=a[j]-(t-(s-a[j]));
                    else
                        cur=a[j];
                    if(cur>max)
                    {
                        max=cur;
                        nmax=j;
                    }
                }
            }
            if(nmax==-1)break;
            b[nmax]--;
        }
        t*=2;
        long long ans=0;
        for(int i=0;i<n;i++)
        {
            int j=i%c;
            int k=i/c;
            if(b[j]>k)
            {
                ans+=a[j]*2;
            }
            else
            {
                if(ans>=t)
                    ans+=a[j];
                else
                {

                    ans+=t-ans+a[j]-(t-ans)/2;
                }
            }
        }
        cout<<"Case #"<<test_case+1<<": "<<ans<<endl;
    }
    return 0;
}
