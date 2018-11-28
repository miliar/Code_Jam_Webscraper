// #include "template.cc"
// C++0x - e.g. gcc 4.6
#ifndef DEBUG
#define DEBUG 0
#endif
#include <cmath>
#include <iomanip>
#include <array>
#include <iostream>
#include <tuple>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>
#include <algorithm>
#include <exception>
#include <cassert>
#include <cstring>
using namespace std;
#define forn(i,n) for(i=0;i<n;++i)
#define zero_array(a) memset(&a,0,sizeof(a))
#define umap unordered_map
#define umultimap unordered_multimap
#define uset unordered_set
// BUG: uset creates buggy executables, use umap instead (mingw gcc 4.6.x)
#define die(x) do{cerr<<"ERROR: "<<x<<endl;throw #x;}while(0)
#define fi(N) for(int i=0,Ni=N;i<Ni;++i)
#if DEBUG
# define debug1(x) cerr<<#x<<": "<<x<<endl
# define debug(...) do {  outargs(outargs(std::cerr,# __VA_ARGS__)<<'=', __VA_ARGS__)<<std::endl; } while(0)
# define debugm(m,...) do { std::cerr<<#m<<": ";debug(__VA_ARGS__); } while(0)
#else
# define debug1(x)
# define debug(...)
# define debugm(...)
#endif
#define readq(n) do{if (!(cin>>n)) { die("read "<<#n); }  }while(0)
#define read(n) do{readq(n); debug(n); }while(0)
#define write(n) do{cout<<n;debug(n);}while(0)
typedef long long int64;
typedef unsigned long long uint64;
typedef int64 I;
typedef uint64 U;
typedef double F;
U gcd(U a, U b) {
  while (b) {
    U t=b;
    b=a%b;
    a=t;
  }
  return a;
}

