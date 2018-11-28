
//Tomasz Kulczyński
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }


/* Duze liczby odziedziczone po Orzelkach.
 * Uzywac w przypadku potrzeby uzycia wielu operacji na Bignumach.
 */

class Natural {
  /* obowiazkowa czesc prywatna */
  static const int BASE = 100000000;
  static const int BASEDIGS = 8;
  int ndigs;
  int *digs;
  void init(int n,const int *d) {
    while(n>0 && d[n-1]==0) --n;
    ndigs=n;
    digs=new int[n];
    for(int i=0;i<n;++i) digs[i]=d[i];
  }
  Natural(int n,const int *d) { init(n,d); }
  /* przesuwanie (dla dzielenia i pierwiastkowania) */
  Natural operator<<(int sh) const { // sh >= 0
    int n=sh+ndigs;
    int d[n];
    REP(i,sh) d[i]=0;
    REP(i,ndigs) d[i+sh]=digs[i];
    return Natural(n,d);
  }
public:
  /* konstruktory */
  Natural(int x=0) {
    int d[2];
    d[0]=x%BASE;
    d[1]=x/BASE;
    init(2,d);
  }
  Natural(const Natural&a) {
    init(a.ndigs,a.digs);
  }
  Natural(const char *s) {
    int n=strlen(s);
    int nd=n/BASEDIGS+1;
    int d[nd];
    REP(i,nd) {
      d[i]=0;
      FORD(j,BASEDIGS-1,0) {
        int poz=i*BASEDIGS+j;
        if(poz<n) d[i]=10*d[i]+s[n-1-poz]-'0';
      }
    }
    init(nd,d);
  }
  /* destruktor */
  ~Natural() { delete[] digs; }
  /* przypisanie */
  Natural &operator=(const Natural&a) {
    delete[] digs;
    init(a.ndigs,a.digs);
    return *this;
  }
  /* dodawanie */
  Natural operator+(const Natural&a) const {
    int n=max(ndigs,a.ndigs)+1;
    int d[n];
    REP(i,n) d[i]=0;
    REP(i,n) {
      if(i<ndigs) d[i]+=digs[i];
      if(i<a.ndigs) d[i]+=a.digs[i];
      if(d[i]>=BASE) { d[i]-=BASE; ++d[i+1]; }
    }
    return Natural(n,d);
  }
  Natural &operator+=(const Natural&a) {
    return *this = *this + a;
  }
  /* odejmowanie */
  Natural operator-(const Natural&a) const { // a <= *this
    int d[ndigs];
    REP(i,ndigs) d[i]=digs[i];
    REP(i,ndigs) {
      if (i < a.ndigs) d[i]-=a.digs[i];
      if (d[i] < 0) {
        d[i]+=BASE;
        --d[i+1];
      }
    }
    return Natural(ndigs,d);
  }
  Natural &operator-=(const Natural&a) {
    return *this = *this - a;
  }
  /* mnozenie liczb */
  Natural operator*(const Natural&a) const {
    int n=ndigs+a.ndigs;
    int d[n];
    REP(i,n) d[i]=0;
    REP(i,ndigs) {
      int p=0;
      REP(j,a.ndigs) {
        long long v=(long long)(digs[i])*a.digs[j];
        int v1=v/BASE,v0=v%BASE;
        d[i+j]+=v0+p;
        p=v1+d[i+j]/BASE;
        d[i+j]%=BASE;
      }
      for(int j=i+a.ndigs;p>0;++j) {
        d[j]+=p;
        p=d[j]/BASE;
        d[j]%=BASE;
      }
    }
    return Natural(n,d);
  }
  Natural &operator*=(const Natural&a) {
    return *this = *this * a;
  }
  /* dzielenie liczb */
  Natural operator/(const Natural&a) const {
    int n=max(ndigs-a.ndigs+1,0);
    int d[n];
    Natural prod;
    FORD(i,n-1,0) {
      int l=0, r=BASE-1;
      while(l<r) {
        int m=(l+r+1)/2;
        if (*this<prod+(a*m<<i))
	  r=m-1;
	else
	  l=m;
      }
      prod+=a*l<<i;
      d[i]=l;
    }
    return Natural(n,d);
  }
  Natural &operator/=(const Natural&a) {
    return *this = *this / a;
  }
  /* modulo */
  Natural operator%(const Natural&a) const {
    return *this - *this/a*a;
  }
  Natural &operator%=(const Natural&a) {
    return *this = *this % a;
  }
  /* pierwiastek */
  Natural sqrt() const {
    int n=(ndigs+1)/2;
    int d[n];
    REP(i,n) d[i]=0;
    Natural sq;
    FORD(i,n-1,0) {
      Natural a(n,d);
      int l=0, r=BASE-1;
      while(l<r) {
        int m=(l+r+1)/2;
        if (*this<sq+(a*2*m<<i)+(Natural(m)*m<<2*i))
	  r=m-1;
	else
	  l=m;
      }
      sq+=(a*2*l<<i)+(Natural(l)*l<<2*i);
      d[i]=l;
    }
    return Natural(n,d);
  }
  /* mnozenie przez inta */
  Natural operator*(int x) const { // !!! 0 <= x <= BASE
    int n=ndigs+1;
    int d[n];
    long long a=0;
    REP(i,ndigs) {
      a+=digs[i]*(long long)x;
      d[i]=a%BASE;
      a/=BASE;
    }
    d[ndigs]=a;
    return Natural(n,d);
  }
  Natural &operator*=(int x) {
    return *this = *this * x;
  }
  /* dzielenie przez inta */
  Natural operator/(int x) const { // !!! 0 < x
    int d[ndigs];
    long long a=0;
    FORD(i,ndigs-1,0) {
      a=BASE*a+digs[i];
      d[i]=a/x;
      a%=x;
    }
    return Natural(ndigs,d);
  }
  Natural &operator/=(int x) {
    return *this = *this / x;
  }
  /* modulo int */
  int operator%(int x) const { // !!! 0 < x
    long long a=0;
    FORD(i,ndigs-1,0) {
      a=BASE*a+digs[i];
      a%=x;
    }
    return a;
  }
  /* porównania (< potrzebne dla dzielenia i pierwiastka) */
  bool operator<(const Natural&a) const {
    if(ndigs<a.ndigs) return true;
    if(ndigs>a.ndigs) return false;
    FORD(i,ndigs-1,0) {
      if(digs[i]<a.digs[i]) return true;
      if(digs[i]>a.digs[i]) return false;
    }
    return false;
  }
  bool operator==(const Natural&a) const {
    if(ndigs!=a.ndigs) return false;
    REP(i,ndigs) {
      if(digs[i]!=a.digs[i]) return false;
    }
    return true;
  }
  bool operator>(const Natural&a) const { return a<*this; }
  bool operator<=(const Natural&a) const { return !(a<*this); }
  bool operator>=(const Natural&a) const { return !(*this<a); }
  bool operator!=(const Natural&a) const { return !(*this==a); }
  /* wypisywanie */
  void write() const {
    if(ndigs==0) printf("0");
    else {
      printf("%d",digs[ndigs-1]);
      FORD(i,ndigs-2,0) printf("%0*d",BASEDIGS,digs[i]);
    }
  }
  void write(char *buf) const {
    if(ndigs==0) sprintf(buf,"0");
    else {
      int pos=0;
      pos+=sprintf(buf,"%d",digs[ndigs-1]);
      FORD(i,ndigs-2,0) pos+=sprintf(buf+pos,"%0*d",BASEDIGS,digs[i]);
    }
  }
};


Natural nwd(Natural a, Natural b)
{
//    a.write(); printf(" "); b.write(); printf(" %d\n",a==0); 
    return (a!=0) ? (nwd(b%a, a)) : (b);
}

Natural t0, t, T;
char buf[57];

int main()
{
    int dd, cas = 0;
    scanf("%d",&dd);
    while(dd--)
    {
        int n;
        T = 0;
        scanf("%d %s",&n,buf);
        t0 = Natural(buf);
        REP(i,n-1) 
        {
            scanf("%s",buf);
            t = Natural(buf);
            T = nwd(T, t>t0 ? t-t0 : (t0-t) );
    //        (t-t0).write(); puts("");
    //       T.write(); puts("");
        }
        printf("Case #%d: ",++cas);
    //    T.write(); puts("");
        ((T - t0%T) % T).write();    puts("");
    }
    return 0;
}
