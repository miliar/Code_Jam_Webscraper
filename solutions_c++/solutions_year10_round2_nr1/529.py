#include<iostream>
//#include<fstream>
#include<sstream>
#include<unistd.h>
#include<complex>
#include<valarray>
#include<numeric>
#include<cstdio>
#include<cctype>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>
#include<time.h>
using namespace std;

#define NDEBUG
#include<assert.h>
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define RFOREACH(I,C) for(VAR(I,(C).rbegin());I!=(C).rend();I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define PF(I,V) V.insert(V.begin(),I)
#define EB(V) V.erase(V.rbegin());
#define EF(V) V.erase(V.begin());
#define MP make_pair
#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define SGN(X) (((X)>0)?1:(((X)<0)?-1:0))
#define FI first
#define SE second
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
#define LD(X) ((ld)(X))
#define LL(X) ((ll)(X))
#define BIT_CHECK(X,N) (X&(1<<N))
#define BIT_SET(X,N) (X|=(1<<N))
#define BIT_CLEAR(X,N) (X&=~(1<<N))
#define BIT_TOGGLE(X,N) (X^=(1<<N))

const long long INFTY=(long long)(1000000000)*(long long)(1000000000);
const long double EPS=10e-12;

typedef long long ll;
typedef long double ld;
typedef vector<int> VI;
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

inline VS parse(string s,char ch=' '){string a;VS wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(a);a="";} if(!a.empty()) wyn.PB(a);return wyn;}


int T, M, N;
SETS ex;
SETS nex;

int main(){
  cin >> T;
  for(int i=1; i<=T; i++){
    cin >> N >> M;
    ex.clear();
    nex.clear();
    for(int j=1; j<=N; j++){
      string s;
      cin >> s;
      ex.insert(s);
    }
    for(int j=1; j<=M; j++){
      string s;
      cin >> s;
      nex.insert(s);
    }
    int ret=0;
    FOREACH(I, nex){
      VS p=parse(*I,'/');
      string x="";
      FOREACH(J, p) {
        x+="/"+(*J);
        if(ex.find(x)==ex.end()){
          ex.insert(x);
          ret++;
        }
      }
    }
    printf("Case #%d: %d\n",i,ret);
  }
  return 0;
}
