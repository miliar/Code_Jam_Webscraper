//MingW G++ 3.4.5
//Main < Input.txt > Output.txt
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


class BigInt {
public:

    BigInt():a(1,0) {}
    BigInt(long long v) {
        a.push_back((unsigned)v);
        if (v!=(int)v)a.push_back(unsigned(v>>32));
    }
    BigInt(const BigInt& rhs):a(rhs.a) {}

    BigInt operator-()const {
        BigInt t(*this);
        t.neg();
        return t;
    }

    BigInt operator+(const BigInt& rhs)const {
        BigInt res(*this);
        res.add(rhs);
        return res;
    }
    BigInt& operator+=(const BigInt& rhs) {
        add(rhs);
        return *this;
    }
    BigInt operator-(const BigInt& rhs)const {
        BigInt res(*this);
        res.sub(rhs);
        return res;
    }
    BigInt& operator-=(const BigInt& rhs) {
        sub(rhs);
        return *this;
    }
    BigInt operator*(const BigInt& rhs)const {
        BigInt res;
        mul(rhs,res);
        return res;
    }
    BigInt& operator*=(const BigInt& rhs) {
        BigInt res;
        mul(rhs,res);
        return *this=res;
    }
    BigInt operator/(const BigInt& rhs)const {
        BigInt res,rem;
        div(rhs,res,rem);
        return res;
    }
    BigInt& operator/=(const BigInt& rhs) {
        BigInt res,rem;
        div(rhs,res,rem);
        return *this=res;
    }
    BigInt operator%(const BigInt& rhs)const {
        BigInt res,rem;
        div(rhs,res,rem);
        return rem;
    }
    BigInt& operator%=(const BigInt& rhs) {
        BigInt res,rem;
        div(rhs,res,rem);
        return *this=rem;
    }

    bool operator<(const BigInt& rhs)const {
        return compare(rhs)<0;
    }
    bool operator<=(const BigInt& rhs)const {
        return compare(rhs)<=0;
    }
    bool operator>(const BigInt& rhs)const {
        return compare(rhs)>0;
    }
    bool operator>=(const BigInt& rhs)const {
        return compare(rhs)>=0;
    }
    bool operator==(const BigInt& rhs)const {
        return compare(rhs)==0;
    }
    bool operator!=(const BigInt& rhs)const {
        return compare(rhs)!=0;
    }

    bool iszero() {
        return size()==1 && a[0]==0;
    }
    int sign()const {
        return int(a.back())>>31;
    }
    unsigned size()const {
        return a.size();
    }
    unsigned operator[](unsigned i)const {
        return i<size() ? a[i]: (unsigned)sign();
    }

    static int leadingzeros(unsigned n) {
        if (!n)return 32;
        int ret=1;
        if (!(n>>16)) {
            ret+=16;
            n<<=16;
        }
        if (!(n>>24)) {
            ret+=8;
            n<<=8;
        }
        if (!(n>>28)) {
            ret+=4;
            n<<=4;
        }
        if (!(n>>30)) {
            ret+=2;
            n<<=2;
        }
        return int(ret-(n>>31));
    }

    static BigInt parse(string str) {
        bool sf=str[0]=='-';
        BigInt ret(atoi(str.substr(sf,(str.size()-sf)%9).c_str()));
        for (unsigned i=(str.size()-sf)%9+sf;i<str.size();i+=9) {
            ret.umul(1000000000);
            ret+=atoi(str.substr(i,9).c_str());
        }
        if (sf) ret.neg();
        return ret;
    }
    string toString() {
        ostringstream os;
        os<<*this;
        return os.str();
    }

    friend istream& operator >>(istream& is, BigInt& rhs) {
        string str;
        is>>str;
        rhs=parse(str);
        return is;
    }
    friend ostream& operator <<(ostream& os, BigInt rhs) {
        vector<unsigned> a;
        if (rhs.sign())	os<<'-',rhs.neg();
        do a.push_back(rhs.udiv(1000000000));
        while (!rhs.iszero());
        os<<a.back();
        for (int i=(int)a.size()-1;--i>=0;os.width(9),os.fill('0'),os<<a[i]);
        return os;
    }

private:
    typedef long long I64;
    typedef unsigned long long U64;

