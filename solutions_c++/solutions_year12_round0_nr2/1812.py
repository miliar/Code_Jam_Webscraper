#include <iostream>
using namespace std;
int t,n,p,s,a;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    for (int tt=1;tt<=t;++tt)
    {
        cout<<"Case #"<<tt<<": ";
        int ans=0;
        cin>>n>>s>>p;
        for (int i=0;i<n;++i)
        {
            cin>>a;
            if (p)
            {
               if (a>=p*3-2) ++ans;
               else if (p>1 && s && (a>=(p*3-4))) ++ans,--s;
            }
            else ++ans;
        }
        cout<<ans<<endl;
    }
    return 0;
}
        
