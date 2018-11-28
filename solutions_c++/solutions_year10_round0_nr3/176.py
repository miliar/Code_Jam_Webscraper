/* theme_park */
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
#include <queue>
#include <map>
#include <set>
#define skip(x) for(int i=1;i<=x;++i) getchar();
#define xx first
#define yy second
using namespace std;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
const int maxn=1002;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
int n,m,R,K,a[maxn<<1],b[maxn],v[maxn],c[maxn];
long long ans,s[maxn<<1];
int main(){
    int tt,ii,i,j,times;
    #ifndef ONLINE_JUDGE
    freopen("theme_park.in","r",stdin);
    freopen("theme_park.out","w",stdout);
    #endif
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        memset(v,0,sizeof(v));
        scanf("%d%d%d",&R,&K,&n);
        for (i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            s[i]=s[i-1]+a[i];
            a[i+n]=a[i];
        }
        for (i=n+1;i<=n+n;i++) s[i]=s[i-1]+a[i];
        if (s[n]<=K) {printf("Case #%d: %I64d\n",ii,s[n]*R); continue;}
        for (j=1,i=1;i<=n;i++)
        {
            for (;s[j]-s[i-1]<=K;j++);
            b[i]=j;
            //cout<<i<<' '<<b[i]<<endl;
        }
        for (times=0,j=1,ans=0;R;R--)
        {
            ans+=s[b[j]-1]-s[j-1];
            j=b[j]; if (j>n) j-=n,++times;
            if (v[j]) break;
            v[j]=R; c[j]=times;
        }
        if (R<=1) {printf("Case #%d: %I64d\n",ii,ans);continue;}
        //cout<<ans<<' '<<R<<' '<<v[j]<<' '<<times<<' '<<c[j]<<endl;
        ans+=(long long)((R-1)/(v[j]-R))*s[n]*(times-c[j]);
        for (R=(R-1)%(v[j]-R);R;R--)
        {
            ans+=s[b[j]-1]-s[j-1];
            j=b[j]; if (j>n) j-=n;
        }
        printf("Case #%d: %I64d\n",ii,ans);
    }
    return 0;
}
