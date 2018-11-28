#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<cstdlib>
#include<time.h>
#include<string.h>
#include<list>
#include<sstream>
#include<algorithm>
using namespace std;
#define ps system("pause")
#define maxn 10000
long long a[maxn],sum[maxn];
long long m[maxn],t[maxn];
long long n,k,r;
long long find(long long &start)
{
    long long tmp=k;
    long long total=0;
    while(1)
    {
        if(tmp>=a[start]) 
        {
            tmp-=a[start];
            total+=a[start];
        }
        else return total;
        start=(start+1)%n;
    }
    return start;
}

int main()
{
    long long T;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>T;
    for(long long cas=1;cas<=T;cas++)
    {
        cin>>r>>k>>n;
        long long sum=0;
        for(long long i=0;i<n;i++) 
        {
            cin>>a[i];
            sum+=a[i];
        }
        cout<<"Case #"<<cas<<": ";
        if(sum<=k) cout<<r*sum<<endl;
        else
        {
            for(long long i=0;i<n;i++)
            {
                m[i]=-1;
                t[i]=-1;              
                
            }
            long long start=0;
            long long cnt=1;
            m[0]=t[0]=0;
            long long ans=0;
            while(r--)
            {
                long long total=find(start);
                if(a[start]>k) break;
                if(m[start]==-1)
                {

                    ans+=total;                   
//                     cout<<ans<<" "<<start<<endl;
                    m[start]=ans;
                    t[start]=cnt++;
                }
                else
                {
                    
//                    cout<<"r  "<<r<<endl; 
                    ans+=total;
                    long long dif=ans-m[start];
  //                  cout<<"find cicle "<<start<<" "<<ans-m[start]<<" "<<cnt-t[start]<<endl;
                    long long dif_t=cnt-t[start];
                    cnt++;
                    long long z=r/dif_t;
                    ans+=z*dif;
                    r%=dif_t;
                    for(long long i=0;i<n;i++) m[i]=-1;
                }
                
            }
            cout<<ans<<endl;
        }
        
    }
    return 0;
}
