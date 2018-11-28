//MingW G++ 3.4.5
#include<iostream>
#include<valarray>
#include<complex>
#include<bitset>
#include<queue>
#include<map>
#include<set>
using namespace std;

#include<ext/hash_set>
#include<ext/hash_map>
using namespace __gnu_cxx;

//template code
#define PB(v) push_back(v)
#define PF(v) push_front(v)
#define MP(a,b) make_pair(a,b)
#define SZ(c) ((int)(c).size())
#define BG(c) (c).begin()
#define ED(c) (c).end()
#define BE(c) BG(c),ED(c)
#define TYPE(v) __typeof(v)
#define FORE(i,c) for(TYPE(ED(c))i=BG(c);i!=ED(c);++i)
#define FOR(i,a,b) for(TYPE(b)i(a),_##i(b);i<_##i;++i)
#define REP(i,n) FOR(i,0,n)
#define FORR(i,a,b) for(TYPE(b)i(a),_##i(b);i<=_##i;++i)
#define REPR(i,n) FORR(i,0,n)
#define FORD(i,a,b) for(TYPE(b)i(b),_##i(a);--i>=_##i;)
#define REPD(i,n) for(TYPE(n)i(n);--i>=0;)
#define FORDR(i,a,b) for(TYPE(b)i(b),_##i(a);i>=_##i;--i)
#define REPDR(i,n) for(TYPE(n)i(n);i>=0;--i)
#define LAST(c) (*(c).rbegin())
#define iBIT(msk,p) ((msk)&1<<(p))
#define LBIT(msk,p) ((msk)&1LL<<(p))
#define vBIT(var,p) (((int*)&(var))[p>>5]&1<<(p&31))
#define BOUND(i,a,b) ((i)>=(a)&&(i)<(b))
#define SQR(x) ((x)*(x))
#define LET(var,val) TYPE(val)var=val;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef short I16;
typedef unsigned short U16;
typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<LL>VL;
typedef vector<VL>VVL;
typedef vector<string>VS;
typedef vector<VS>VVS;
typedef vector<double>VD;
typedef vector<VD>VVD;
typedef vector<LD> VLD;
typedef vector<VLD> VVLD;
typedef pair<int,int>pii;
typedef map<int,int>mii;
typedef pair<double,double>pdd;

#define ZPO {o<<'('<<SZ(v)<<"){ ";FORE(i,v)o<<'\"'<<*i<<"\" ";return o<<'}';}
#define ZPP {return o<<'('<<v.first<<','<<v.second<<')';}
#define ZPS(C) template<class T>ostream& operator<<(ostream& o,const C<T>& v)ZPO
#define ZPD(T,P) template<class K,class V>ostream& operator<<(ostream& o,const T<K,V>&v)P
ZPS(vector)ZPS(set)ZPS(deque)ZPS(hash_set)
ZPD(map,ZPO)ZPD(hash_map,ZPO)ZPD(pair,ZPP)

#define DBG(v) cerr<<#v<<"="<<(v)<<endl;
template<class I>void view(I b,I e,ostream& o=cerr){o<<"{ ";while(b!=e)o<<'\"'<<*b++<<"\" ";o<<"}\n";}

template<class T>string vtos(const T& v){ostringstream os;os<<v;return os.str();}
string ultos(ULL v,int r=10,int len=1){int i,c;char b[64];b[i=63]=0;for(;--len>=0||v;v/=r)b[--i]=(c=v%r)>9?c+55:c+48;return b+i;}

template<class T>T stov(const string& s){T v;istringstream(s)>>v;return v;}
int stoi(const string& s){return atoi(s.c_str());}
LL stol(const string& s){LL v=0;istringstream(s)>>v;return v;}
template<class T>vector<T> stoken(const string& s){istringstream is(s);vector<T> res;T v;while(is>>v)res.PB(v);return res;}

template<class T>inline T expn(T a,unsigned n) {T r=1;for(;;a*=a){if(n&1)r*=a;if(!(n>>=1))break;}return r;}
template<class T>pair<T,T> ext_euclid(T a,T b){
	if(!b)return pair<T,T>(1,0);
	pair<T,T> r=ext_euclid(b,a%b);return pair<T,T>(r.second,r.first-a/b*r.second);
}

template<class C>vector<pair<typename C::value_type,int> >run_length_encode(const C& c){
	vector<pair<typename C::value_type,int> >res;
	for(typename C::const_iterator i=BG(c),t;i!=ED(c);res.PB(MP(*t,i-t)))
	for(t=i;++i!=ED(c)&&*i==*t;);return res;
}

ULL permute(int n,int p){ULL r=p>=0;for(int i=n-p;i<n;r*=++i);return r;}

ULL combine(int n,int c){
	ULL res=1;
	for(int i=0,t=min(c,n-c);i<t;res*=n-i,res/=i+1,++i);
	return res;
}

