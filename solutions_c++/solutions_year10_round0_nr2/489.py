#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#define EPS 1E-9
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLR(c) memset(c, 0, sizeof(c))
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SSORT(c) stable_sort(ALL(c))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";
#define TCT template <class T>

typedef long long LL; typedef unsigned long long ULL; typedef long double LD;
typedef vector<int> vi; typedef vector<vi> vvi;
typedef vector<string> vs; typedef pair<int,int> pii;

const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);

TCT bool OrdAsc (const T &a, const T &b) {return a < b;}
TCT bool OrdDes (const T &a, const T &b) {return a > b;}
TCT bool OrdXY (const T &a, const T &b) {if (a->x==b->x) RET a->y<b->y; RET a->x<b->x;}
TCT bool OrdYX (const T &a, const T &b) {if (a->y==b->y) RET a->x<b->x; RET a->y<b->y;}
TCT string t2s(T x) {ostringstream o; o << x; return o.str();}
TCT T s2t(string s) {istringstream i(s); T x; i>>x; return x;}
TCT inline int size (const T&c) {return c.size();}

#define REDUCE() while (L>1 && !D[L-1]) --L;

struct BigNum {

  static const int BASE = 1000000000, BD = 9;

  int  L; // #digits (actual length)
  int  A; // #digits (allocated memory, size of D)
   LL *D; // digits

  BigNum (int v = 0, int a = 2) : L(1), A(a), D(new LL[a]) {
    REP(x,A) D[x] = 0;
    if ((D[0]=v) >= BASE) carryUpTo(1);
  }

  BigNum (const BigNum &a) : L(a.L), A(L), D(new LL[A]) {
    REP(x,A) D[x] = a.D[x];
  }

  ~BigNum () { delete D; }

  void resize (int l) {
    if (l > A) {
      LL* ND = new LL[l=max(l,A<<1)];
      REP(x,l) ND[x] = ((x >= A) ? 0 : D[x]);
      delete D; D = ND; A = l;
    }
  }

  void carryUpTo (int p) {
    int x = 0;
    for (;x<p || D[x]<0 || D[x]>=BASE;++x) {
      resize(x+2);
      if (D[x]<0) {LL i=(-D[x]-1)/BASE+1; D[x]+=i*BASE; D[x+1]-=i;}
      else if (D[x]>=BASE) {LL i=D[x]/BASE; D[x]-=i*BASE; D[x+1]+=i;}
    }
    L = max(L,x+1);
    REDUCE();
  }

  // comparative operators

  bool operator == (const BigNum &a) const {
    if (L != a.L) return false;
    REP(x,L) if (D[x] != a.D[x]) return false;
    return true;
  }

  bool operator < (const BigNum &a) const {
    if (L != a.L) return L < a.L;
    int x = L-1;
    while (x && a.D[x] == D[x]) --x;
    return D[x] < a.D[x];
  }

  bool operator >  (const BigNum &a) const { return  (a<*this); }
  bool operator <= (const BigNum &a) const { return !(a<*this); }
  bool operator >= (const BigNum &a) const { return !(*this<a); }
  bool operator != (const BigNum &a) const { return !(*this==a); }

  // operators for ints (32b)

  BigNum& operator = (int a) {
    REP(x,L) D[x] = 0; L = 1;
    if ((D[0]=a)>=BASE) carryUpTo(1);
    return *this;
  }

  void operator += (LL a) {D[0]+=a; carryUpTo(1);}
  void operator -= (int a) {D[0]-=a; carryUpTo(1);}
  void operator *= (int a) {REP(x,L) D[x]*=a; carryUpTo(L);}
   int operator /= (int a) { // returns (this % a)
     LL w = 0;
     FORD(p,L-1,0) {w=w*BASE+D[p]; D[p]=w/a; w%=a;}
     REDUCE();
     return w;
   }

   int operator % (int a) {
     LL w = 0;
     FORD(p,L-1,0) w=(w*BASE+D[p])%a;
     return w;
   }

  // operators for BigNums

  BigNum& operator += (const BigNum &a) {
    resize(a.L);
    REP(x,a.L) D[x] += a.D[x];
    carryUpTo(a.L);
    return *this;
  }

  BigNum& operator -= (const BigNum &a) {
    REP(x,a.L) D[x] -= a.D[x];
    carryUpTo(a.L);
    return *this;
  }

    BigNum& operator *= (const BigNum &a) {
    BigNum c(0,L+a.L);
    REP(x,a.L) {
      REP(y,L) c.D[y+x] += D[y]*a.D[x];
      c.carryUpTo(L+x);
    }
    *this = c;
    return *this;
  }

