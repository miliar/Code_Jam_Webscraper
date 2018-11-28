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

char C[600];
string s,w="$welcome to code jam";
ll d[600][600],t;

int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    cout.flags(ios::fixed);
    cout.precision(15);
    cin>>t;
    gets(C);
    for(int T=0;T<t;T++)
    {
        gets(C);
        s=C;
        s="$"+s;
        clr(d);        
        cout<<"Case #"<<T+1<<": ";
        for(int i=s.sz-1;i>=0;i--)
        {
            for(int j=w.sz-1;j>=0;j--)
            {
                if (s[i]==w[j])
                {
                    if (j==w.sz-1) d[i][j]++; 
                    else
                    {
                        for(int t=i;t<s.sz;t++)
                        if (s[t]==w[j+1]) {d[i][j]+=d[t][j+1]; d[i][j]%=1000000000;}
                    }
                }
            }
        }
/*        for(int i=0;i<s.sz;i++)
        {
            for(int j=0;j<w.sz;j++)
            cout<<d[i][j]<<" ";
            cout<<endl;
        }*/
        ll ans=d[0][0];
//        for(int i=0;i<s.sz;i++)
//        ans>?=d[i][0];
        ans%=10000;
        if (ans<1000) cout<<0;
        if (ans<100) cout<<0;
        if (ans<10) cout<<0;        
        printf("%d\n",ans);
//        cout<<ans<<endl;
//        cout<<d[0][0]<<endl;
    }
    return 0;
}
