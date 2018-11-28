//////////////////////////////////////////////////////////////////////////
//
// GCJ Round 1
//
// Problem: Saving the Universe
// 
// Language: Numbers
//
// by Michael Rybak
//
//////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////
///NOTE: THIS PROGRAM CONTAINS SOME COPY-PASTED CODE//////////////////////
///SEE BELOW FOR THE MARK WHERE ACTUALLY TYPED CODE STARTS////////////////
//////////////////////////////////////////////////////////////////////////


#define ASSERT(x) if (!(x)) while (1) cout << 1;else 1
#include <iostream>
#include "stdio.h"
#include <list>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <math.h>
#include <sstream>
#include <fcntl.h>
#include <set>
using namespace std;

typedef unsigned long ulong;
typedef unsigned char uchar;
typedef long long llong;
typedef long double ldouble;
typedef short int sint;
typedef unsigned short int usint;


//strings/////////////////////////////////////////////////////////////////
#define STR string
#define GETCOREOF(c, eof) c=0;eof=scanf("%c", &(c))==EOF;
#define SERASELAST(s) if (SIZE(s)) (s).erase(--(s).end(), (s).end())
template <class _T> STR TO_S(_T v)
{ostringstream o;o<<v;return o.str();}
template <class _T> _T FROM_S(STR& s)
{_T v;istringstream i(s);i>>v;return v;}

//vectors/////////////////////////////////////////////////////////////////
#define VE vector
#define SIZE(a) ((int)(a).size())
#define IT iterator
#define VI VE < int >
#define PB push_back
#define PPB pop_back
#define ALL(c) (c).begin(), (c).end()
#define UNIQ(c) sort(ALL(c)), (c).resize(unique(ALL(c)) - (c).begin());
#define VD VE < double >
#define VB VE < bool >
#define VS VE < STR >
#define REV(a) reverse((a).begin(), (a).end())
#define DECALL(_T,a) FOREACH(_T,_it,a)--(*_it);
#define INCALL(_T,a) FOREACH(_T,_it,a)++(*_it);
#define CINTO(_T,n,a) {REP(_i, n) {_T _v; cin >> _v; (a).PB(_v);}}
#define CINNTO(_T,n,a) cin>>n;{REP(_i, n) {_T v; cin >> v; (a).PB(v);}}
#define COUTALL(_T,a,d) {REP(_i,SIZE(a)) cout<<a[_i]<<(_i==_n-1?"\n":d);}
#define CINSTRTO(n,a){REP(_i,n){STR v;getline(cin,v);(a).PB(v);}}
#define CINNSTRTO(n,a)\
  cin>>n; {STR v;getline(cin,v);REP(_i,n){getline(cin,v);(a).PB(v);}}

//cycles//////////////////////////////////////////////////////////////////
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH01(T,it,it0,it1)\
  for(VE< T >::IT it(it0),_itn(it1);it!=_itn;++it)
#define FOREACH(T,it,c) FOREACH01(T,it,(c).begin(),(c).end())
#define FOREACHI01(T,it,it0,it1,i)\
  int i = 0;for(VE< T >::IT it=it0,_itn(it1);it!=_itn;++it,++i)
#define FOREACHI(T,it,i,c) FOREACHI01(T,it,(c).begin(),(c).end(),i)
#define FOREACHNEXT01(T,icur,inext,it0,it1,c)for(VE< T >::IT\
  icur=it0,inext=it0+1;icur!=it1&&inext!=it1;++icur,++inext)
#define FOREACHNEXT(T,icur,inext,c)\
  FOREACHNEXT01(T,icur,inext,(c).begin(),(c).end(),c) 
#define FINDI01(i,i0,i1,v,pre) bool found_ = false;\
  FOR(i_, i0, i1)if (pre){i = i_;found_ = true; break;}
#define FINDI(i,v,pre) FINDI_(i,0,SIZE(v),v,pre)

