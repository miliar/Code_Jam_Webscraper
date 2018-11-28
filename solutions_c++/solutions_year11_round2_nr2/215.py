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

int t,n;
ld d,a[210],b[210];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(12);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        ld F=0,L=1e20;
        cin>>n>>d;
        for(int i=0;i<n;i++)
        {
            cin>>a[i]>>b[i];
            F=max(F,(b[i]*1.0-1)/2*d);
        }
        for(int q=0;q<300;q++)
        {
            ld C=(F+L)/2;
            ld lft=-1e20;
            bool can=true;
            for(int i=0;i<n;i++)
            {
                ld lp=max(lft+d,a[i]-C);
                ld rp=lp+(b[i]-1)*d;
                if (rp>a[i]+C)
                {
                    can=false;
                }
                lft=rp;
            }
            if (can) L=C; else F=C;
        }
        cout<<"Case #"<<T+1<<": "<<F<<endl;
    }
    re 0;
}