template <class O,class F>
O& outargs(O& o,F const& f) {
  return o<<f;
}
template <class O,class F,class... A>
O& outargs(O& o,F const& f,A... a) {
  o<<f<<' ';
  return outargs(o,a...);
}
template <class Cont,class F>
auto mapv(Cont const& c,F const&f) -> vector<decltype(f(*begin(c)))>
{
  vector<decltype(f(*begin(c)))> ret;
  for (auto const& x: c) ret.push_back(f(x));
  return ret;
}
int ucord(char c) {
  assert(c>='A'&&c<='Z');
  return c-'A';
}
char orduc(int o) {
  return 'A'+o;
}
int lcord(char c) {
  assert(c>='a'&&c<='z');
  return c-'a';
}
char ordlc(int o) {
  return 'a'+o;
}
template <class I,class J> I maxeq(I &m,J const& x) { if (m<x) m=x; }
template <class I,class J> I mineq(I &m,J const& x) { if (x<m) m=x; }
template <class I> I abs(I x) { return x<0 ? -x : x; }
template <class T>
vector<T> split(string const& s) {
  vector<T> r;
  istringstream i(s);
  T w;
  while (i>>w)
    r.push_back(w);
  return r;
}
vector<string> splits(string const& s) { return split<string>(s); }
template <class T> inline void hash_combine(size_t& seed, const T& v)
{
    std::hash<T> hasher;
    seed ^= hasher(v) + 0x9e3779b9 + (seed<<6) + (seed>>2);
}
template <long M,class Int=long> // Int should be > m^2 so you can do modular multiplication without mod e.g. 2^31 overflow
struct intmod {
  typedef intmod<M,Int> I;
  Int x;
  static const int modulus=M;
  operator Int() const { return x; }
  explicit intmod(Int x) : x(x%M) {  }
  inline friend ostream& operator<<(ostream &o,I i) { return o<<i.x; }
#define INTMODOP_SHRINK(op) \
  I& operator op ## =(Int y) { x op ## = y; return *this; }                                              \
    I operator op (Int y) const { return intmod<M,Int>(x op y); }
#define INTMODOP(op) \
  I& operator op ## =(Int y) { x op ## = y; x%=M; return *this; }                                              \
    I operator op (Int y) const { return intmod<M,Int>(x op y); }
  INTMODOP(+)INTMODOP(-)INTMODOP(*)INTMODOP(<<)INTMODOP(^)INTMODOP(|)
  INTMODOP_SHRINK(/)INTMODOP_SHRINK(%)INTMODOP_SHRINK(>>)INTMODOP_SHRINK(&)
#define INTMODOP_COMP(comp) \
  bool operator comp(Int y) const { return x comp y; }
  INTMODOP_COMP(==)INTMODOP_COMP(!=)INTMODOP_COMP(<)INTMODOP_COMP(<=)INTMODOP_COMP(>)INTMODOP_COMP(>=)
  I pow(Int e) const { // *this^e in log-time
    I t(1),a=*this;
    while(e>0) {
      if (e%2)
        t*=a;
      a*=a;
      e/=2;
    }
    return a;
  }
  friend inline I pow(I b,Int e) {
    return b.pow(e);
  }
  I inverse() const { // return mult inverse. M must be prime
    return pow(M-2);
  }
  friend inline I binomialk(Int n,Int k) { // the binomial coeffecient C(n,k) = ways of choosing a subset of size k from a set of size n = the ways of splitting the range [0...n+1] of n+2 items, into k+1 nonempty parts = the coefficient c*x^k of (1+x)^n.
    if (k>(n-k))
      return binomialk(n,n-k);
    I num(1),den(1);
    for(int i=n;i>n-k;--i) num*=i; // post: num=n^k_ (factorial decaying power)=n!/(n-k)!
    for(int i(k);i>1;--i) den*=i; // post: den=k!
    return num*den.inverse();
  }
};
struct sep {
  char const* s;
  bool squelch;
  sep(char const* s) : s(s),squelch(true) {  }
  operator char const* ()  {
    if (squelch) {
      squelch=false;
      return "";
    } else
      return s;
  }
};
template <class O,class C>
O& outlist(O &o,C const& c,char const* space=", ",char const* pre="[",char const* post="]") {
  o<<pre;
  sep s(space);
  for (auto const& x: c)
    o<<s<<x;
  return o<<post;
}
template <class O,class E>
O& operator<<(O&o,vector<E> const& v) { return outlist(o,v); }
template <class S> void szero(S &s) {
  for (auto &x:s) x=0;
}
template <class K,class Counts>
struct counted_stack : vector<K> {
  template <class I>
  counted_stack(I const& ninit) : n(ninit) {  }
  Counts n;
  // don't modify vector any other way than the below:
  void clear() { szero(n); vector<K>::clear(); }
  void push(K x) { this->push_back(x);++n[x]; }
  void pop() { --n[this->back()];this->pop_back(); }
};
// F f; F::argument_type; template <class Recur> f(argument_type const& a,Recur &r) { if (a==0) return 0; return 1+r(a-1,r); }
template <class F>
struct nomemo {
  F f;
  nomemo(F f=F()) : f(f) {  }
  //nomemo(nomemo<F> const& m) : f(m.f) {}
  typename F::return_type operator()(typename F::argument_type const& a) {
    return f(a,*this);
  }
  template <class A>
  auto operator()(A const& a) -> decltype(f(a,nomemo<F>())) {
    return f(a,*this);
  }
};
//TODO: allow f that fails to reach base case by entering those cases into memo instead of into f logic (saves branches)
template <class F>
struct memo { // unlocked (single thread)
  F f;
  typedef typename F::argument_type Key;
  typedef typename F::return_type Val;
  typedef Val return_type;
  typedef umap<Key,Val> Map;
  Map m;
  memo(F f=F()) : f(f) {  }
  //memo(memo<F> const& m) : f(m.f) {}
  template <class A>
  return_type const& operator()(A const& a) {
    auto i=m.find(a);
    if (i==m.end())
      return m[a]=f(a,*this);
    return i->second;
  }
};
template <class Vector> inline
typename Vector::value_type &at(Vector &vec,std::size_t i,const typename Vector::value_type &default_value)
{
    std::size_t sz=vec.size();
    if (i>=sz)
        vec.resize(i+1,default_value);
    return vec[i];
}
template <class Vector> inline
typename Vector::value_type &at(Vector &vec,std::size_t i)
{
    std::size_t sz=vec.size();
    if (i>=sz)
        vec.resize(i+1);
    return vec[i];
}
template <class I>
struct fact_m { // memoized. no locking.
  vector<I> m;
  explicit fact_m(int n=0) : m(1,I(1)) {
    (*this)(n);
  }
  I operator()(int i) {
    for (int k=m.size()-1;k<i;++k)
      m.push_back(m[k]*k+1);
    return m[i];
  }
};
fact_m<int64> factorial;

