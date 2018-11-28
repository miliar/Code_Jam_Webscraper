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

int t,h,w,x,y,r,a[128][128];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cin>>t;
    for(int q=0;q<t;q++)
    {
        cin>>h>>w>>r;
        clr(a);
        a[1][1]=1;
        for(int i=0;i<r;i++)
        {
            cin>>x>>y;
            a[x][y]=-1;
        }
        for(int i=2;i<=h;i++)
        for(int j=2;j<=w;j++)
        {
            if (a[i][j]==-1) continue;
            a[i][j]=max(0,a[i-2][j-1])+max(a[i-1][j-2],0);
            a[i][j]%=10007;
        }
        cout<<"Case #"<<q+1<<": "<<a[h][w]<<endl;
    }
    return 0;
}
