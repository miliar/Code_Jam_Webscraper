/* Number_Game */
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
const int maxn=1000003;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,a[maxn],b[maxn];
int main(){
    int tt,ii,i,j,k,t,a1,a2,b1,b2;
    #ifndef ONLINE_JUDGE
    freopen("Number_Game.in","r",stdin);
    freopen("Number_Game.out","w",stdout);
    #endif
    /*for (i=1;i<=100;i++)
    {
        t=-1;
        for (j=1;j<=100;j++)
        {
            f[i][j]=0;
            for (k=i-j;k>0;k-=j)
                if (f[k][j]==0) f[i][j]=1;
            for (k=j-i;k>0;k-=i)
                if (f[i][k]==0) f[i][j]=1;
            if (t==-1 && !f[i][j]) cout<<i<<' '<<j<<' ';
            if (!f[i][j])t=j;
        }
        cout<<t<<endl;
    }*/
    for (a[1]=b[1]=1,i=2;i<=1000000;i++)
    {
        a[i]=i+1-a[a[i-1]];
        if (a[i]!=a[i-1]) b[i]=b[i-1]+2;
        else b[i]=b[i-1]+1;
    }
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
        long long ans=(long long)(a2-a1+1)*(b2-b1+1);
        for (i=a1;i<=a2;i++)
        {
            //cout<<a[i]<<' '<<b[i]<<endl;
            ans-=max(0,min(b2,b[i])-max(b1,a[i])+1);
        }
        printf("Case #%d: %I64d\n",ii,ans);
    }
    
    return 0;
}
