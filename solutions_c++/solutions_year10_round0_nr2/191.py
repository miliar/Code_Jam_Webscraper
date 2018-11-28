#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
typedef int LL;
using namespace std;

struct Natural {
  static const int BASE = 10000;
  static const int BD = 4;
  
  LL *cyf;
  int len, al;
  
  Natural(int x=0, int y=2) {
    len=1; al=y; cyf=new LL[al];
    REP(i,al) cyf[i]=0;
    cyf[0]=x; if(x>=BASE) przen(1);
  }
  
  Natural(const Natural &x) {
    len=x.len; al=x.al; cyf=new LL[al];
    REP(i,al) cyf[i]=x.cyf[i];
  }
  
  Natural& operator = (const Natural &x) {
    resize(x.len);
    REP(i,x.len) cyf[i]=x.cyf[i];
    FORD(i,len-1,x.len) cyf[i]=0;
    len=x.len; return *this;
  }
  
  
  Natural& operator = (int x) {
    REP(i,len) cyf[i]=0; len=1;
    cyf[0]=x; if(x>=BASE) przen(1);
    return *this;
  }
  
  ~Natural() { delete[] cyf; }
  void dropZeros() { while(len>1 && !cyf[len-1]) --len; }
  
  void przen(int s) {
    int i=0;
    while(i<s || cyf[i]<0 || cyf[i]>=BASE) {
      resize(i+2);
      if(cyf[i]<0) {
        LL j=(-cyf[i]-1)/BASE+1;
        cyf[i]+=j*BASE;
        cyf[i+1]-=j;
      } else if(cyf[i]>=BASE) {
        LL j=cyf[i]/BASE;
        cyf[i]-=j*BASE;
        cyf[i+1]+=j;
      } ++i;
    } len=max(len,i+1);
    dropZeros();
  }
  
  void resize(int s) {
    if(s>al) { s=max(s,2*al);
      LL *t=new LL[s];
      REP(i,s) t[i]=i>=al?0:cyf[i];
      delete[] cyf; cyf=t; al=s;
    }
  }
  
  bool operator < (const Natural &x) const {
    if(len!=x.len) return len<x.len;
    int i=len-1; while(i && cyf[i]==x.cyf[i]) --i;
    return cyf[i]<x.cyf[i];
  }
  
  bool operator == (const Natural &x) const {
    if(len!=x.len) return false;
    REP(i,len) if(cyf[i]!=x.cyf[i]) return false;
    return true;
  }
  
  bool operator <= (const Natural &x) const { return !(x<*this); }
  bool operator > (const Natural &x) const { return x<*this; }
  bool operator != (const Natural &x) const { return !(x==*this); }
  bool operator >= (const Natural &x) const { return !(*this<x); }
  
  Natural& operator += (const Natural &x) {
    resize(x.len);
    REP(i,x.len) cyf[i]+=x.cyf[i];
    przen(x.len); return *this;
  }
  
  Natural& operator += (int x) {
    cyf[0]+=x; if(cyf[0]>=BASE) przen(1);
    return *this;
  }
  
  Natural operator + (const Natural &x) const { Natural y=*this; y+=x; return y; }
  
  Natural& operator -= (const Natural &x) {
    REP(i,x.len) cyf[i]-=x.cyf[i];
    przen(x.len); return *this;
  }
  
  Natural& operator -= (int x) {
    cyf[0]-=x; if(cyf[0]<0) przen(1);
    return *this;
  }
  
  Natural operator - (const Natural &x) const { Natural y=*this; y-=x; return y; }  
  
  Natural& operator *= (const Natural &x) {
    Natural c(0,len+x.len);
    REP(i,x.len) {
      REP(j,len) c.cyf[i+j]+=x.cyf[i]*cyf[j];
      c.przen(len+i);
    } *this=c; return *this;
  }
  
  Natural& operator *= (int x) {
    REP(i,len) cyf[i]*=x;
    przen(len); return *this;
  }
  
  Natural operator * (const Natural &x) const { Natural y=*this; y*=x; return y; }
  
  Natural& operator <<= (int x) {
    if(len==1 && !cyf[0]) return *this;
    resize(len+x);
    FORD(i,len-1,0) cyf[x+i]=cyf[i];
    REP(i,x) cyf[i]=0;
    len += x; return *this;
  }
  
  Natural& operator >>= (int x) {
    x=min(x,len); int n=len-x;
    REP(i,n) cyf[i]=cyf[i+x];
    REP(i,x) cyf[n+i]=0;
    len=n; if(!len) len=1;
    return *this;
  }
  
  Natural operator << (int x) const { Natural y=*this; y<<=x; return y; }
  Natural operator >> (int x) const { Natural y=*this; y>>=x; return y; }
  
  Natural& operator /= (const Natural &x) {
    int n=max(len-x.len+1, 1);
    Natural d(0,n), prod;
    FORD(i,n-1,0) {
      int pc=0,kn=BASE-1;
      while(pc<kn) { int sr=(pc+kn+1)/2;
        if(*this<prod+((x*sr)<<i)) kn=sr-1;
        else pc=sr;
      } d.cyf[i]=pc;
      if(pc) d.len=max(d.len,i+1);
      prod+=(x*pc)<<i;
    } *this=d; return *this;
  }
  
  int operator /= (int x) {
    LL d=0;
    FORD(i,len-1,0) {
      d=d*BASE+cyf[i];
      cyf[i]=d/x; d%=x;
    } dropZeros();
    return d;
  }
  
  Natural operator / (const Natural &x) const { Natural y=*this; y/=x; return y; }
  
  int operator % (int x) {
    LL d=0;
    FORD(i,len-1,0) d=(d*BASE+cyf[i])%x;
    return d;
  }
  
  Natural& operator %= (const Natural &x) {
    Natural y=*this; y/=x; y*=x; *this-=y; return *this;
  }
  
  Natural operator % (const Natural &x) const { Natural y=*this; y%=x; return y; }
  
  Natural& operator = (const string s) {
    int n=s.length(); *this=0;
    len=n/BD+1; resize(len);
    REP(i,n) cyf[(n-1-i)/BD]=10*cyf[(n-1-i)/BD]+s[i]-'0';
    dropZeros(); return *this;
  }
  
  void write() const {
    printf("%d", (int)cyf[len-1]);
    FORD(i,len-2,0) printf("%0*d", BD, (int)cyf[i]);
    printf("\n");
  }
  
  bool odd() const { return cyf[0]%2; }
};

Natural gcd(const Natural &x, const Natural &y) {
  Natural a=x, b=y, r=1;
  while(a!=0 && b!=0) { if(a<b) swap(a,b);
    if(a.odd()) { if(b.odd()) a-=b; else b/=2; }
    else { if(b.odd()) a/=2; else {r*=2; a/=2; b/=2;} }
  } return a==0?r*b:r*a;
}

Natural tab[1005];
int n;

char bufor[100];

int main() {
  int d;
  scanf("%d\n",&d);
  for(int tc=1;tc<=d;++tc) {
    scanf("%d\n",&n);
    for(int j=1;j<=n;++j) {
      scanf("%s\n",bufor);
      tab[j]=bufor;
    }
    sort(tab+1,tab+n+1);
    Natural T(0);
    for(int i=1;i<n;++i) {
      Natural tmp=gcd(T,tab[i+1]-tab[i]);
      T=tmp;
    }
    Natural resz=(tab[1]%T);
    Natural ret=T-resz;
    ret%=T;
    printf("Case #%d: ",tc);
    ret.write();
  }
  return 0;
}
