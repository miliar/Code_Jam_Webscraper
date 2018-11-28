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
#define clr(a); memset(a,0,sizeof(a));
#define pb push_back
#define sz size()  
#define ld long double
#define istr istringstream

int t,x,y,n,m,d[2000],dd[2000];
char a[12][12];

bool corr(int m1,int m2,int w)
{
    int r=1;
    for(int i=0;i<m;i++)
    {
        if (r&m1 && a[w][i]=='x') return false;
        if (r&m2 && a[w+1][i]=='x') return false;
        if (i) if (r&m2 && (r/2)&m1) return false;
        if (i<m-1) if (r&m2 && (r*2)&m1) return false;
        if (i) if (r&m1 && (r/2)&m1) return false;
        r*=2;
    }
    return true;
}

int ans(int m1)
{
    int e=0,r=1;
    for(int i=0;i<m;i++)
    {
        if (r&m1) e++;
        r*=2;
    }
    return e;
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cin>>t;
    for(int q=0;q<t;q++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        cin>>a[i][j];
        int loc=0;
        for(int mask=0;mask<(1<<m);mask++)
        {
            d[mask]=0;
            int r=1;
            bool can=true;
            for(int i=0;i<m;i++)
            {
                if (r&mask && a[n-1][i]=='x') can=false;
                if (i) if (r&mask && (r/2)&mask) {can=false;}
                if (r&mask && a[n-1][i]=='.') d[mask]++;
                r*=2;
            }
            if (!can) d[mask]=0;
            loc>?=d[mask];
        }
//        cout<<loc<<"!"<<endl;
        for(int w=n-2;w>=0;w--)
        {
            for(int m1=0;m1<(1<<m);m1++)
            {
                dd[m1]=0;
                for(int m2=0;m2<(1<<m);m2++)
                {
                    if (corr(m1,m2,w)) {dd[m1]=max(ans(m1)+d[m2],dd[m1]);}
                }
            }
            for(int m1=0;m1<(1<<m);m1++)
            d[m1]=dd[m1];
        }
        long long ans=0;
        for(int m1=0;m1<(1<<m);m1++)
        ans>?=d[m1];
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
    return 0;
}
