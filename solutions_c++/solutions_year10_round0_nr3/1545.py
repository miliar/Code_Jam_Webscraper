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

ll a[1200],r[1200],z[1200],t,roll,k,n;

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>roll>>k>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            z[i]=-1;
            r[i]=0;
        }
        int now=0;
        ll ans=0;
        for(int i=0;i<roll;i++)
        {
            if (z[now]!=-1)
            {
                ans+=r[now];                
                now=z[now];
                continue;
            }
            int x=now,v=k;
            while(true)
            {
                if (x==n) x=0;
                if (x==now && v!=k) break;
                if (a[x]<=v)
                {
                    v-=a[x];
                    r[now]+=a[x];
                    x++;
                }
                else break;
            }
            z[now]=x;
            ans+=r[now];
            now=x;
        }
        cout<<"Case #"<<T+1<<": "<<ans<<endl;
    }
    return 0;
}

