/* spinning_blade */
/* produced by wegnahz */
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define skip(x) for(int i=1;i<=(x);++i) getchar();
#define xx first
#define yy second
#define MP make_pair
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define fill0(a) memset(a,0,sizeof(a));
typedef pair<int,int> ipair;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
const int maxn=503;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans,f[maxn][maxn],g[maxn][maxn];
int a[maxn][maxn];
char s[maxn];
bool check(int x,int y,int z){
    int i,j,k,t,s,p,q;
    for (p=q=0,t=1;t<=z;t++)
    {
        p+=t*(f[x-t][y+z]-f[x-t][y-z-1]);
        q+=t*(f[x+t][y+z]-f[x+t][y-z-1]);
    }
    p-=a[x-z][y-z]*z+a[x-z][y+z]*z;
    q-=a[x+z][y-z]*z+a[x+z][y+z]*z;
    if (p!=q) return 0;
    for (p=q=0,t=1;t<=z;t++)
    {
        p+=t*(g[x+z][y-t]-g[x-z-1][y-t]);
        q+=t*(g[x+z][y+t]-g[x-z-1][y+t]);
    }
    p-=a[x-z][y-z]*z+a[x+z][y-z]*z;
    q-=a[x-z][y+z]*z+a[x+z][y+z]*z;
    if (p!=q) return 0;
    return 1;
}
bool check1(int x,int y,int z){
    int i,j,k,t,s;
    double p,q;
    for (p=q=0,t=1;t<=z;t++)
    {
        p+=(t-0.5)*(f[x-t+1][y+z]-f[x-t+1][y-z]);
        q+=(t-0.5)*(f[x+t][y+z]-f[x+t][y-z]);
    }
    p-=a[x-z+1][y-z+1]*(z-0.5)+a[x-z+1][y+z]*(z-0.5);
    q-=a[x+z][y-z+1]*(z-0.5)+a[x+z][y+z]*(z-0.5);
    if (fabs(p-q)>eps) return 0;
    for (p=q=0,t=1;t<=z;t++)
    {
        p+=(t-0.5)*(g[x+z][y-t+1]-g[x-z][y-t+1]);
        q+=(t-0.5)*(g[x+z][y+t]-g[x-z][y+t]);
    }
    p-=a[x-z+1][y-z+1]*(z-0.5)+a[x+z][y-z+1]*(z-0.5);
    q-=a[x-z+1][y+z]*(z-0.5)+a[x+z][y+z]*(z-0.5);
    if (fabs(p-q)>eps) return 0;
    return 1;
}
int main(){
    int tt,ii,i,j,k,t;
    #ifndef ONLINE_JUDGE
    freopen("spinning_blade.in","r",stdin);
    freopen("spinning_blade.out","w",stdout);
    #endif
    cin>>tt;
    for (ii=1;ii<=tt;ii++)
    {
        cin>>m>>n>>k;
        fill0(a);
        for (i=1;i<=m;i++)
        {
            cin>>(s+1);
            for (j=1;j<=n;j++) a[i][j]=s[j]-'0'+k;
        }
        ans=0;
        fill0(f); fill0(g);
        for (i=1;i<=m;i++) for (j=1;j<=n;j++)
            f[i][j]=f[i][j-1]+a[i][j],g[i][j]=g[i-1][j]+a[i][j];
        for (i=1;i<=m;i++) for (j=1;j<=n;j++)
            for (k=min(min(m-i,i-1),min(n-j,j-1));k>ans;k--)
                if (check(i,j,k)) ans=k;
        ans=ans*2+1;
        if (ans<3) ans=2;
        for (i=1;i<=m;i++) for (j=1;j<=n;j++)
            for (k=min(min(i,m-i),min(j,n-j));k+k>ans;k--)
                if (check1(i,j,k)) ans=k+k;
        if (ans>=3) printf("Case #%d: %d\n",ii,ans);
        else printf("Case #%d: IMPOSSIBLE\n",ii);
    }
    return 0;
}
