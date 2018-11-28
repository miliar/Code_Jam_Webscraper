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

string s;
int n,t,bst,k,a[10],b[10],u[10];

void tst()
{
    string z=s;
    for(int i=0;i<s.sz;i+=k)
    {
         for(int j=0;j<k;j++)
         z[j+i]=s[i+b[j]-1];
    }
    int ans=s.sz;
    for(int i=1;i<s.sz;i++)
    if (z[i]==z[i-1]) ans--;
    bst<?=ans;
}

void rec(int x)
{
    if (x==k) tst();
    for(int i=1;i<=k;i++)
    {
         if (!u[i])
         {
             u[i]=1;
             b[x]=i;
             rec(x+1);
             u[i]=0;
         }
    }
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout); 
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
         cin>>k;
         cin>>s;
         clr(u);
         bst=100000;
         rec(0);
         cout<<"Case #"<<ii+1<<": "<<bst<<endl;
    }
    return 0;
}
