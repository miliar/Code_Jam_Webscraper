#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

bool cmp(pair<double,double> a, pair<double,double> b){
  return a.nd < b.nd;
}

void scase(int CID){
  double X,S,R,t;
  int N;
  scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
  vector<pair<double,double> > V;
  REP(i,N){
    double B,E,w;
    scanf("%lf%lf%lf",&B,&E,&w);    
    X -= E-B;
    V.push_back(mp(E-B, w+S));
  }
  V.push_back(mp(X,S));
  sort(V.begin(), V.end(), cmp);
  double result = 0;
  REP(i,V.size()){
    double t1 = min(V[i].st / (V[i].nd + (R-S)), t);
    t -= t1;
    result += t1;
    V[i].st -= t1 * (V[i].nd + (R-S));
    result += V[i].st / V[i].nd;
  }
  printf("Case #%d: %0.9lf\n",CID,result);
}

int main(){
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
