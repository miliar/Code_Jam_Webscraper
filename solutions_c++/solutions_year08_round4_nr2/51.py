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

ld dist(ld x,ld y,ld xx,ld yy)
{return sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy));}

ld trg(ld x,ld y,ld xx,ld yy)
{
    ld p=0;
    ld a=dist(0,0,x,y);
    ld b=dist(0,0,xx,yy);
    ld c=dist(x,y,xx,yy);
    p=a+b+c;
    p/=2;
    return sqrt(p*(p-a)*(p-b)*(p-c));
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout); 
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
         int A,n,m,I,J,X,Y;
         cin>>n>>m>>A;
         ld r=A;
         r/=2;
         bool can=false;
         for(int i=0;i<=n;i++)
         for(int j=0;j<=m;j++)
         {
              if (!can)
              for(int x=0;x<=n;x++)
              for(int y=0;y<=m;y++)
              if (!can)
              if (fabs(trg(i,j,x,y)-r)<0.00000001) {can=true; I=i; J=j; X=x; Y=y; break;}
         }
         cout<<"Case #"<<ii+1<<": ";
         if(can)
         {
             cout<<"0 0 "<<I<<" "<<J<<" "<<X<<" "<<Y<<endl;
         } else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