template<class It,class T>inline bool next_combination(It b,It e,T t){
	It p=e;do if(p==b)return 0;while(*--p>--t);for(t=*p;p!=e;)*p++=++t;return 1;
}

template<class T>inline T gcd(T a,T b){while(b){T r=a%b;a=b;b=r;}return a;}

inline int rnd(){static int s=time(0);return s=s%44488*48271-s/44488*3399,s<0?s+=2147483647:s;}
inline int rnd(int n){return n>0?rnd()%n:0;}
inline int rnd(int lo,int hi){return lo+rnd(hi-lo);}

inline int bct(unsigned i){
	i-=(i>>1)&0x55555555,i=(i&0x33333333)+((i>>2)&0x33333333);return i=(i+(i>>4))&0x0f0f0f0f,i+=i>>8,i+=i>>16,i&0x3f;
}

template<class T>bool isprime(T n){
	if(n<25)return n>1&&((n&1)&&(n%3)||n<4);
	if(!(n&1)||n%3==0||n%5==0||n%7==0||n%11==0||n%13==0||n%17==0||n%19==0||n%23==0)return 0;
	for(unsigned i=29,ed=unsigned(sqrt(n));i<=ed;i+=2)if(n%i==0)return 0;return 1;
}

struct timer{double t;timer():t(clock()){}operator double()const{return (clock()-t)/CLOCKS_PER_SEC;}};

struct union_find{
	vector<int> e;union_find(int n):e(n,-1){}int operator()(int x){return e[x]<0?x:e[x]=this->operator()(e[x]);}
	void operator()(int x,int y){if((x=this->operator()(x))==(y=this->operator()(y)))return;if(e[x]<e[y])e[y]=x;else e[y]-=e[x]==e[y],e[x]=y;}
};

template<class T>struct indexer{
	map<T,int> m;int n;indexer(int base=0):n(base){}
	int operator()(const T& val){return m.count(val)?m[val]:m[val]=n++;}
};

bool isvowel(char c){return c=tolower(c),c=='a'||c=='e'||c=='i'||c=='o'||c=='u';}

string sreplace(string s,string a,string b){
	string r;int p=0,np;
	while(np=s.find(a,p),np>=0)r+=s.substr(p,np-p),r+=b,p=np+SZ(a);
	return r+=s.substr(p);
}
int scount(string s,string t){int p=0,np,r=0;while(np=s.find(t,p),np>=0)++r,p=np+SZ(t);return r;}
VS ssplit(string s,string t=" "){
	VS r;int p=0,np;
	while(np=s.find(t,p),np>=0){if(np!=p)r.PB(s.substr(p,np-p));p=np+SZ(t);}
	if(p<SZ(s))r.PB(s.substr(p));return r;
}
string strim(string s){
	int p=0,q=SZ(s);while(p<q&&isspace(s[p]))p++;
	if(p<q)while(isspace(s[--q]));return s.substr(p,q-p+1);
}
bool sstartswith(const string& s1,const string& s2){
	return equal(BE(s2),BG(s1));
}
bool sendswith(const string& s1,const string& s2){
	return equal(s2.rbegin(),s2.rend(),s1.rbegin());
}
//end of template code

double inR;

double getarea(double rc){
    double h=sqrt(SQR(inR)-SQR(rc)/4);
    double th=asin(rc/inR/2)*2;
    return SQR(inR)*th/2-h*rc/2;
}

double getarea(double x1,double y1,double x2,double y2){
    return (y2-y1)*(x2-x1)/2+getarea(hypot(y2-y1,x2-x1));
}

double check(double x1,double y1,double x2,double y2){
    if(SQR(x2)+SQR(y2)<=SQR(inR)){
        return (y2-y1)*(x2-x1);
    }
    double _x1=sqrt(SQR(inR)-SQR(y1));
    double _y1=sqrt(SQR(inR)-SQR(x1));

    double area=getarea(x1,y1,_x1,_y1);
    if(_x1>x2)area-=getarea(x2,y1,_x1,sqrt(SQR(inR)-SQR(x2)));
    if(_y1>y2)area-=getarea(x1,y2,sqrt(SQR(inR)-SQR(y2)),_y1);
    return area;
}


double calc(double r,double g){

    if(g<=0)return 1;

    //DBG(inR);
    //DBG(r);
    //DBG(g);
    double gd=r*2+g;
    double res=0;
    for(double xx=r;xx<inR;xx+=gd)
    for(double yy=r;SQR(xx)+SQR(yy)<SQR(inR);yy+=gd){
        res+=check(xx,yy,xx+g,yy+g);
    }
    return 1-res*4/M_PI;
}

void solve(){
    static int ct=0;
    printf("Case #%d: ",++ct);

    double f,t,R,r,g;
    scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
    f/=R;
    t/=R;
    r/=R;
    g/=R;
    R=1;
    inR=R-t-f;
    printf("%lf\n",calc(r+f,g-f*2));
}

int main(){
	int n;
	scanf("%d",&n);
	while(n--)solve();
	return 0;
}