int Ncase;
int icase;


void solve(); // you supply

void problem() { // yo i'll solve it.
  solve();
  cout<<endl;
}

int main() {
  read(Ncase);
  for (icase=1;icase<=Ncase;++icase) {
    cout<<"Case #"<<icase<<": ";
    cerr<<endl;
    problem();
  }
  return 0;
}

// system specific typedef for ulong should go here (or use boost::uint64_t)

//from http://stackoverflow.com/questions/3918968/brute-force-single-threaded-prime-factorization

template <class O>
// Caller needs to pass in an empty factors vector
void append_factors(O factors, U num)
{
  // Num has to be at least 2 to contain "prime" factors
  if (num<2)
    return;

  U workingNum=num;
  U nextOffset=2; // Will be used to skip multiples of 3, later

  // Factor out factors of 2
  while (workingNum%2==0)
  {
    *factors=2;++factors;
    workingNum/=2;
  }

  // Factor out factors of 3
  while (workingNum%3==0)
  {
    *factors=3;++factors;
    workingNum/=3;
  }

  // If all of the factors were 2s and 3s, done...
  if (workingNum==1)
    return;

  // sqrtNum is the (inclusive) upper bound of our search for factors
  U sqrtNum=(U) sqrt(double(workingNum+0.5));

  // Factor out potential factors that are greate than or equal to 5
  // The variable n represents the next potential factor to be tested
  for (U n=5;n<=sqrtNum;)
  {
    // Is n a factor of the current working number?
    if (workingNum%n==0)
    {
      // n is a factor, so add it to the list of factors
      *factors=n;++factors;

      // Divide current working number by n, to get remaining number to factor
      workingNum/=n;

      // Check if we've found all factors
      if (workingNum==1)
        return;

      // Recalculate the new upper bound for remaining factors
      sqrtNum=(U) sqrt(double(workingNum+0.5));

      // Recheck if n is a factor of the new working number,
      // in case workingNum contains multiple factors of n
      continue;
    }

    // n is not or is no longer a factor, try the next odd number
    // that is not a multiple of 3
    n+=nextOffset;
    // Adjust nextOffset to be an offset from n to the next non-multiple of 3
    nextOffset=(nextOffset==2UL ? 4UL : 2UL);
  }

  // Current workingNum is prime, add it as a factor
  *factors=workingNum;++factors;
}

vector<U>& set_factors(vector<U> &out,U num) {
  out.clear();
  append_factors(back_inserter(out),num);
  return out;
}

vector<U> factors(U num) {
  vector<U> ret;
  return set_factors(ret,num);
}

ostream& operator<<(ostream &o,vector<U> const& v) {
  o<<'[';
  for (auto const& x : v)
    o<<x<<' ';
  return o<<']';
}

template <class C,class X>
bool contains(C const& c,X const& x) {
  return c.find(x)!=c.end();
}
