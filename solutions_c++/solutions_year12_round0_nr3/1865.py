#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N=int(2e7)+5;
int f[N],v[12];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("Answer.txt","w",stdout);
    int t,a,b;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        cin>>a>>b;
        int ans=0;
        memset(f,0,N*sizeof f[0]);
        for(int n=a;n<=b;n++)
        {
            int x=n,p=0;
            while (x)
            {
                v[p++]=x%10;
                x/=10;
            }
            reverse(v,v+p);
            for(int j=1;j<p;j++)
            {
                if (!v[j])
                    continue;
                int m=0;
                for(int i=j;i<p;i++)
                    m=m*10+v[i];
                for(int i=0;i<j;i++)
                    m=m*10+v[i];
                if (m>n && m>=a && m<=b && f[m]!=n)
                {
                    f[m]=n;
                    ans++;
                }
            }
        }
        cout<<"Case #"<<q<<": "<<ans<<endl;
    }
    return 0;
}
