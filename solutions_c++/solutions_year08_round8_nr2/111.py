// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
///////////////////////////////////////////////////////////////////////////////////
// }}}


int n;
int z[300],k[300];
char nazov[300][50];
int b[10005];

map<string,int> cf;
int pf;
vector<pair<int,int> > e[300];

int bcnt(int mask){
    int ret=0; while(mask>0) { ret+=mask%2; mask/=2; } return ret;
}

int dajcislo(string x){
    if(cf.count(x)) return cf[x];
    pf++;
    cf[x]=pf-1;
    return pf-1;
}

int pokryje(vector<pair<int,int> > e){
    sort(ALL(e));
    if(e.SZ==0) return 1000;
    //if(e[0].first>1) return 1000;
    int x=1;
    int y=0;
    int ret=0;
    //FORSZ(j,e) printf("(%d %d)",e[j].first,e[j].second); PN;
    FORSZ(i,e){
//       printf("%d %d\n",x,y);
//       printf(" %d %d\n",e[i].first,e[i].second);
       //mozem si vyberat len z tych, kt. zacinaju do x
       if(e[i].first>x) {
          if(x<=y) { ret++; x=y+1; y=0; } else return 1000;
       }
       if(e[i].first>x) return 1000;
       if(e[i].first<=x) y=max(y,e[i].second);
//       printf("%d %d\n",x,y);
    }
    if(x!=10001){
       if(y!=10000) return 1000;
       ret++;
    }
//    printf("ret: %d\n",ret);
    return ret;
}

void solve(){
    scanf("%d\n",&n);
    char s[100];
    pf=0; cf.clear();
    int ret=1000;
    FOR(i,300) e[i].clear();
    FOR(i,n){
        scanf("%s %d %d\n",nazov[i],&z[i],&k[i]);
        //printf("%s\n",nazov[i]); printf("%d\n",dajcislo(nazov[i]));
        int f=dajcislo(nazov[i]);
        e[f].PB(MP(z[i],k[i]));
    }
//    printf("%d\n",pf);
//    FOR(i,pf){
//       FORSZ(j,e[i]) printf("(%d %d)",e[i][j].first,e[i][j].second); PN;
//    }
    FOR(i,pf) FOR(j,i+1) FOR(k,j+1){      //TODO
       vector<pair<int,int> > ee=e[i];
       FORSZ(ii,e[j]) ee.PB(e[j][ii]);
       FORSZ(ii,e[k]) ee.PB(e[k][ii]);
       ret=min(ret,pokryje(ee));
    }
    if(ret==1000) printf("IMPOSSIBLE\n"); else printf("%d\n",ret); 
   
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
