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
char a[120][120];
ld ans[120],wp[120],owp[120],oowp[120];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(9);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
        cin>>a[i][j];
        clr(ans);
        
        for(int i=0;i<n;i++)
        {
            wp[i]=0;
            ld all=0;
            for(int j=0;j<n;j++)
            {
                if (a[i][j]=='1') wp[i]+=1;
                if (a[i][j]!='.') all+=1;
            }
            wp[i]/=all;
        }
       
        for(int i=0;i<n;i++)
        {
            ld all=0;
            owp[i]=0;
            for(int j=0;j<n;j++)
            if (a[i][j]!='.')
            {
                ld wp=0,allhere=0;
                for(int t=0;t<n;t++)
                if (t!=i)
                {
                    if (a[j][t]=='1') wp+=1;
                    if (a[j][t]!='.') allhere+=1;
                }
                wp/=allhere;
                owp[i]+=wp;
                all+=1;
            }
            owp[i]/=all;
        }
        
        for(int i=0;i<n;i++)
        {
            oowp[i]=0;
            ld all=0;
            for(int j=0;j<n;j++)
            if (a[i][j]!='.')
            {
                oowp[i]+=owp[j];
                all+=1;
            }
            oowp[i]/=all;
        }        
        
        cerr<<"Case #"<<T+1<<":"<<endl;
        cout<<"Case #"<<T+1<<":"<<endl;
        for(int i=0;i<n;i++)
        {
            ans[i]=wp[i]/4+owp[i]/2+oowp[i]/4;
            cout<<ans[i]<<endl;
        }
    }
    re 0;
}