    vector<unsigned> a;

    void ensure(unsigned sz) {
        if (size()<sz)a.resize(sz,(unsigned)sign());
    }

    void trim() {
        while (int(a.back())==sign() &&
                size()>1 &&
                (int(*(a.rbegin()+1))>>31)==sign())
            a.pop_back();
    }

    void neg() {
        int sf=sign();
        I64 t=0;
        for (unsigned i=0;i<size();++i)
            a[i]=t=(t>>32)-a[i];
        if (sign()==sf)a.push_back(0);
        else trim();
    }

    void add(const BigInt& rhs) {
        ensure(rhs.size()+1);
        U64 t=0;
        unsigned i=0;
        for (;i<rhs.size();++i)
            a[i]=t=(t>>32)+a[i]+rhs.a[i];
        if (rhs.sign())
            for (;i<size();++i)
                a[i]=t=(t>>32)+a[i]+0xffffffff;
        else
            for (;(t>>=32)&&i<size();++i)
                a[i]=t+=a[i];
        trim();
    }

    void sub(const BigInt& rhs) {
        ensure(rhs.size()+1);
        I64 t=0;
        unsigned i=0;
        for (;i<rhs.size();++i)
            a[i]=t=(t>>32)+a[i]-rhs.a[i];
        if (rhs.sign())
            for (;i<size();++i)
                a[i]=t=(t>>32)+a[i]-0xffffffff;
        else
            for (;(t>>=32)&&i<size();++i)
                a[i]=t+=a[i];
        trim();
    }

    void mul(const BigInt& rhs, BigInt& res)const {
        if (sign())
            if (rhs.sign())(-*this).mul2(-rhs,res);
            else (-*this).mul2(rhs,res),res.neg();
        else
            if (rhs.sign())mul2(-rhs,res),res.neg();
            else mul2(rhs,res);
    }

    void mul2(const BigInt& q, BigInt& res)const {
        if (size()<2 || size()==2 && a[1]==0) {
            res=q;
            res.umul(a[0]);
            return;
        }
        if (q.size()<2 || q.size()==2 && q.a[1]==0) {
            res=*this;
            res.umul(q.a[0]);
            return;
        }
        res=0;
        res.ensure(size()+q.size());
        for (unsigned i=0;i<size();++i)if (a[i]) {
                U64 t=0;
                for (unsigned j=0,k=i;j<q.size();++j,++k,t>>=32)
                    res.a[k]=t+=U64(a[i])*q.a[j]+res.a[k];
                res.a[i+q.size()]=t;
            }
        res.trim();
    }

    void umul(unsigned v) {
        ensure(size()+1);
        U64 t=0;
        for (unsigned i=0;i<size();++i,t>>=32)
            a[i]=t+=U64(a[i])*v;
        trim();
    }

    unsigned udiv(unsigned v) {
        U64 t=0;
        for (int i=size();--i>=0;a[i]=t/v,t%=v)
            t=(t<<32)+a[i];
        trim();
        return t;
    }

    int compare(const BigInt& rhs)const {
        return sign()==rhs.sign()? ucompare(rhs) : sign()-rhs.sign();
    }

    int ucompare(const BigInt& rhs)const {
        if (size()!=rhs.size())
            return (size()<rhs.size())^bool(sign()) ? -1:1;
        for (int i=size();--i>=0;)
            if (a[i]!=rhs.a[i])
                return a[i]<rhs.a[i] ? -1 : 1;
        return 0;
    }

    unsigned getU32byoffset(unsigned offset)const {
        unsigned p=offset>>5,q=offset&31;
        if (!q)return a[p];
        return (a[p]>>q)+(a[p+1]<<(32-q));
    }
    U64 getU64byoffset(unsigned offset)const {
        unsigned p=offset>>5,q=offset&31;
        if (!q)return (U64((*this)[p+1])<<32)+(*this)[p];
        return ((*this)[p]>>q)+(U64((*this)[p+1])<<(32-q))+
               (U64((*this)[p+2])<<(64-q));
    }
    void addU32byoffset(unsigned offset,unsigned val) {
        unsigned p=offset>>5,q=offset&31;
        U64 t;
        a[p]=t=U64(val<<q)+a[p];
        if (q)++p,a[p]=t=(t>>32)+(val>>(32-q))+a[p];
        while (t>>=32)
            ++p,a[p]=t+=a[p];
    }

