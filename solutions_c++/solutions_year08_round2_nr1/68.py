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

vector<long long> x,y;

int n;
LL A,B,C,D,M,x00,y00;

LL a[3][3];
LL kolko[9];


void generuj(){
  LL X=x00;
  LL Y=y00;
  x.PB(X);
  y.PB(Y);
  FR(i,1,n){
    X = (A * X + B) % M;
    Y = (C * Y + D) % M;
    x.PB(X);
    y.PB(Y);
 }
}

int dajx(int q){
   return q%3;
}
int dajy(int q){
   return q/3;
}

void solve(){
   scanf("%d %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x00,&y00,&M);
   x.clear(); y.clear();
   generuj();
   LL ret=0;
   CL(a);
   FOR(i,n){ a[x[i]%3][y[i]%3]++; }
   FOR(i,9){ kolko[i]=a[dajx(i)][dajy(i)]; }
   FOR(i,9) FOR(j,i+1) FOR(k,j+1){
       //ci sedia pocty..
       int xx=dajx(i)+dajx(j)+dajx(k);
       int yy=dajy(i)+dajy(j)+dajy(k);
       if(xx%3 || yy%3) continue;
       //kolko takych tam je ??
       if(i==j && j==k) { ret+=kolko[i]*(kolko[i]-1)*(kolko[i]-2)/6; continue; }
       if(i==j){  ret+= (kolko[i]*(kolko[i]-1)/2)*kolko[k]; continue; }
       if(j==k){ ret+= (kolko[i]*(kolko[j]*(kolko[j]-1)/2)); continue; }
       ret+=kolko[i]*kolko[j]*kolko[k];       
   }
   printf(" %lld\n",ret);
}

main(){
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d:",ppp);

     solve();
  }
}


