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
int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout); 
    int t,p,k,l,a[2000];
    cin>>t;
    for(int q=0;q<t;q++)
    {
        cin>>p>>k>>l;
        for(int i=0;i<l;i++)
        cin>>a[i];
        sort(a,a+l);
        int z=0,w=1,ans=0;
        for(int i=l-1;i>=0;i--)
        {
              if (z==k) {w++; z=0;}
              z++;
              ans+=a[i]*w;
        }
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
    return 0;
}
