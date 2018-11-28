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

int t,n,m;
string a[1200],b[1200];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);   
    cin>>t;
    for(int e=0;e<t;e++)
    {
        cin>>n;
        string s;
        getline(cin,s);
        for(int i=0;i<n;i++)
        {
            getline(cin,a[i]);
//            cout<<a[i]<<endl;
        }
        cin>>m;
//        cout<<endl;
        getline(cin,s);
        for(int i=0;i<m;i++)
        {
            getline(cin,b[i]);
//            cout<<b[i]<<endl;
        }
//        cout<<endl;
        int now=0,ans=0;
        while(now<m)
        {
             int bst=now,r=now;
             for(int i=0;i<n;i++)
             {
                     r=now;
                  while(true)
                  {
                       if (r==m) break;
                       if (b[r]==a[i]) break;
                       r++;
                  }
                  if (r>bst) bst=r;
             }
             now=bst;
             if (now==m) break;
             ans++;
        }
        cout<<"Case #"<<e+1<<": "<<ans<<endl;
    }
    return 0;
}
