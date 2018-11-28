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

ld x[1200],y[1200],z[1200],p[1200];
int n,t;

ld getans(ld X,ld Y,ld Z)
{
     ld mx=0;
     for(int i=0;i<n;i++)
     mx>?=(abs(X-x[i])+abs(Y-y[i])+abs(Z-z[i]))/p[i];
     return mx;
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout); 
    cin>>t;
    cout.flags(ios::fixed);
cout.precision(9);
    for(int q=0;q<t;q++)
    {
         cin>>n;
         for(int i=0;i<n;i++)
         cin>>x[i]>>y[i]>>z[i]>>p[i];
         ld X=500000,Y=500000,Z=500000,st=500000;
         int xx,yy,zz;
         while(st>0.00000001)
         {
              ld now=getans(X,Y,Z);
              xx=0;
              yy=0;
              zz=0;
              for(int i=-1;i<2;i++)
              for(int j=-1;j<2;j++)
              for(int k=-1;k<2;k++)
              {
                   if (getans(X+st*i,Y+st*j,Z+st*k)<now)
                   {
                         now=getans(X+st*i,Y+st*j,Z+st*k);
                         xx=i;
                         yy=j;
                         zz=k;
                   }
              }
              X+=st*xx;
              Y+=st*yy;
              Z+=st*zz;
              st*=100;
              st/=111;
         }
         ld ans=getans(X,Y,Z);
         cout<<"Case #"<<q+1<<": ";
         cout<<ans<<endl;
    }
    return 0;
}
