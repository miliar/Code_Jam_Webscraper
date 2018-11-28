/* bacteria */
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
const int maxn=102;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans;
bool a[2][maxn][maxn];
int main(){
    int tt,ii,i,j,k,t;
    #ifndef ONLINE_JUDGE
    freopen("bacteria.in","r",stdin);
    freopen("bacteria.out","w",stdout);
    #endif
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        fill0(a);
        scanf("%d",&n);
        while (n--)
        {
            int p1,p2,q1,q2;
            scanf("%d%d%d%d",&p1,&q1,&p2,&q2);
            for (i=p1;i<=p2;i++) for (j=q1;j<=q2;j++)
                a[0][i][j]=1;
        }
        for (ans=0;;ans++)
        {
            bool flag=1;
            int u=ans & 1,v=1-u;
            for (i=1;i<=100;i++) for (j=1;j<=100;j++)
                if (a[u][i][j]) {flag=0;break;}
            if (flag) break;
            for (i=1;i<=100;i++) for (j=1;j<=100;j++)
                if (a[u][i-1][j] && a[u][i][j-1]) a[v][i][j]=1;else
                if (!a[u][i-1][j] && !a[u][i][j-1]) a[v][i][j]=0;else
                    a[v][i][j]=a[u][i][j];
        }
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