//misc////////////////////////////////////////////////////////////////////
#define TWO(x) (1<<(x))
#define MSET(a, v) memset(a, v, sizeof(a))
#define MSET0(a) MSET(a, 0)
#define FMIN(a, b) ((a) < (b) ? (a) : (b))
#define FMAX(a, b) ((a) > (b) ? (a) : (b))
#define INF 1000000000
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define SIGN(a) ((a) > 0 ? 1 : (a) < 0 ? -1 : 0)
#define SQR(a) ((a) * (a))
template <class _T> void SWP(_T& a, _T& b) {_T c=a;a=b;b=c;}
template <class _T> void SWP3(_T& a, _T& b, _T& c) {_T d=a;a=b;b=c;c=d;}
template <class _T> void SWP4(_T&a,_T&b,_T&c,_T&d){_T e=a;a=b;b=c;c=d;d=e;}
template <class _T> void ORDER(_T& a, _T& b) {if(a>b)SWP(a,b);}
template <class _T> void RORDER(_T& a, _T& b) {if(a<b)SWP(a,b);}
template <class _T> bool BTW(const _T&a, const _T&a0, const _T&a1)
{return a0<a&&a<a1;}
template <class _T> bool BTWE(const _T&a, const _T&a0, const _T&a1)
{return a0<=a&&a<=a1;}

//maps////////////////////////////////////////////////////////////////////
#define MM multimap
#define MMII MM <int, int>
#define INS insert
#define LOWB lower_bound
#define UPB upper_bound
#define HASKEY(m, k) ((m).LOWB(k) != (m).UPB(k))
#define FORKEYVALS(TK,TV,it,m,k)\
  for(MM<TK,TV>::IT it=m.LOWB(k),_iend=m.UPB(k);it!=_iend;++it)

//pairs///////////////////////////////////////////////////////////////////
typedef pair<int, int> PII;
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second

inline int TrOrder(const PII& a, const PII& b, const PII& c)
{return SIGN((b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X));}

inline int TrS(const PII& a, const PII& b, const PII& c)
{return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);}

template <class _T1, class _T2>
istream& operator >> (istream& cin, pair <_T1, _T2> &p)
{return cin >> p.X >> p.Y;}

template <class _T1, class _T2>
ostream& operator << (ostream& cout, const pair <_T1, _T2> &p)
{return cout << p.X << " " << p.Y;}
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////
// long nums
//////////////////////////////////////////////////////////////////////////
const int MAX_ANS_LEN = 256;

#define L_0 L_(0)
#define L_1 L_(1)
#define L_2 L_(2)
typedef llong L_;

