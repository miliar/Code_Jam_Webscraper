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

int t;
ll n,pd,pg;

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>n>>pd>>pg;
        bool ans=false;
        
        ll d=100/__gcd(100ll,pd);
        
        
        if (d<=n)
        {
            if ((pg==100 && pd==100) || (pg<100 && pg>1) || (pg==0 && pd==0)) ans=true;
        }
        
        cout<<"Case #"<<T+1<<": ";
        if (ans) puts("Possible"); else puts("Broken");
    }
    re 0;
}

