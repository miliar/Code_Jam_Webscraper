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
#define PB push_back
#define PF(I,V) V.insert(V.begin(),I)
#define EB(V) V.erase(V.rbegin());
#define EF(V) V.erase(V.begin());
#define SGN(X) (((X)>0)?1:(((X)<0)?-1:0))
#define LD(X) ((ld)(X))
#define LL(X) ((ll)(X))
#define BIT_CHECK(X,N) (X&(1<<N))
#define BIT_SET(X,N) (X|=(1<<N))
#define BIT_CLEAR(X,N) (X&=~(1<<N))
#define BIT_TOGGLE(X,N) (X^=(1<<N))
#define BIT_LOWEST(X) (__builtin_ffsll((unsigned long long)X))
#define BIT_COUNT(X) (__builtin_popcountll((unsigned long long)X))
template<class T> inline void wypisz(const T& x){FOREACH(I,x)cout<<*I<<" ";cout<<endl;}

const long long INFTY=(long long)(2147483647)*(long long)(2147483647)*(long long)2;
const int INF=0x7f7f7f7f;
const long double EPS=10e-12;

typedef long long ll;
typedef unsigned long long ull;
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

template<class T> inline T ABS(T x){return x<0?-x:x;}
inline VS parse(string s,char ch=' '){string a;VS wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(a);a="";} if(!a.empty()) wyn.PB(a);return wyn;}
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}
inline string lacz(VS t, string c=""){string s;REP(i,(int)t.size()-1)s+=(t[i]+c);s+=t[(int)t.size()-1];return s;}
template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}
inline int toInt(string &s){int x=0;istringstream i(s);i>>x;return x;}
inline double toDouble(string &s){double x=0;istringstream i(s);i.precision(9);i>>x;return x;}
inline ll toLL(string &s){ll x=0;istringstream i(s);i>>x;return x;}
inline ld toLD(string &s){ld x=0;istringstream i(s);i.precision(12);i>>x;return x;}

inline int getI(){int pom=0; scanf("%d",&pom); return pom;}
char buf[1000000]; inline char * getS(){scanf("%s",buf);return buf;}
int TT=0;
int R=0,C=0;
//char x[60][60];
VS x;

int main(){
  string s;
  getline(cin,s);
  TT=toInt(s);
  FOR(ttt,1,TT){
    x.clear();
      getline(cin,s);
      VI pom=parsei(s);
  R=pom[0];
  C=pom[1];
//    REP(i,R) scanf("%s",x[i]);
  REP(i,R){
      getline(cin,s);
      x.PB(s);
  }
    FOR(i,0,R-2) FOR(j,0,C-2) if(x[i][j]=='#' && x[i+1][j]=='#' && x[i][j+1]=='#' && x[i+1][j+1]=='#'){
      x[i][j]='/';
      x[i+1][j]='\\';
      x[i+1][j+1]='/';
      x[i][j+1]='\\';
    }
    int ok=1;
    REP(i,R) REP(j,C) if(x[i][j]=='#') ok=0;
    cout<<"Case #"<<ttt<<":\n";
    if(!ok) cout<<"Impossible\n"; else{
      REP(i,R) cout<<x[i]<<"\n";
    }
  }
  return 0;
}
