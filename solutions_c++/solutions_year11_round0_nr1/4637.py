#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstring>

using namespace std;

#define DEBUG

#ifdef DEBUG
  #define dbg(x) cerr<<#x<<" = "<<x;
    #define de() cerr<<endl;
#else 
  #define dbg(x)    
  #define de()
#endif
#define FileName "out.deb"
#define foreach(it,v) for(typeof (v).begin() it=(v).begin();it!=(v).end();it++)
#define forl(p,s,n,u) for((p)=(s);(p)<(n);(p)+=(u))
#define fore(p,s,n,u) for((p)=(s);(p)<=(n);(p)+=(u))        
#define loop(i,s,n) for((i)=(s);(i)<(n);(i)++)
#define pool(i,s,n) for((i)=(s);(i)>(n);(i)--)
#define fs first
#define ins insert
#define sc second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define all(v) (v).begin(),(v).end()
typedef long double ld;

const ld EPS=1e-9;
const ld PI=3.1415926535897932384626433832795;

const int INF=1000*1000*1000;
const int NMAX=1000*1000;
long ans,i,j,k,l,n,m,x,y,w,q,c,g,h;
struct qwrep{
  long x,y;
} b[1000],o[1000];
 
long a[1000],f[10];
long long  mx,mn;
string s;
int main()
{
  #ifdef DEBUG
    freopen(FileName,"w",stderr);
  #endif
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&n);
  for(i=1;i<=n;i++){
    scanf("%d ",&m);
    b[0].x=0;
    o[0].x=0;
    memset(b,0,sizeof(b));
    memset(o,0,sizeof(o));
    w=0;
    g=1;h=1;
    for(j=1;j<=m;j++){
      scanf("%c %d ",&x,&y);
      if(x=='O'){
        o[++o[0].x].x=y;
        o[o[0].x].y=j;
      }else{
          b[++b[0].x].x=y;
          b[b[0].x].y=j;
      
      }
    }
    k=1;
    l=1;
    w=1;
    bool ok=1;
    for(j=1;j<=100000;j++){
      ok=1;
      if(o[l].x==g){
        if(o[l].y==w){
          w++;
          l++;
          ok=0;
        }
      }else{
        if(g>o[l].x)g--;
        else g++;
      }
      if(b[k].x==h){
        if(b[k].y==w&&ok){
          w++;
          k++;
        }
      }else{
        if(h>b[k].x)h--;
        else h++;
      }
      if(k>b[0].x&&l>o[0].x)break;
    } 
    printf("Case #%d: %d\n",i,j);
  }      
  
  return 0;
}






































