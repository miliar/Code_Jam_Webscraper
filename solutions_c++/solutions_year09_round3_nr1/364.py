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
#define FI first
#define SE second
#define SZ(x) ((int)x.size())
#define CLR(x) memset(x,0,sizeof(x))

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

//numerics
//transformations
template<class T> inline void delv(int i,vector<T> &v){typename vector<T>::iterator it=v.begin();it+=i;v.erase(it);}
inline VS parse(string s,char ch=' '){string a;VS wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(a);a="";} if(!a.empty()) wyn.PB(a);return wyn;}
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}
inline string lacz(VS t){string s;REP(i,(int)t.size()) s+=t[i];return s;}
inline int toi(char ch) {return int(ch)-int('0');}
inline void toLower(string &s){REP(i,(int)s.size()) s[i]=tolower(s[i]);}
inline void toUpper(string &s){REP(i,(int)s.size()) s[i]=toupper(s[i]);}
inline int chnum(char ch){return int(ch)-int('a');}
template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}
inline int toInt(string &s){int x=0;istringstream i(s);i>>x;return x;}
inline double toDouble(string &s){double x=0;istringstream i(s);i.precision(9);i>>x;return x;}
inline ll toLL(string &s){ll x=0;istringstream i(s);i>>x;return x;}
inline ld toLD(string &s){ld x=0;istringstream i(s);i.precision(12);i>>x;return x;}

map<char,unsigned int> s;

int T;
int main(){
  scanf("%d",&T);
  string linia;
  getline(cin,linia);
  for(int i=0; i<T; i++){
    string x;
    unsigned int n=1;
    getline(cin,x);
    s.clear();
    for(int j=0; j<SZ(x); j++){
      if(s.find(x[j])==s.end()){s[x[j]]=n; if(n==1) n=0; else if(n==0) n=2; else n++;}
    }
      unsigned long long ret=0;
      int q=s.size();
if(SZ(s)==1) q++;
    for(int j=0; j<SZ(x); j++){
      ret*=q;
      ret+=s[x[j]];
    }
    printf("Case #%d: %llu\n",i+1,ret);
  }
	return 0;
}
