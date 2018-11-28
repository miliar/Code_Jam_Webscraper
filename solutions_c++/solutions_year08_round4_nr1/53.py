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

int g[12000],t[12000],e[12000],c[12000],m,v,n,d[12000][2];

void fndw(int x)
{
    if (e[x]) return;
    fndw(2*x+1);
    fndw(2*x+2);
    if (g[x]==1) t[x]=t[2*x+1]&t[2*x+2]; else t[x]=t[2*x+1]|t[2*x+2];
}

int rec(int x,int st)
{
    if (d[x][st]!=-1) return d[x][st];
    if (d[x][st]==-1) d[x][st]=1000000000;
    int ans=1000000000;
    if (st==1)
    {
         if (g[x]==1)
         {
              ans<?=rec(x*2+1,1)+rec(x*2+2,1);
         }
         if (g[x]==0)
         {
              ans<?=min(rec(x*2+1,1),rec(x*2+2,1));
         }
         if (g[x]==1 && c[x]==1)
         {
              ans<?=min(rec(x*2+1,1),rec(x*2+2,1))+1;
         }
         d[x][st]<?=ans;
    }
    if (st==0)
    {
         if (g[x]==1)
         {
              ans<?=min(rec(x*2+1,0),rec(x*2+2,0));
         }
         if (g[x]==0)
         {
              ans<?=rec(x*2+1,0)+rec(x*2+2,0);
         }
         if (g[x]==0 && c[x]==1)
         {
              ans<?=min(rec(x*2+1,0),rec(x*2+2,0))+1;
         }
         d[x][st]<?=ans;
    }
    if (d[x][st]>1000000000) d[x][st]=1000000000;
    return d[x][st];
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout); 
    cin>>n;
    for(int i=0;i<n;i++)
    {
         scanf("%d%d",&m,&v);
         clr(e);
         clr(c);
         clr(g);
         clr(t);
         for(int j=0;j<m;j++)
         {
             d[j][0]=-1;
             d[j][1]=-1;
         }
         for(int j=0;j<(m-1)/2;j++)
         {
              scanf("%d%d",&g[j],&c[j]);   
              t[j]=-1;
              e[j]=0;
         }
         for(int j=(m-1)/2;j<m;j++)
         {
              scanf("%d",&t[j]);   
              d[j][t[j]]=0;
              d[j][(t[j]+1)%2]=1000000000;
              e[j]=1;
         }
         fndw(0);
         rec(0,v);
         cout<<"Case #"<<i+1<<": ";
         if (d[0][v]<1000000000) cout<<d[0][v]<<endl; else cout<<"IMPOSSIBLE"<<endl;
//         cout<<d[0][v]<<endl;
//         cout<<v<<" "<<t[0]<<endl;
    }
    return 0;
}
