#pragma comment(linker, "/STACK:16777216")
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
#define re return
#define fi first
#define se second
#define mp make_pair
#define y0 y32479
#define y1 y95874

const ld PI=3.1415926535897932384626433832795;
const ld EPS=1e-9;

int n,t,a[1200];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        cin>>a[i];
        int ans=-1;
        for(int m=1;m<(1<<n)-1;m++)
        {
            int x=0,y=0;
            for(int i=0;i<n;i++)
            {
                if (m&(1<<i)) x^=a[i]; else y^=a[i];
            }
            if (x==y)
            {
                x=0;
                y=0;
                for(int i=0;i<n;i++)
                {
                    if (m&(1<<i)) x+=a[i]; else y+=a[i];
                }
                ans>?=max(x,y);
            }
        }
        cout<<"Case #"<<T+1<<": ";
        if (ans==-1) cout<<"NO"<<endl; else cout<<ans<<endl;
    }
    re 0;
}

