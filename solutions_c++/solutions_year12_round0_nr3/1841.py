#include <iostream>
using namespace std;
const int m[8]={1,10,100,1000,10000,100000,1000000,10000000};
int t,a,b;
bool flag[2000010];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    for (int tt=1;tt<=t;++tt)
    {
        int ans=0;
        cout<<"Case #"<<tt<<": ";
        cin>>a>>b;
        int tmp=a,p=0;
        while (tmp)
        {
              ++p;
              tmp/=10;
        }
        for (int i=a;i<=b;++i)
        {
            for (int j=1;j<p;++j)
            {
                int tmp=i%m[j]*m[p-j]+i/m[j];
                if (tmp>i && tmp<=b && !flag[tmp]) ++ans,flag[tmp]=1;
            }
            for (int j=1;j<p;++j)
            {
                int tmp=i%m[j]*m[p-j]+i/m[j];
                if (tmp<=b) flag[tmp]=0;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
