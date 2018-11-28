/* space_emergency */
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
int num,n,m,ans;
int a[maxn];
int main(){
    int tt,ii,i,j,k,l,c;
    long long t,ans,tmp;
    #ifndef ONLINE_JUDGE
    freopen("space_emergency.in","r",stdin);
    freopen("space_emergency.out","w",stdout);
    #endif
    cin>>tt;
    for (ii=1;ii<=tt;ii++)
    {
        cout<<"Case #"<<ii<<": ";
        cin>>l>>t>>n>>c;
        for (i=1;i<=c;i++) cin>>a[i];
        for (i=c+1;i<=n;i++) a[i]=a[(i-1)%c+1];
        for (ans=0,i=1;i<=n;i++)
        {
            tmp=ans+a[i]+a[i];
            if (tmp>t)
            {
                ans=t;
                a[i]=(tmp-t)>>1;
                break;
            }else
            ans=tmp;
        }
        //show(a,n);
        //cout<<ans<<endl;
        if (i>n) cout<<ans<<endl;else
        {
            sort(a+i,a+n+1);
            for (j=n;j>=i && l;j--,l--) ans+=a[j];
            for (;j>=i;j--) ans+=a[j]+a[j];
            cout<<ans<<endl;
        }                
    }
    return 0;
}
