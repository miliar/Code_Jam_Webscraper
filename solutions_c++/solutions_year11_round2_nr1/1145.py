#include<iostream>
#include<complex>
#include<vector>
#include<string>

#include<cstdio>
#include<cctype>
#include<cstring>
#include<cstdlib>
#include<cmath>

#include<sstream>
#include<unistd.h>
#include<valarray>
#include<numeric>
#include<algorithm>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>

#include<fstream>
#include<time.h>
using namespace std;

#define NDEBUG
#include<assert.h>
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define MOD(A,B) (((A)%(B)+(B))%(B))
#define MP make_pair
#define FI first
#define SE second
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define RFOREACH(I,C) for(VAR(I,(C).rbegin());I!=(C).rend();I++)
#define ALL(X) (X).begin(),(X).end()
#define SRT(X) sort((X).begin(),(X).end())
#define CLC(ACT,V) (*({ACT;static __typeof(V) ret;ret=(V);&ret;}))
#define FIRST(P,A,B,COND) CLC(VAR(P,A);for(;P<(B);++P)if(COND)break,P)
#define LAST(P,A,B,COND) CLC(VAR(P,B);while((A)<=(--P))if(COND)break,P)
#define EXISTS(P,A,B,COND) (FIRST(P,A,B,COND)<(B))
#define FORALL(P,A,B,COND) (!(EXISTS(P,A,B,!(COND))))
#define EXISTSI(I,C,COND) CLC(VAR(I,(C).begin());for(;I!=(C).end();I++)if(COND)break,I)!=(C).end()
#define FORALLI(I,C,COND) (!(EXISTSI(I,C,!(COND))))
#define PB push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<vector<int> > VVI;
typedef list<int> LI;
typedef stack<int> SI;
typedef queue<int> QI;
typedef priority_queue<int> PQI;
typedef set<int> SETI;
typedef set<string> SETS;
typedef pair<int,int> PII;
typedef vector< PII > VII;
typedef pair<ll,ll> PLL;
typedef vector<string> VS;
typedef vector<vector<string> > VVS;

int TT=0,N=0;
VS s;
VD WP, OWP,OOWP;
VI aa;

inline void cWP(){
  REP(i,N){
    double w=0,a=0;
    REP(j,N) if(s[i][j]=='1'){w++;a++;} else if(s[i][j]=='0') a++;
    if(a==0) WP.PB(0); else WP.PB(w/a);
    aa.PB((int)a);
  }
  return;
}

inline void cOWP(){
  REP(i,N){
    double sum=0;
    int ns=0;
    REP(j,N) if(i!=j){
      if(s[j][i]=='1'){if(aa[j]>1) sum+=((WP[j]*aa[j]-1)/(aa[j]-1));ns++;}
      else if(s[j][i]=='0'){if(aa[j]>1) sum+=((WP[j]*aa[j])/(aa[j]-1));ns++;}
    }
    if(ns) sum/=ns; else sum=0;
    OWP.PB(sum);
  }
  return;
}

inline void cOOWP(){
  REP(i,N){
    double sum=0;
    int ns=0;
    REP(j,N) if(i!=j){
      if(s[j][i]!='.'){sum+=OWP[j];ns++;}
    }
    if(ns) sum/=ns; else sum=0;
    OOWP.PB(sum);
  }
  return;
}

int main(){
  scanf("%d",&TT);
  char buf[1000];
  FOR(t,1,TT){
    s.clear();
    scanf("%d",&N);
    REP(i,N){
      scanf("%s",buf);
      string str=buf;
      s.PB(str);
    }
    WP.clear(), OWP.clear(),OOWP.clear();
    cWP(); cOWP(); cOOWP();aa.clear();
    printf("Case #%d:\n",t);
    REP(i,N) printf("%.6f\n",WP[i]*0.25 + 0.50 * OWP[i] + 0.25 * OOWP[i]);
  }
  return 0;
}