    //for div()
    //*this = *this - q * val << ofs (*this > 0 && q>0 && result>0)
    void usubmulshl(const BigInt& q,unsigned val,unsigned ofs) {
        U64 tm=0;
        I64 ts=0;
        unsigned pos=ofs>>5;
        for (unsigned i=0,ofsb=ofs&31,w0=0,w1;
                i<q.size()||w0||tm;
                ++i,++pos,w0=w1,tm>>=32) {
            w1=tm+=U64(q[i])*val;
            a[pos]=ts=(ts>>32)+a[pos]-
                      (w1<<ofsb)-(ofsb? (w0>>(32-ofsb)) : 0 );
        }
        while (ts>>=32)
            a[pos]=ts+=a[pos],++pos;
        trim();
    }

    void div(const BigInt& rhs,BigInt& res,BigInt& rem)const {
        if (sign())
            if (rhs.sign())(-*this).div2(-rhs,res,rem),rem.neg();
            else (-*this).div2(rhs,res,rem),res.neg(),rem.neg();
        else
            if (rhs.sign())div2(-rhs,res,rem),res.neg();
            else div2(rhs,res,rem);
    }

    void div2(const BigInt& q,BigInt& res,BigInt& rem)const {
        if (q.size()<2 || q.size()==2 && q[1]==0) {
            res=*this;
            rem=res.udiv(q.a[0]);
        } else {
            int cp=ucompare(q);
            switch (cp) {
            case -1:
                res=0;
                rem=*this;
                break;
            case 0:
                res=1;
                rem=0;
                break;
            case 1:
                res=0;
                res.ensure(size()-q.size()+1);
                rem=*this;
                int ofsq=(q.size()<<5)-leadingzeros(q.a.back())-32;
                U64 eq=U64(q.getU32byoffset(ofsq))+1;
                for (;;) {
                    int ofsp=(rem.size()<<5)-leadingzeros(rem.a.back())-64;
                    if (ofsp<ofsq) {
                        if (ofsp==ofsq-32 && rem>=q) {
                            rem.sub(q);
                            res.addU32byoffset(0,1);
                            break;
                        }
                        if (ofsp<ofsq-32)
                            break;
                        ofsp=ofsq;
                    }
                    U64 ep=U64(rem.getU64byoffset(ofsp));
                    if ((ep>>32)>=eq) ++ofsp,ep>>=1;
                    unsigned eofs=ofsp-ofsq;
                    unsigned eres=unsigned(ep/eq);
                    res.addU32byoffset(eofs,eres);
                    rem.usubmulshl(q,eres,eofs);
                }
                res.trim();
                break;
            }
        }
    }
};




struct T{
    BigInt p,q;
    T(LL p,LL q):p(p),q(q){}
    T(LL p):p(p),q(0){}
    T& operator*=(const T& rhs){
        BigInt p0=p*rhs.p+q*rhs.q*5;
        BigInt q0=p*rhs.q+q*rhs.p;
        p=p0;q=q0;
        return *this;
    }
};


void solve(){
    static int ct=0;
    printf("Case #%d: ",++ct);
    int n;
    scanf("%d",&n);


    T base(3,1);
    T ex=expn(base,n);

    //DBG(n);
    //DBG(ex.p.size());
    //DBG(ex.q.size());
    //DBG(ex.p);DBG(ex.q);

    //P+q*sqrt(5);
    BigInt p=ex.q*ex.q*5;
    BigInt a=ex.q*2-1;
    BigInt b=ex.q*3+1;
    while(a+1<b){
        BigInt mid=(a+b)/2;
        BigInt t=mid*mid;
        if(t>p)b=mid; else a=mid;
    }
    BigInt t=(a%1000+ex.p%1000)%1000;
    printf("%03d\n",t[0]);
    //printf("%lf",pow(3+sqrt(5),n));
}


int main(){
	int n;
	scanf("%d",&n);
	while(n--)solve();
	return 0;
}
