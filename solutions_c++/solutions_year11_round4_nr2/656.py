#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <string.h>
#include <memory.h>
using namespace std;
template <class T> void OUT(T x, int n){  for(int i = 1; i <= n; ++i)  cout << x[i] << ' ';    cout << endl;    }
template <class T> void OUT(T x, int n, int m){  for(int i = 1; i <= n; ++i)    OUT(x[i], m);    cout << endl;    }
template <class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
#define  eps 1e-8
#define  LL long long
inline LL mod(LL x, LL y) { return x - floor(1.0 * x / y+eps) * y; }
#define  out(x) (cout << #x << " = " << x << endl)
#define  Set(a,b)  memset(a,b,sizeof(a))
#define  Sqr(x) ((x) * (x))
#define  pi  acos(-1.0)
const int maxn = 1005,INF = (1<<29);
int n,m;

double mat[maxn][maxn];

bool solve(int x,int y,int k){
    double mx=(x+x+k)*1.0/2.0,my=(y+y+k)*1.0/2;
    int i,j;
    double vx=0,vy=0;
    for(i=x;i<x+k;i++)
        for(j=y;j<y+k;j++){
            if(i==x&&j==y) continue;
            if(i==x+k-1&&j==y) continue;
            if(i==x&&j==y+k-1) continue;
            if(i==x+k-1&&j==y+k-1) continue;
            vx+=(i+0.5-mx)*mat[i][j];
            vy+=(j+0.5-my)*mat[i][j];
        }
    if(fabs(vx)<eps&&fabs(vy)<eps) return 1;
    else return 0;
}
char in[maxn][maxn];
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int i,j,k,t,T,x,y,sum,index;
    cin>>T;
    int d;
    for(t=1;t<=T;t++){
        scanf("%d%d%d",&n,&m,&d);
        for(i=0;i<n;i++) scanf("%s",in[i]);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++){
                mat[i][j]=in[i][j]-'0';
                mat[i][j]+=d;
            }
        int len,ans=0;
        for(i=0;i<=n;i++)
            for(j=0;j<=m;j++){
                for(k=3;k+i<=n&&k+j<=m;k++){
                    if(solve(i,j,k)){
//                         cout<<i<<" "<<j<<" "<<k<<endl;
                         ans=max(k,ans);
                    }
                }
            }
        if(ans==0) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
