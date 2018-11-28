//////////////////////////////////////////////////////////////////////////
//
// 
//
// Problem: 
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

#define TWO(x) (1 << (x))

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

template <class _T1, class _T2>
istream& operator >> (istream& cin, pair <_T1, _T2> &p)
  {return cin >> p.X >> p.Y;}

template <class _T1, class _T2>
ostream& operator << (ostream& cout, const pair <_T1, _T2> &p)
  {return cout << p.X << " " << p.Y;}
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////////////
///////CODE THAT WAS ACTUALLY TYPED FOR THIS PROBLEM STARTS HERE//////////
//////////////////////////////////////////////////////////////////////////

int ntest;

bool operator < (VI& a, VI& b)
  {
  REP(i, SIZE(a))
    if (a[i] >= b[i])
      return false;

  return true;
  }

int main()
  { 
  cin >> ntest;

  REP(ctest, ntest)
    {
    int n, k;

    cin >> n >> k;

    VE<VI> d;

    REP(i, n)
      {
      VI row;
      CINTO(int, k, row);
      d.PB(row);
      }

    int ans = 0;

    REP(i, 1 << n)
      {
      bool ok = true;
      int count = 0;
      REP(j, n)
        if (i & TWO(j))
          ++count;

      REP(j, n)
        if (i & TWO(j))
          REP(k, n)
            if (i & TWO(k))
              if (d[j] < d[k] || d[k] < d[j])
                {
                ok = false;
                }

      if (ok)
        ans = FMAX(ans, count);
      }

    //while (SIZE(d))
    //  {
    //  VB larger_than_something(SIZE(d), false);
    //  REP(i, SIZE(d))
    //    REP(j, SIZE(d))
    //      if (d[i] < d[j])
    //        larger_than_something[j] = true;

    //  VE<VI> new_d;
    //  REP(i, SIZE(d))
    //    if (larger_than_something[i])
    //      new_d.PB(d[i]);

    //  ans = FMAX(ans, SIZE(d) - SIZE(new_d));
    //  
    //  d = new_d;
    //  }

    printf("Case #%d: %d\n", ctest + 1, ans);
    }

  return 0;
  }
