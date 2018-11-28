#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define TynKogep TOPCODER
#define bublic public:
#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define sz size()
#define ld long double
#define ll long long
#define istr istringstream

const ld eps=1e-9;
const ld PI=3.1415926535897932384626433832795;

int n,m;
string s[6000],z;

int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    cout.flags(ios::fixed);
    cout.precision(15);
    cin>>n>>n>>m;
    for(int i=0;i<n;i++)
    cin>>s[i];
    for(int i=0;i<m;i++)
    {
        cin>>z;
        int k=0,ans=0;
        bool can=true,now;
        for(int j=0;j<n;j++)
        {
            can=true;
            k=0;
            for(int t=0;t<z.sz;t++)
            {                
                if (k==s[j].sz) break;
                if (z[t]=='(')
                {
                    now=false;
                    t++;
                    while(z[t]!=')')
                    {
                        if (s[j][k]==z[t]) now=true;
                        t++;
                    }
                    k++;
                    if (!now) {can=false; break;}
                    continue;
                }
                if (z[t]==s[j][k])
                {
                    k++;
                    continue;
                }
                can=false;
                break;
            }
            if (can) ans++;
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }

    return 0;
}
