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

string zz[1200],yy[1200],s;
int z,y,t;

string trans(string q,char A,char B)
{
    for(int i=0;i<z;i++)
    {
        if (zz[i][0]==A && zz[i][1]==B)
        {
            q=q.substr(0,q.sz-1);
            q+=zz[i][2];
            return q;
        }
        if (zz[i][0]==B && zz[i][1]==A)
        {
            q=q.substr(0,q.sz-1);
            q+=zz[i][2];
            return q;
        }        
    }
    q+=B;
    return q;
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>z;
        for(int i=0;i<z;i++)
        {
            cin>>zz[i];
        }
        cin>>y;
        for(int i=0;i<y;i++)
        {
            cin>>yy[i];
        }
        cin>>s>>s;
        string q="";
        for(int i=0;i<s.sz;i++)
        {
            if (q.sz) q=trans(q,q[q.sz-1],s[i]); else q+=s[i];
            for(int j=0;j<(int)q.sz-1;j++)
            {
                for(int r=0;r<y;r++)
                {
                    if (yy[r][0]==q[j] && yy[r][1]==q[q.sz-1])
                    {
                        q="";
                        break;
                    }
                    if (yy[r][1]==q[j] && yy[r][0]==q[q.sz-1])
                    {
                        q="";
                        break;
                    }                    
                }
            }
        }
        cout<<"Case #"<<T+1<<": [";
        for(int i=0;i<(int)q.sz-1;i++)
        cout<<q[i]<<", ";
        if (q.sz)
        cout<<q[q.sz-1];
        cout<<"]"<<endl;
    }
    re 0;
}

