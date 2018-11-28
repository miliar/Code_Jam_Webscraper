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
typedef set<string> SETS;
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

class Bitset{
private:
  unsigned int *t;
  int n,m,r,rem;
public:
  ~Bitset(){free(t);}
  Bitset(){Bitset(256);}
  Bitset(int s){r=8*sizeof(unsigned int); m=s/r; if(m*r<s) m++; t=(unsigned int*)calloc(m, r); n=s; rem=m*r-n;}
  Bitset(Bitset &a){n=a.n; m=a.m; r=a.r; rem=a.rem; t=(unsigned int*)calloc(m, r); for(int i=0; i<m; i++) t[i]=a.t[i];}
  int operator[](int i){int a=i/r;int b=i-a*r;if((((int*)t)[a]&(1<<b))==0) return 0; else return 1;}
  void set(int i){int a=i/r;int b=i-a*r;t[a]|=(1<<b);}
  void unset(int i){int a=i/r;int b=i-a*r;t[a]&=(~(1<<b));} 
  Bitset &operator= (Bitset &a) {for(int i=0; i<m; i++) t[i]=a.t[i]; return *this;}
  Bitset operator| (Bitset &a){Bitset ret(*this); for(int i=0; i<m; i++) ret.t[i]|=a.t[i]; return ret;}
  Bitset operator& (Bitset &a){Bitset ret(*this); for(int i=0; i<m; i++) ret.t[i]&=a.t[i]; return ret;}
  Bitset operator^ (Bitset &a){Bitset ret(*this); for(int i=0; i<m; i++) ret.t[i]^=a.t[i]; return ret;}
  Bitset &inv(){for(int i=0; i<m; i++) t[i]=~t[i]; unsigned int mask=0;for(int i=0; i<rem; i++) {mask<<=1; mask|=1;} mask<<=(8*sizeof(int)-rem);t[m-1]&=(~mask);return *this;}
  Bitset &operator|= (Bitset &a){for(int i=0; i<m; i++) t[i]|=a.t[i]; return *this;}
  Bitset &operator&= (Bitset &a){for(int i=0; i<m; i++) t[i]&=a.t[i]; return *this;}
  Bitset &operator^= (Bitset &a){for(int i=0; i<m; i++) t[i]^=a.t[i]; return *this;}
  int first(){int ret=0, q=0; for(int i=0; i<m; i++) if(ret=__builtin_ffs(t[i])) break; else q++; return q*r+ret-1;}
  int size(){int ret=0; for(int i=0; i<m; i++) ret+=__builtin_popcount(t[i]);return ret;}
  int capacity(){return n;}
  int empty(){return this->size()==0?1:0;}
};

class Tree{
public:
  double pt;
  string name;
  Tree *left;
  Tree *right;
  //~Tree(){ if(left!=NULL) delete []left; if(right!=NULL) delete []right; }
  Tree(){pt=0;name="";left=NULL;right=NULL;}
  Tree(double p){pt=p;name="";left=NULL;right=NULL;}
  Tree(double p, string s){pt=p;name=s;left=NULL;right=NULL;}
  Tree(double p, string s, Tree &t1, Tree &t2){pt=p;name=s;left=new Tree; right=new Tree;*left=t1;*right=t2;}  
  Tree(double p, string s, Tree t1, Tree t2){pt=p;name=s;left=new Tree; right=new Tree;*left=t1;*right=t2;}  
  Tree &operator=(Tree &t){pt=t.pt; name=t.name; left=t.left; right=t.right; return *this;}
  double r(SETS &q){
    if(left==NULL) return pt;
    if(q.find(name)!=q.end()) return pt*(left->r(q)); else return pt*(right->r(q)); 
  }
void print(){
printf("%s %f\n", name.c_str(), pt);
printf("left:\n");
if(left!=NULL) left->print();
printf("right:\n");
if(right!=NULL) right->print();
printf("\n");
}
};

SETS q;

Tree buildT(string s){
  string a1="",a2="", a3="", a4="";
//printf("budowanie %s\n",s.c_str());
  int x=0,b=0;
  for(int i=1; i<(int)s.size()-1; i++){
    if(s[i]!=' ' && s[i]!='\n') switch(x){
      case 0: a1+=s[i]; x=1; break;
      case 1: a1+=s[i]; break;
      case 2: a2+=s[i]; x=3; break;
      case 3: a2+=s[i]; break;
      case 4: a3+=s[i]; x=5; b++; break;
      case 5: a3+=s[i]; if(s[i]=='(') b++; if(s[i]==')') b--;  break;
      case 6: a4+=s[i]; x=7; b++; break;
      case 7: a4+=s[i]; if(s[i]=='(') b++; if(s[i]==')') b--;  break;
      default: break;
    } else switch(x){
      case 0: break;
      case 2: break;
      case 4: break;
      case 6: break;
      case 8: break;
      case 1: x=2; break;
      case 3: x=4; break;
      case 5: if(b) a3+=s[i]; else x=6; break;
      case 7: if(b) a4+=s[i]; else x=8; break;
      default: break;
    }
  }
//printf(" jest a1=%s\n", a1.c_str());
//printf(" jest a2=%s\n", a2.c_str());
//printf(" jest a3=%s\n", a3.c_str());
//printf(" jest a4=%s\n", a4.c_str());
  if(a2=="") return Tree(atof(a1.c_str()));
  else return Tree(atof(a1.c_str()), a2, buildT(a3), buildT(a4));
}


int main()
{
  string linia;
  int N,L,A;
  scanf("%d",&N);
  getline(cin,linia);
  string opis;
  for(int i=0; i<N; i++){
    scanf("%d",&L);
    opis="";
    getline(cin,linia);    
    for(int j=0; j<L; j++) {getline(cin,linia); opis+=linia;}
    Tree t=buildT(opis);
//printf("**********************\n");
//t.print();
//printf("**********************\n");
    scanf("%d",&A);
    getline(cin,linia);        
    printf("Case #%d:\n",i+1);
    for(int j=0; j<A; j++){
      VS an;
      getline(cin,linia);
      an=parse(linia);
      q.clear();
      for(int k=2; k<(int)an.size(); k++) q.insert(an[k]);
      printf("%f\n",t.r(q));
    }
  } 
	return 0;
}
