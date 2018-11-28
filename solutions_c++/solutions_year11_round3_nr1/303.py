/* dashboard */
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
const int move[4][2]={{1,0},{1,1},{0,1},{0,0}};
const int maxn=55;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans;
string a[maxn];
int main(){
    int tt,ii,i,j,k,t,x,y;
    #ifndef ONLINE_JUDGE
    freopen("dashboard.in","r",stdin);
    freopen("dashboard.out","w",stdout);
    #endif
    cin>>tt;
    for (ii=1;ii<=tt;ii++)
    {
        cout<<"Case #"<<ii<<":\n";
        cin>>m>>n;
        for (i=0;i<m;i++) cin>>a[i];
        n=a[0].length();
        for (i=0;i<m;i++) for (j=0;j<n;j++)
            if (a[i][j]=='#')
            {
                for (k=0;k<4;k++)
                {
                    x=i+move[k][0]; y=j+move[k][1];
                    if (x<0 || y<0 || x>=m || y>=n) goto l0;
                    if (a[x][y]!='#') goto l0;
                    if (k & 1) a[x][y]='/'; else a[x][y]='\\';
                }
            }
        for (i=0;i<m;i++) cout<<a[i]<<endl;
        continue;
        l0:
        cout<<"Impossible\n";
    }
    return 0;
}
