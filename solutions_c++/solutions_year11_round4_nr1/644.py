/* airport_walkways */
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
const int maxn=1003;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,x,s,r;
pair<int,int> a[maxn];
double ans,t;
int main(){
    int tt,ii=0,i,j,k,left;
    #ifndef ONLINE_JUDGE
    freopen("airport_walkways.in","r",stdin);
    freopen("airport_walkways.out","w",stdout);
    #endif
    cin>>tt;
    while (tt--)
    {
        cin>>x>>s>>r>>t>>n;
        ans=0; left=x; ++ii;
        for (i=1;i<=n;i++)
        {
            cin>>j>>k>>a[i].xx;
            a[i].yy=k-j;
            ans+=(double)a[i].yy/(a[i].xx+s);
            left-=a[i].yy;
        }
        ans+=(double)left/s;
        n++; a[n]=make_pair(0,left);
        sort(a+1,a+n+1);
        for (i=1;i<=n;i++)
        {
            double tmp=(double)a[i].yy/(a[i].xx+r);
            if (tmp>t)
            {
                ans-=((double)(a[i].xx+r)/(a[i].xx+s)-1)*t;
                break;
            }else
            {
                ans-=((double)(a[i].xx+r)/(a[i].xx+s)-1)*tmp;
                t-=tmp;
            }
        }
        printf("Case #%d: %.7f\n",ii,ans);
    }
        
    return 0;
}
