/* bot_trust */
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
const int maxn=105;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans,a[maxn],pos[2];
bool b[maxn];
int main(){
    int tt,ii,i,j,k,t;
    char ch;
    #ifndef ONLINE_JUDGE
    freopen("bot_trust.in","r",stdin);
    freopen("bot_trust.out","w",stdout);
    #endif
    cin>>tt;
    for (ii=1;ii<=tt;ii++)
    {
        cin>>n;
        for (i=0;i<n;i++)
        {
            cin>>ch;
            cin>>a[i];
            b[i]=(ch=='B');
        }
        int ans=0;
        for (pos[0]=pos[1]=1,k=0;k<n;k++)
        {
            for (t=k+1;t<n && b[t]==b[k];t++);
            if (t<n)
                if (abs(pos[1-b[k]]-a[t])<=abs(pos[b[k]]-a[k])+1)
                    pos[1-b[k]]=a[t];
                else pos[1-b[k]]+=(pos[1-b[k]]-a[t]>0?-1:1)*(abs(pos[b[k]]-a[k])+1);
            ans+=abs(pos[b[k]]-a[k])+1;
            pos[b[k]]=a[k];
        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return 0;
}
