/* Rotate */
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
const int maxn=53;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans;
char a[maxn][maxn],b[maxn][maxn];
bool f1,f2,ff;
int main(){
    int tt,ii,i,j,k,t;
    #ifndef ONLINE_JUDGE
    freopen("Rotate.in","r",stdin);
    freopen("Rotate.out","w",stdout);
    #endif
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        fill0(a); fill0(b);
        scanf("%d%d\n",&n,&m);
        for (i=1;i<=n;i++) gets(a[i]+1);
        for (i=1;i<=n;i++) for (j=1;j<=n;j++)
            b[i][j]=a[n-j+1][i];
        fill0(a);
        for (j=1;j<=n;j++)
        {
            for (k=n,i=n;i;i--) if (b[i][j]!='.')
                a[k--][j]=b[i][j];
        }
        f1=f2=0;
        //for (i=1;i<=n;i++,cout<<endl) for (j=1;j<=n;j++) putchar(b[i][j]);
        //for (i=1;i<=n;i++,cout<<endl) for (j=1;j<=n;j++) putchar(a[i][j]);
        for (i=1;i<=n;i++) for (j=1;j<=n;j++)
        {
            if (a[i][j]==0) continue;
            ff=0;
            if (ff==0 && j+m-1<=n)
            for (ff=1,k=j+1;k-j+1<=m;k++)
                if (a[i][j]!=a[i][k]) ff=0;
            if (ff==0 && i+m-1<=n)
            for (ff=1,k=i+1;k-i+1<=m;k++)
                if (a[k][j]!=a[i][j]) ff=0;
            if (ff==0 && j+m-1<=n && i+m-1<=n)
            for (ff=1,k=i+1,t=j+1;k-i+1<=m;k++,t++)
                if (a[i][j]!=a[k][t]) ff=0;
            if (ff==0 && j>=m && i+m-1<=n)
            for (ff=1,k=i+1,t=j-1;k-i+1<=m;k++,t--)
                if (a[i][j]!=a[k][t]) ff=0;
            if (ff==0) continue;
            //cout<<i<<' '<<j<<endl;
            if (a[i][j]=='R') f1=1;
            else f2=1;
        }
        printf("Case #%d: ",ii);
        if (f1) if (f2) puts("Both");
                else puts("Red");
        else if (f2) puts("Blue");
                else puts("Neither");
        
    }
    
    return 0;
}
