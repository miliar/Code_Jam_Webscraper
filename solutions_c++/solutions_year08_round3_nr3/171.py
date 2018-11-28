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

long long t,n,m,X,Y,Z,a[123],z[510000],ans,d[1234];

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout); 
    cin>>t;
    for(int q=0;q<t;q++)
    {
        cin>>n>>m>>X>>Y>>Z;
        ans=0;
        for(int i=0;i<m;i++)
        cin>>a[i];
        for(int i=0;i<n;i++)
        {
            z[i]=a[i%m];
            a[i%m]=(X*a[i%m]+Y*(i+1))%Z;
            while(a[i%m]<0) a[i%m]+=Z;
//            cout<<z[i]<<" ";
        }
        for(int i=0;i<n;i++)
        d[i]=1;
        for(int i=1;i<n;i++)
        for(int j=0;j<i;j++)
        if (z[j]<z[i]) {d[i]+=d[j]; d[i]%=1000000007;}
        ans=0;
        for(int i=0;i<n;i++)
        {
        ans+=d[i];
        ans%=1000000007;
        }
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
    return 0;
}
