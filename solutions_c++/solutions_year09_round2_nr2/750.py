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
const double EPS=10e-9;
const long double EPSL=10e-12;

typedef long long ll;
typedef long double ld;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef list<int> LI;
typedef stack<int> SI;
typedef queue<int> QI;
typedef priority_queue<int> PQI;
typedef set<int> SETI;
typedef pair<int,int> PII;
typedef vector< PII > VII;
typedef pair<ll,ll> PLL;
template <class T>
inline int size(const T&a) { return a.size()-1; }
typedef vector<string> VS;
typedef vector<vector<string> > VVS;

inline ll ABS(ll x) { return x<0?-x:x; }
ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline ll nww(ll a,ll b) { return a*b/nwd(a,b); }
inline int CEIL(int a,int b) { return a%b?a/b+1:a/b; }
inline void delv(int i, vector<int>& v) { vector<int>::iterator it = v.begin();FOR(p,0,i-1) it++;v.erase(it);return; }
inline VS parse(string s) { string a;VS wyn;REP(i,(int)s.size()) if (s[i]!=' ') a+=s[i]; else if (!a.empty()) { wyn.PB(a); a=""; } if (!a.empty()) wyn.PB(a); return wyn; }
inline VS parse(string s,char ch) { string a;VS wyn;REP(i,(int)s.size()) if (s[i]!=ch) a+=s[i];else if (!a.empty()) { wyn.PB(a);a=""; } if (!a.empty()) wyn.PB(a); return wyn; }
inline VI parsei(string s) { string a="";VI wyn;REP(i,(int)s.size()) if (s[i]!=' ') a+=s[i];else if (!a.empty()) { wyn.PB(atoi(a.c_str()));a=""; } if (!a.empty()) wyn.PB(atoi(a.c_str()));return wyn; }
inline string lacz(VS t) { string s;REP(i,(int)t.size()) s+=t[i];return s; }
inline int toi(char ch) { return int(ch)-int('0'); }
inline void tolower(string &s) { REP(i,(int)s.size()) s[i]=tolower(s[i]); }
inline int chnum(char ch) { return int(ch)-int('a'); }
inline string tostr(int l) { char p[12];sprintf(p,"%d",l);return string(p); }
inline string tostr(unsigned int l) { char p[12];sprintf(p,"%u",l);return string(p); }
inline string tostr(float l) { char p[12];sprintf(p,"%f",l);return string(p); }
inline string tostr(long long l) { char p[23];sprintf(p,"%lld",l);return string(p); }
inline string tostr(unsigned long long l) { char p[23];sprintf(p,"%llu",l);return string(p); }
inline string tostr(double l) { char p[20];sprintf(p,"%lf",l);return string(p); }
inline string tostr(long double l) { char p[23];sprintf(p,"%Lf",l);return string(p); }
inline string sntostr(string s) { string w=s;string::iterator it;FOREACH(it,w) *it=(*it)+'a';return w; }
inline bool losujb(double p) { if ((double) rand()/RAND_MAX <=p) return true;else return false; }
inline int losuji(int a, int b) { return (rand()%(b+1-a))+a; }
inline int losuji(int b) { return (rand()%(b+1)); }
inline string stringify(int x){ostringstream o; o << x; return o.str();}
inline ll C(int n, int k){if(k<0||n<k)return 0;int q[n+1],i,j,a;ll ret=1;for(i=0;i<=n;i++)q[i]=0;for(i=2;i<=k;i++){a=i;for(j=2;a>1;j++)while(a%j==0){a/=j;q[j]--;}}for(i=n-k+1;i<=n;i++){a=i;for(j=2;a>1;j++)while(a%j==0){a/=j;q[j]++;}}for(i=2;i<=n;i++)while(q[i]--)ret*=i;return ret;}
inline ld Cr(ld n, int k){if(k<0)return 0;else if(k==0)return n;int i;ld ret=n;for(i=1;i<k;i++){ret*=(n-i);ret/=i;}ret/=k;return ret;}
inline ld power(ld a, ld b){if(b!=0) return powl(a,b); else return 1;}
inline int isZero(double x){if(x>=-EPS&&x<=EPS) return 1; else return 0;}
inline int isZero(long double x){if(x>=-EPSL&&x<=EPSL) return 1; else return 0;}



class Num{
public:
  int t[25];
  int n;
  Num(){n=0;}
  Num(string s){n=s.size(); for(int i=0; i<(int)s.size(); i++) t[i]=s[i]-'0';}
  Num &operator=(Num &a){n=a.n; for(int i=0; i<n; i++) t[i]=a.t[i];return *this;}
  bool operator==(Num &a){if(n!=a.n) return false; for(int i=0; i<n; i++) if(t[i]!=a.t[i]) return false; return true;}
  bool operator==(Num a){if(n!=a.n) return false; for(int i=0; i<n; i++) if(t[i]!=a.t[i]) return false; return true;}
  bool operator< (Num &a){if(n>a.n) return false; else if(n<a.n) return true; for(int i=0; i<n; i++) if(t[i]>a.t[i]) return false; else if(t[i]<a.t[i]) return true; return false;}
  int size(){return n;}
  string print(){string wyn=""; for(int i=0; i<n; i++) wyn+=stringify(t[i]); return wyn;}
};

int T;

inline void clarify(Num &p, int x){
  VI q;
  for(int i=x+1; i<p.size(); i++) q.PB(p.t[i]);
  sort(q.begin(), q.end());
  for(int i=x+1, j=0; i<p.size(); i++, j++) p.t[i]=q[j];
}

int main()
{
  scanf("%d",&T);
  string linia;
  getline(cin, linia);  
  for(int i=0; i<T; i++){
    getline(cin, linia);
    Num n(linia);
    Num m(string("99999999999999999999"));
    Num p;
    for(int j=n.size()-1; j>=0; j--){
      bool c=false;
      for(int k=j+1; k<n.size(); k++){
        if(n.t[j]<n.t[k]){
          p=n;
          p.t[k]=n.t[j];p.t[j]=n.t[k]; 
          c=true;
          clarify(p, j);
          if(p<m) m=p;
        }
      }
      if(c) break;
    }
    if(m==Num(string("99999999999999999999"))){
      m=n;
      clarify(m,-1);
      int w;
      for(w=0; w<m.size(); w++) if(m.t[w]!=0) break;
      if(w>0) swap(m.t[0],m.t[w]);
      for(int i=m.size()-1; i>0; i--) m.t[i+1]=m.t[i];
      m.t[1]=0;
      m.n++;
    }
    cout << "Case #"<<(i+1)<<": "<<m.print()<<"\n";
  }
	return 0;
}
