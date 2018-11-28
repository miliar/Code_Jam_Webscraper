/* Make_it_Smooth */
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
const int maxn=103;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans,a[maxn],f[maxn][260],q[1000000];
bool v[260];
int main(){
    int tt,ii,i,j,k,h,t;
    #ifndef ONLINE_JUDGE
    freopen("Make_it_Smooth.in","r",stdin);
    freopen("Make_it_Smooth.out","w",stdout);
    #endif
    scanf("%d",&tt);
    int D,I;
    for (ii=1;ii<=tt;ii++)
    {
        scanf("%d%d%d%d",&D,&I,&m,&n);
        for (i=1;i<=n;i++) scanf("%d",&a[i]);
        
        fill0(f);
        for (i=1;i<=n;i++)
        {
            for (j=0;j<256;j++)
            {
                f[i][j]=f[i-1][j]+D;
                for (k=max(0,j-m);k<=min(255,j+m);k++)
                {
                    checkmin(f[i][j],abs(a[i]-j)+f[i-1][k]);
                    //if (i==3 && j==169) cout<<abs(a[i]-j)<<' '<<f[i-1][k]<<' '<<k<<' '<<f[i][j]<<endl;
                }
            }
            for (j=0;j<256;j++) q[j]=j;
            memset(v,1,sizeof(v));
            h=0; t=255;
            for (;h<=t;h++)
            {
                j=q[h]; v[j]=0;
                for (k=max(0,j-m);k<=min(255,j+m);k++)
                    if (f[i][k]>f[i][j]+I)
                    {
                        f[i][k]=f[i][j]+I;
                        if (!v[k])
                        {
                            q[++t]=k;
                            v[k]=1;
                        }
                    }
            }
            //for (j=0;j<=255;j++) cout<<i<<' '<<j<<' '<<f[i][j]<<endl;
        }
        for (k=inf,j=0;j<256;j++) checkmin(k,f[n][j]);
        printf("Case #%d: %d\n",ii,k);
    }
    return 0;
}