template <long MAX_LEN> struct CNumber {
  long len;
  long float_len; //fraction
  long print_digits_after_point;
  bool is_rounded;//if false, truncated
  char sign;
  bool exponential_form;

  uchar data[MAX_LEN];

  void Init();//default constr
  CNumber ();
  CNumber (L_ i);
  CNumber (ldouble v);

  void UpdateLen(long i_max = -1);
  char GetDigit(long id) const; //if id < 0, returns 0 
  CNumber<MAX_LEN>& MulByPow10(long power);
  CNumber<MAX_LEN> operator + (const CNumber<MAX_LEN>& b) const;
  CNumber<MAX_LEN> operator - (const CNumber<MAX_LEN>& b) const;
  CNumber<MAX_LEN> operator * (const CNumber<MAX_LEN>& b) const;
  bool operator <  (const CNumber<MAX_LEN>& b) const;
  bool operator <=  (const CNumber<MAX_LEN>& b) const;
  bool operator >  (const CNumber<MAX_LEN>& b) const;
  bool operator == (const CNumber<MAX_LEN>& b) const;
  CNumber<MAX_LEN>& operator += (const CNumber<MAX_LEN>& b);
  CNumber<MAX_LEN>& operator -= (const CNumber<MAX_LEN>& b);
  CNumber<MAX_LEN>& operator *= (const CNumber<MAX_LEN>& b);

private:
  CNumber<MAX_LEN> _UnsignAdd(const CNumber<MAX_LEN>& b) const;
  CNumber<MAX_LEN> _UnsignSub(const CNumber<MAX_LEN>& b) const;
  CNumber<MAX_LEN> _SignedAddOrSub(const CNumber<MAX_LEN>& b, char oper_sign) const;

  long _UnsignCmp(const CNumber<MAX_LEN>& b) const;
};
typedef CNumber <MAX_ANS_LEN> N_;
const N_ N_0 = N_(L_0);
const N_ N_1 = N_(L_1);
const N_ N_2 = N_(L_2);

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
void CNumber<MAX_LEN>::Init() {
  sign = 1;
  len = 1;
  float_len = 0;
  print_digits_after_point = 0;
  is_rounded = true;
  exponential_form = false;
  memset(data, 0, sizeof(data));
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>::CNumber() 
{
  Init();
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>::CNumber(L_ i)
{
  Init();

  len = 0;
  for (; i > 0; i /= 10)
    data[len++] = char(i % 10);
  if (!len) len = 1;
  float_len = 0;
  UpdateLen();
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
void CNumber<MAX_LEN>::UpdateLen(long i_max) {
  if (i_max == -1)
    i_max = len;

  ASSERT(i_max < MAX_LEN);

  long first_non_nil = 0;
  for (;
    data[first_non_nil] == 0 && 
    first_non_nil < i_max &&
    first_non_nil < float_len
    ;
  ++first_non_nil);

  long last_non_nil = i_max;
  for (; 
    data[last_non_nil] == 0 && 
    last_non_nil > first_non_nil &&
    last_non_nil > float_len
    ; 
  --last_non_nil);

  if (first_non_nil)
    for (long i = first_non_nil; i <= last_non_nil; ++i) {
      data[i - first_non_nil] = data[i];
      data[i] = 0;
    } 

    float_len -= first_non_nil;
    len = last_non_nil - first_non_nil + 1;
    if (len == 1 && data[0] == 0)
      sign = 1;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
char CNumber<MAX_LEN>::GetDigit(long id) const {
  //if id < 0, returns 0 
  return (id >= len) 
    ? 0 
    : (id >= 0) ? data[id] : 0;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>& CNumber<MAX_LEN>::MulByPow10(long power) {
  if (power == 0)
    return *this;

  if (power > 0) {
    for (long i = len - 1; i >= 0; --i) {
      data[i + power] = data[i];
      data[i] = 0;
    }
    len += power;
  }
  else 
    float_len -= power;
  UpdateLen(FMAX(len, float_len));
  return *this;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN> CNumber<MAX_LEN>::_UnsignAdd(const CNumber<MAX_LEN>& b) const
{
  static CNumber<MAX_LEN> r;
  r = CNumber<MAX_LEN>();

  long fl = FMAX(float_len, b.float_len);
  r.float_len = fl;

  long d = 0, v;
  for (long i = -fl; i + float_len <= len || i + b.float_len <= b.len; ++i) {
    v = GetDigit(float_len + i) + b.GetDigit(b.float_len + i) + d;
    d = 0;
    if (v >= 10) {
      d = 1;
      v -= 10;
    }
    r.data[r.float_len + i] = char(v);
  }

  ASSERT(d == 0);

  r.UpdateLen(fl + FMAX(len - float_len, b.len - b.float_len) + 1);
  r.print_digits_after_point = FMAX(print_digits_after_point,
    b.print_digits_after_point);
  r.is_rounded = is_rounded && b.is_rounded;

  return r;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN> CNumber<MAX_LEN>::_UnsignSub(const CNumber<MAX_LEN>& b) const
{
  static CNumber<MAX_LEN> r;
  r = CNumber<MAX_LEN>();

  long fl = FMAX(float_len, b.float_len);
  r.float_len = fl;

  long d = 0, v;
  for (long i = -fl; i + float_len <= len || i + b.float_len <= b.len; ++i) {
    v = GetDigit(float_len + i) - b.GetDigit(b.float_len + i) + d;
    d = 0;
    if (v < 0) {
      d = -1;
      v += 10;
    }
    r.data[r.float_len + i] = char(v);
  }

  ASSERT(d == 0);

  r.UpdateLen(fl + FMAX(len - float_len, b.len - b.float_len) + 1);
  r.print_digits_after_point = FMAX(print_digits_after_point,
    b.print_digits_after_point);
  r.is_rounded = is_rounded && b.is_rounded;

  return r;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN>
long CNumber<MAX_LEN>::_UnsignCmp(const CNumber<MAX_LEN>& b) const{
  long first = FMAX(len - float_len, b.len - b.float_len);
  long last = -FMAX(float_len, b.float_len);

  char ca, cb;
  for (long i = first; i >= last; --i) {
    ca = GetDigit(float_len + i);
    cb = b.GetDigit(b.float_len + i);
    if (ca < cb)
      return -1;
    if (ca > cb)
      return 1;
  }
  return 0;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN>
CNumber<MAX_LEN> CNumber<MAX_LEN>::_SignedAddOrSub(
  const CNumber<MAX_LEN>& b, char oper_sign) const
{
  static CNumber<MAX_LEN> r;
  r = CNumber<MAX_LEN>();

  if (sign == b.sign * oper_sign) {
    r = _UnsignAdd(b);
    r.sign = sign;
  } 
  else if (_UnsignCmp(b) >= 0) {
    r = _UnsignSub(b);
    r.sign = sign;
  }
  else {
    r = b._UnsignSub(*this);
    r.sign = b.sign * oper_sign;
  }

  return r;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN> CNumber<MAX_LEN>::operator + (
  const CNumber<MAX_LEN>& b) const
{
  return _SignedAddOrSub(b, +1);
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN> CNumber<MAX_LEN>::operator - (
  const CNumber<MAX_LEN>& b) const
{
  return _SignedAddOrSub(b, -1);
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN> CNumber<MAX_LEN>::operator * (const CNumber<MAX_LEN>& b) const{
  static CNumber<MAX_LEN> r;
  r = CNumber<MAX_LEN>();

  long res_len = len + b.len + 2;
  long d = 0, v;
  for (long i = 0; i < res_len; ++i) {
    v = d;
    for (long j = FMAX(0, i - len + 1); j < b.len && j <= i; ++j)
      v += b.GetDigit(j) * GetDigit(i - j);
    r.data[i] = char(v % 10);
    d = v / 10;
  }
  ASSERT(d == 0);

  r.float_len = float_len + b.float_len;
  r.UpdateLen(res_len);
  r.print_digits_after_point = FMAX(print_digits_after_point,
    b.print_digits_after_point);
  r.is_rounded = is_rounded && b.is_rounded;
  r.sign = sign * b.sign;

  return r;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
bool CNumber<MAX_LEN>::operator < (const CNumber<MAX_LEN>& b) const{
  if (sign != b.sign)
    return (sign < b.sign);  
  return (sign * _UnsignCmp(b) == -1);
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
bool CNumber<MAX_LEN>::operator <= (const CNumber<MAX_LEN>& b) const{
  if (sign != b.sign)
    return (sign < b.sign);  
  return (sign * _UnsignCmp(b) < 1);
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
bool CNumber<MAX_LEN>::operator > (const CNumber<MAX_LEN>& b) const{
  return b < *this;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
bool CNumber<MAX_LEN>::operator == (const CNumber<MAX_LEN>& b) const{
  return (sign == b.sign && _UnsignCmp(b) == 0);
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>& CNumber<MAX_LEN>::operator += (const CNumber<MAX_LEN>& b) 
{
  static CNumber<MAX_LEN> t;
  t = *this;

  *this = t + b;
  return *this;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>& CNumber<MAX_LEN>::operator -= (const CNumber<MAX_LEN>& b) 
{
  static CNumber<MAX_LEN> t;
  t = *this;

  *this = t - b;
  return *this;
}

//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN> 
CNumber<MAX_LEN>& CNumber<MAX_LEN>::operator *= (const CNumber<MAX_LEN>& b) 
{
  static CNumber<MAX_LEN> t;
  t = *this;

  *this = t * b;
  return *this;
}
//////////////////////////////////////////////////////////////////////////
template <long MAX_LEN>
ostream& operator << (ostream & cout, CNumber<MAX_LEN> const& i_c) {
  static CNumber<MAX_LEN> c;
  c = i_c;

  long d = c.print_digits_after_point;
  if (c.is_rounded) 
  { //round
    static CNumber<MAX_LEN> t;
    t = CNumber<MAX_LEN>(L_ (5));
    t.MulByPow10( -d - 1);
    c += t;
  }

  long e = 0;
  if (c.exponential_form)
  {
    //leave only one symbol in int part
    e = c.len - c.float_len - 1;
    c.MulByPow10(-e);
  }

  long i;

  for (i = c.len - 1; i >= c.float_len; --i)
    cout << long(c.GetDigit(i));

  if (c.print_digits_after_point)
  {
    cout << ".";

    for (i = 1; i <= d; ++i)
      cout << long(c.GetDigit(c.float_len - i));

    if (e != 0) 
      cout << "e" << e;
  }

  return cout;
}
//////////////////////////////////////////////////////////////////////////

#define PK() cin.peek()
#define PKC(cin) cin.peek()

inline void SkipSpaces(istream& cin){while (PKC(cin) == ' ') cin.get();}
//inline void SkipSpaces(){SkipSpaces(cin);}
inline void SkipSpacesEOLN(istream&){
  while (true) {
    if (!(PKC(cin) == ' ' || PKC(cin) == 10 || PKC(cin) == 13))
      break;
    cin.get();
  }
}

template <long MAX_LEN>
istream& operator>>(istream& cin, CNumber<MAX_LEN> & n) {
  n.Init();
  n.len = 0;

  SkipSpacesEOLN(cin);
  if (PK() == '+' || PK() == '-') {
    if (cin.get() == '-') n.sign = -1;
    SkipSpaces(cin);
  }

  if (PK() >= '0' && PK() <= '9') {
    while (PK() >= '0' && PK() <= '9')
      n.data[n.len++] = cin.get() - '0';
  }
  else {
    ASSERT(PK() == '.');
    n.data[n.len++] = 0;
  }

  n.float_len = n.len; //we'll keep int_len here and then when reverse
  if (PK() == '.') 
  {
    cin.get();

    SkipSpaces(cin);
    while (PK() >= '0' && PK() <= '9')
      n.data[n.len++] = cin.get() - '0';

  }

  //reverse
  {
    char t;
    for (long i = 0; i < n.len / 2; ++i) {
      t = n.data[i];
      n.data[i] = n.data[n.len - i - 1];
      n.data[n.len - i - 1] = t;
    }
    n.float_len = n.len - n.float_len;
  }

  n.UpdateLen();

  SkipSpaces(cin);
  if (PK() == 'e' || PK() == 'E') {
    cin.get();
    long pow;
    cin >> pow;
    n.MulByPow10(pow);
  }

  return cin;
}

//////////////////////////////////////////////////////////////////////////


N_ Div(N_ a, N_ b)
//integers only
{
  int len = FMAX(1, a.len - b.len + 2);
  N_ r = N_0;
  r.len = len;
  FORD(i, len - 1, 0)
    FOR(j, 1, 10)
  {
    r.data[i] = j;
    if (r * b > a)
    {
      r.data[i] = j - 1;
      break;
    }
  }

  r.UpdateLen(len);
  return r;
}
//////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////
// Long numbers CMatrix for modular powering
//////////////////////////////////////////////////////////////////////////

template <typename _T>
struct CMatrix
{
  _T a[2][2];
  int n;

  CMatrix operator * (CMatrix& b)
  {
    CMatrix c;
    c.n = n;

    REP(i, n)
      REP(j, n)
    {
      _T s = L_0;
      REP(k, n)
        s += a[i][k] * b.a[k][j];
      c.a[i][j] = s;
    }

    return c;
  }
};

template <typename _T>
CMatrix<_T> powmtx(CMatrix<_T> v, llong p)
{
  //cout << "powering" << endl;

  CMatrix<_T> r;

  r.n = v.n;
  REP(i, r.n)
  {
    REP(j, r.n)
      r.a[i][j] = _T(L_0);
    r.a[i][i] = _T(L_1);
  }

  while (p)
  {
    //cout << p << endl;
    if (p % 2)
      r = r * v;
    v = v * v;
    p /= 2;
  }
  return r;
}

//////////////////////////////////////////////////////////////////////////
///////CODE THAT WAS ACTUALLY TYPED FOR THIS PROBLEM STARTS HERE//////////
//////////////////////////////////////////////////////////////////////////

int ntest;

int main()
{ 
  cin >> ntest;

  REP(ctest, ntest)
  {
    int n;
    cin >> n;

    CMatrix<N_> matrix;
    matrix.n = 2;
    matrix.a[0][0] = N_(L_(3));
    matrix.a[0][1] = N_(L_(5));
    matrix.a[1][0] = N_(L_(1));
    matrix.a[1][1] = N_(L_(3));

    matrix = powmtx(matrix, n);

    N_ a = matrix.a[0][0];
    N_ b = matrix.a[1][0];
    b = b * b * N_(L_(5));

    // now get sqrt from b
    N_ c = N_0;
    c.len = b.len / 2 + 1;
    FORD(i, c.len - 1, 0)
      FORD(v, 9, 0)
      {
        c.data[i] = v;
        if (c * c <= b)
          break;
      }

    a += c;

    cout << "Case #" << ctest + 1 << ": " 
         << int(a.data[2]) << int(a.data[1]) << int(a.data[0]) << endl;

  }

  return 0;
}