  BigNum& operator /= (const BigNum &a) {
    int n = max(L-a.L+1,1);
    BigNum d(0,n), prod;
    FORD(i,n-1,0) {
      int l=0, r=BASE-1;
      while(l<r) {
        int  m=(l+r+1)/2;
        if (*this < prod+(a*m<<i))
          r = m-1;
        else
          l = m;
      }
      prod += a*l<<i;
      d.D[i] = l;
      if (l) d.L = max(d.L, i+1);
    }
    *this = d;
    return *this;
  }

  BigNum& operator %= (const BigNum &a) {
    BigNum v = *this;
    v /= a; v *= a;
    *this -= v;
    return *this;
  }

  BigNum& operator = (const BigNum &a) {
    resize(a.L);
    FORD(x, L-1, a.L) D[x] = 0;
    REP(x,a.L) D[x] = a.D[x];
    L = a.L;
    return *this;
  }

  // input & output

  BigNum &operator = (string a) {
    int s = a.length();
    *this = 0;
    resize(L=s/BD+1);
    REP(x,s) D[(s-x-1)/BD]=10*D[(s-x-1)/BD]+a[x]-'0';
    REDUCE();
    return *this;
  }

  void read (const vi &v, int p) {
    *this=0;
    FORD(x,v.size(),0) {
      *this *= p;
      *this += v[x];
    }
  }

  void write () const {
    printf("%d", int(D[L-1]));
    FORD(x,L-2,0) printf("%0*d", BD, int(D[x]));
  }

  string toString () const {
    string res = ""; char buf[10];
    sprintf(buf,"%d", int(D[L-1])); res += string(buf);
    FORD(x,L-2,0) { sprintf(buf,"%0*d", BD, int(D[x])); res += string(buf); }
    return res;
  }

  // shifts (n digits)

  BigNum &operator >>= (int n) {
    if (n>=L) n=L;
    REP(x,L-n) D[x] = D[x+n];
    FORU(x,L-n,n) D[x] = 0;
    L -= n;
    if (L == 0) L = 1;
    return *this;
  }

  BigNum &operator <<= (int n) {
    if (D[0]==0 && L==1) return *this;
    resize(L+n);
    FORD(x,L-1,0) D[x+n] = D[x];
    REP(x,n) D[x]=0;
    L += n;
    return *this;
  }

  BigNum operator + (const BigNum &a) const {BigNum w = *this;  w += a;  return w;}
  BigNum operator - (const BigNum &a) const {BigNum w = *this;  w -= a;  return w;}
  BigNum operator * (const BigNum &a) const {BigNum w = *this;  w *= a;  return w;}
  BigNum operator / (const BigNum &a) const {BigNum w = *this;  w /= a;  return w;}
  BigNum operator % (const BigNum &a) const {BigNum w = *this;  w %= a;  return w;}

  BigNum operator << (int a) {BigNum w = *this; w <<= a; return w; }
  BigNum operator >> (int a) {BigNum w = *this; w >>= a; return w; }
};

vs split (string s, string del = " ") { vs res;
  int ss = s.size(), sdel = del.size();
  for (int p = 0, q; p < ss; p = q+sdel) {
    if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
    if (q-p>0) res.push_back(s.substr(p,q-p));
  } return res;
}

vector<BigNum> splitBigNums (string s, string del = " ") {
  vector<BigNum> res; vs t = split(s,del);
  FORU(i,0,t.size()-1) {
    BigNum bn; bn = t[i];
    res.push_back(bn);
  } return res;
}

BigNum inline gcd (BigNum a, BigNum b) {
  while (b != 0) { BigNum t = a % b; a = b; b = t; }
  return a;
}

BigNum gcd (vector<BigNum> &v) {
  BigNum res = v[0];
  REPS(i,v) {
    res = gcd(res, v[i]);
  }
  return res;
}

int main() {

  int T,N;
  string line;

  scanf("%d\n",&T);
  FORU(testcase,1,T) {
    scanf("%d",&N); getline(cin, line);
    vector<BigNum> bn = splitBigNums(line," ");
    vector<BigNum> r;

    FORU(i,1,bn.size()-1) {
      if (bn[i] > bn[i-1]) r.PB(bn[i] - bn[i-1]);
      else r.PB(bn[i-1] - bn[i]);
    } BigNum res = gcd(r);

    BigNum d = bn[0] / res;
    if (d*res == bn[0]) {
      res = 0;
    } else {
      res = (d+1)*res - bn[0];
    }
    
    printf("Case #%d: ",testcase);
    res.write(); cout << endl;
  }

  return 0;
}
