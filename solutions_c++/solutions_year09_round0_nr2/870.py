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

const ld eps=1e-9;
const ld PI=3.1415926535897932384626433832795;

int u[120][120],a[120][120],n,m,t,k;
char c[12000];
vector <int> v[12000],w[12000];

void dfs(int x,int y,int k)
{
    if (!u[x][y]) u[x][y]=k;
    int q=100000;
    if (x-1>=0) q<?=a[x-1][y];
    if (x+1<n) q<?=a[x+1][y];    
    if (y-1>=0) q<?=a[x][y-1];    
    if (y+1<m) q<?=a[x][y+1]; 
    if (q>=a[x][y]) return;       
    if (x-1>=0 && a[x-1][y]==q)
    {
        dfs(x-1,y,k);
        u[x][y]=u[x-1][y];        
        return;
    }
    if (y-1>=0 && a[x][y-1]==q)
    {
        dfs(x,y-1,k);
        u[x][y]=u[x][y-1];        
        return;
    }    
    if (y+1<m && a[x][y+1]==q)
    {
        dfs(x,y+1,k);
        u[x][y]=u[x][y+1];        
        return;
    }        
    if (x+1<n && a[x+1][y]==q)
    {
        dfs(x+1,y,k);
        u[x][y]=u[x+1][y];
        return;
    }            
}

int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    cout.flags(ios::fixed);
    cout.precision(15);
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        cin>>a[i][j];
        for(int i=10000;i>=0;i--)
        {
            v[i].clear();
            w[i].clear();            
        }        
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            v[a[i][j]].pb(i);
            w[a[i][j]].pb(j);            
        }   
        clr(u);     
        k=1;        
        for(int i=10000;i>=0;i--)
        for(int j=0;j<v[i].sz;j++)
        {            
            int x=v[i][j],y=w[i][j];
            if (!u[x][y])
            {
                dfs(x,y,k);
                k++;
            }
        }
        clr(c);
        cout<<"Case #"<<T<<":"<<endl;
        char w='a';
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        if (c[u[i][j]]==0)
        {
            c[u[i][j]]=w;
            w++;
        }
        for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
        cout<<c[u[i][j]]<<" ";
        cout<<endl;}
    }
    return 0;
}
