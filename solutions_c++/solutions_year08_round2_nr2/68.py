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

bool b[1000005];
int sef[1000005];
bool bb[10000005];

VI p;
long long A,B,P;
set<LL> prc;

int najsef(int x){
   if(sef[x]==x) return x;
   int y=najsef(sef[x]);
   sef[x]=y;
   return y;
}

void skumaj(LL x){
   FORSZ(i,p){
      if(p[i]>x) break;      
      while(x%p[i]==0) { x/=p[i]; prc.insert(p[i]); }
   }
   if(x!=1) prc.insert(x);
}

void solve(){
  int ret=0;
  scanf("%lld %lld %lld",&A,&B,&P);
  for(LL x=A;x<=B;x++) {sef[x-A]=x-A; bb[x-A]=true; }
  prc.clear();
  

  FORSZ(i,p) prc.insert(p[i]);
  FORSZ(i,p){
     LL pp=p[i];
     for(LL z=(A/pp)*pp;z<=B;z+=pp){
        if(z-A>=0) bb[z-A]=0;
     }
  }
  for(LL x=A;x<=B;x++) if(bb[x-A]) prc.insert(x);

  FORIT(it,prc) if(*it>=P){
     LL pr=*it;
     if(pr>B) break;
     LL q=(A/pr)*pr;
     LL pred=0;
     while(q<=B){
        if(pred>0 && pred>=A ){
            int xx=najsef(q-A);
            int yy=najsef(pred-A);
            if(xx!=yy) { sef[xx]=yy; ret++; }
        }
        pred=q;
        q+=pr;        
     }
  }
  printf(" %d\n", B-A+1-ret );;
}

main(){
  CL(b);
  FR(i,2,1001) if(!b[i]){
     for(int j=i+i;j<=1000001;j+=i) b[j]=true;
  }
  FR(i,2,1000000) if(!b[i]) p.PB(i);

  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


