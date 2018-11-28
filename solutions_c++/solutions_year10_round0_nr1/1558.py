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

#define bublic public
#define TynKogep TOPCODER 
#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define sz size()  
#define ld long double
#define ll long long
#define mp make_pair
#define istr istringstream

const ld PI=3.1415926535897932384626433832795;
const ld EPS=1e-9;

int t,x,y;

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        string ans="OFF";
        cin>>x>>y;
        if ((((1<<x)-1)&y)==(1<<x)-1) ans="ON";
        cout<<"Case #"<<T+1<<": "<<ans<<endl;
    }
    return 0;
}

