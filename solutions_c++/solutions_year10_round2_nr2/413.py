#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int c;
    int n,k,b,t;
    int x[55], v[55];
    int can[55];
    cin >> c;
    int i;
    for(int ca = 1; ca <= c; ++ca)
    {
        cin>>n>>k>>b>>t;
        
        for(i=0;i<n;++i)
        {
            cin>>x[i];
        }
        for(i=0;i<n;++i)
        {
            cin>>v[i];
        }
        int count = 0;
        int res = 0;
        for(i=n-1;i>=0;--i)
        {
            if(x[i]+t*v[i]>=b)
            {
                can[i]=1;
                ++count;
                if(count==k)break;
            }
            else
            {
                can[i]=0;
                res += k-count;
            }
        }
        
        cout << "Case #" << ca << ": ";
        if ( count != k ) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
        
    }
   return 0;
}
