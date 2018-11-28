#ifndef __HPMV_CPP__
#define __HPMV_CPP__

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <numeric>
#include <functional>
#include "boost/tuple/tuple.hpp"
#include "boost/tuple/tuple_comparison.hpp"
#include "boost/tuple/tuple_io.hpp"
using namespace std;
using namespace boost;

#define FOR(i,n) for(int i=0;i<n;i++)
#define ROF(i,n) for(int i=n-1;i>=0;i--)
#define fin FOR(i,n)
#define fjn FOR(j,n)
#define fim FOR(i,m)
#define fjm FOR(j,m)
#define excl(i,a) if(i==a) continue;

typedef long long bint;

char ___ins[100000];

inline int ini(){int i; scanf("%d", &i); return i;}
inline bint inb(){bint b; scanf("%lld", &b); return b;}
inline double ind(){double d; scanf("%lf", &d); return d;}
inline string ins(){scanf("%s", ___ins); return string(___ins);}
inline string getline(){do{gets(___ins);}while(___ins[0]==0); return string(___ins);}
inline char inc(){char c; while(isspace(c=getchar())){} return c;}

inline void in(int& i){i=ini();}
inline void in(bint& b){b=inb();}
inline void in(double& d){d=ind();}
inline void in(string& s){s=ins();}
inline void in(char& c){c=inc();}

#define gint(a) int a;in(a);
#define gchar(a) char a;in(a);
#define gdouble(a) double a; in(a);
#define gstring(a) string a; in(a);
#define gbint(a) bint a; in(a);

#define g0 get<0>()
#define g1 get<1>()
#define g2 get<2>()
#define g3 get<3>()
#define g4 get<4>()
#define g5 get<5>()

template<typename P, typename Q> inline void in(tuple<P,Q>& p){in(p.g0);in(p.g1);}
template<typename P, typename Q, typename R> inline void in(tuple<P,Q,R>& p){in(p.g0);in(p.g1);in(p.g2);}
template<typename P, typename Q, typename R, typename S> inline void in(tuple<P,Q,R,S>& p){in(p.g0);in(p.g1);in(p.g2);in(p.g3);}
template<typename P, typename Q, typename R, typename S, typename T> inline void in(tuple<P,Q,R,S,T>& p){in(p.g0);in(p.g1);in(p.g2);in(p.g3);in(p.g4);}

template<typename P, typename Q> inline void in(P& p, Q& q){in(p);in(q);}
template<typename P, typename Q, typename R> inline void in(P& p, Q& q, R& r){in(p);in(q);in(r);}
template<typename P, typename Q, typename R, typename S> inline void in(P& p, Q& q, R& r, S& s){in(p);in(q);in(r);in(s);}
template<typename P, typename Q, typename R, typename S, typename T> inline void in(P& p, Q& q, R& r, S& s, T& t){in(p);in(q);in(r);in(s);in(t);}


template<typename T> inline void inarr(int n, T* arr){fin in(arr[i]);}
template<typename T> inline int inarr(T* arr){int n=ini();inarr(n,arr);return n;}
template<typename T> inline void inarr(int n, vector<T>& arr){arr.resize(n);fin in(arr[i]);}
template<typename T> inline int inarr(vector<T>& arr){int n=ini();inarr(n,arr);return n;}

template<typename P, typename Q> inline void inarr(int n, P* arr1, Q* arr2){fin{in(arr1[i]);in(arr2[i]);}}
template<typename P, typename Q> inline int inarr(P* arr1, Q* arr2){int n=ini(); inarr(n,arr1,arr2); return n;}
template<typename P, typename Q> inline void inarr(int n, vector<P>& arr1, vector<Q>& arr2){arr1.resize(n);arr2.resize(n);fin{in(arr1[i]);in(arr2[i]);}}
template<typename P, typename Q> inline int inarr(vector<P>& arr1, vector<Q>& arr2){int n=ini(); inarr(n,arr1,arr2); return n;}

template<typename P, typename Q, typename R> inline void inarr(int n, P* arr1, Q* arr2, R* arr3){fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);}}
template<typename P, typename Q, typename R> inline int inarr(P* arr1, Q* arr2, R* arr3){int n=ini(); inarr(n,arr1,arr2,arr3); return n;}
template<typename P, typename Q, typename R> inline void inarr(int n, vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3){arr1.resize(n);arr2.resize(n);arr3.resize(n);fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);}}
template<typename P, typename Q, typename R> inline int inarr(vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3){int n=ini(); inarr(n,arr1,arr2,arr3); return n;}

template<typename P, typename Q, typename R, typename S> inline void inarr(int n, P* arr1, Q* arr2, R* arr3, S* arr4){fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);in(arr4[i]);}}
template<typename P, typename Q, typename R, typename S> inline int inarr(P* arr1, Q* arr2, R* arr3, S* arr4){int n=ini(); inarr(n,arr1,arr2,arr3,arr4); return n;}
template<typename P, typename Q, typename R, typename S> inline void inarr(int n, vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3, vector<S>& arr4){arr1.resize(n);arr2.resize(n);arr3.resize(n);arr4.resize(n);fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);in(arr4[i]);}}
template<typename P, typename Q, typename R, typename S> inline int inarr(vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3, vector<S>& arr4){int n=ini(); inarr(n,arr1,arr2,arr3,arr4); return n;}

template<typename P, typename Q, typename R, typename S, typename T> inline void inarr(int n, P* arr1, Q* arr2, R* arr3, S* arr4, T* arr5){fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);in(arr4[i]);in(arr5[i]);}}
template<typename P, typename Q, typename R, typename S, typename T> inline int inarr(P* arr1, Q* arr2, R* arr3, S* arr4, T* arr5){int n=ini(); inarr(n,arr1,arr2,arr3,arr4,arr5); return n;}
template<typename P, typename Q, typename R, typename S, typename T> inline void inarr(int n, vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3, vector<S>& arr4, vector<T>& arr5){arr1.resize(n);arr2.resize(n);arr3.resize(n);arr4.resize(n);arr5.resize(n);fin{in(arr1[i]);in(arr2[i]);in(arr3[i]);in(arr4[i]);in(arr5[i]);}}
template<typename P, typename Q, typename R, typename S, typename T> inline int inarr(vector<P>& arr1, vector<Q>& arr2, vector<R>& arr3, vector<S>& arr4, vector<T>& arr5){int n=ini(); inarr(n,arr1,arr2,arr3,arr4,arr5); return n;}


inline void out(int i){printf("%d", i);}
inline void out(float f){printf("%f", f);}
inline void out(double d){printf("%lf", d);}
inline void out(bint b){printf("%lld", b);}
inline void out(const string& s){printf("%s", s.c_str());}
inline void out(char c){printf("%c", c);}
inline void out(char* c){if(c[0]!=0)printf("%s", c);}
inline void out(const char* c){if(c[0]!=0) printf("%s", c);}

template<typename P, typename Q> inline void out(P p, Q q){out(p);out(q);}
template<typename P, typename Q, typename R> inline void out(P p, Q q, R r){out(p);out(q);out(r);}
template<typename P, typename Q, typename R, typename S> inline void out(P p, Q q, R r, S s){out(p);out(q);out(r);out(s);}
template<typename P, typename Q, typename R, typename S, typename T> inline void out(P p, Q q, R r, S s, T t){out(p);out(q);out(r);out(s);out(t);}


char* tupledelim = " ";
char* tuplebegin = "";
char* tupleend = "";

template<typename P, typename Q> inline void out(const tuple<P,Q>& t){out(tuplebegin);out(t.g0);out(tupledelim);out(t.g1);out(tupleend);}
template<typename P, typename Q, typename R> inline void out(const tuple<P,Q,R>& t){out(tuplebegin);out(t.g0);out(tupledelim);out(t.g1);out(tupledelim);out(t.g2);out(tupleend);}
template<typename P, typename Q, typename R, typename S> inline void out(const tuple<P,Q,R,S>& t){out(tuplebegin);out(t.g0);out(tupledelim);out(t.g1);out(tupledelim);out(t.g2);out(tupledelim);out(t.g3);out(tupleend);}
template<typename P, typename Q, typename R, typename S, typename T> inline void out(const tuple<P,Q,R,S,T>& t){out(tuplebegin);out(t.g0);out(tupledelim);out(t.g1);out(tupledelim);out(t.g2);out(tupledelim);out(t.g3);out(tupledelim);out(t.g4);out(tupleend);}

template<typename P> void outarr(int n, P* arr, char* delim=" ", char* begin="", char* end=""){out(begin);bool first = true;fin{if(!first)out(delim);else first=false; out(arr[i]);}out(end);}
template<typename P> void outarr(vector<P>& arr, char* delim=" ", char* begin="", char* end=""){int n = arr.size(); out(begin);bool first = true;fin{if(!first)out(delim);else first=false; out(arr[i]);}out(end);}


#define tup make_tuple
typedef tuple<int,int> int2;
typedef tuple<int,int,int> int3;
typedef tuple<int,int,int,int> int4;

typedef vector<int> ivec;
typedef vector<char> cvec;
typedef vector<bool> bitvec;
typedef vector<string> svec;

#define struct2(className,type1,var1,type2,var2) struct className{type1 var1; type2 var2; className(type1 var1, type2 var2){this->var1=var1;this->var2=var2;}};
#define struct3(className,type1,var1,type2,var2,type3,var3) struct className{type1 var1; type2 var2; type3 var3; className(type1 var1, type2 var2, type3 var3){this->var1=var1;this->var2=var2;this->var3=var3;}};

template<typename P>
inline vector<P>& operator+=(vector<P>& v, const P& ele){
	v.push_back(ele);
}


#define hai int main(){
#define bye }
#define casework int main(){gint(v);FOR(i,v){printf("Case #%d: ",i+1);solve();}}
#define hello void solve(){
#define cya } casework

#define ent out("\n")

class Input{};
class Output{};
Input hin;
Output hout;

template<typename T> const Input& operator>>(const Input& input, T& t){in(t); return input;}
template<typename T> const Output& operator<<(const Output& output, T& t){out(t); return output;}

double epsilon = 10e-7;
bool equals(double a, double b){return abs(a-b)<epsilon;}

template<typename T> void infl(T& a, const T& b){if(b>a)a=b;}
template<typename T> void defl(T& a, const T& b){if(b<a)a=b;}

template<typename P, typename Q> inline const tuple<P,Q> operator+(const tuple<P,Q>& a, const tuple<P,Q>& b){return tup(a.g0+b.g0,a.g1+b.g1);}
template<typename P, typename Q, typename R> inline const tuple<P,Q,R> operator+(const tuple<P,Q,R>& a, const tuple<P,Q,R>& b){return tup(a.g0+b.g0,a.g1+b.g1,a.g2+b.g2);}
template<typename P, typename Q, typename R, typename S> inline const tuple<P,Q,R,S> operator+(const tuple<P,Q,R,S>& a, const tuple<P,Q,R,S>& b){return tup(a.g0+b.g0,a.g1+b.g1,a.g2+b.g2,a.g3+b.g3);}
template<typename P, typename Q, typename R, typename S, typename T> inline const tuple<P,Q,R,S,T> operator+(const tuple<P,Q,R,S,T>& a, const tuple<P,Q,R,S,T>& b){return tup(a.g0+b.g0,a.g1+b.g1,a.g2+b.g2,a.g3+b.g3,a.g4+b.g4);}

template<typename P, typename Q> inline const tuple<P,Q> operator-(const tuple<P,Q>& a, const tuple<P,Q>& b){return tup(a.g0-b.g0,a.g1-b.g1);}
template<typename P, typename Q, typename R> inline const tuple<P,Q,R> operator-(const tuple<P,Q,R>& a, const tuple<P,Q,R>& b){return tup(a.g0-b.g0,a.g1-b.g1,a.g2-b.g2);}
template<typename P, typename Q, typename R, typename S> inline const tuple<P,Q,R,S> operator-(const tuple<P,Q,R,S>& a, const tuple<P,Q,R,S>& b){return tup(a.g0-b.g0,a.g1-b.g1,a.g2-b.g2,a.g3-b.g3);}
template<typename P, typename Q, typename R, typename S, typename T> inline const tuple<P,Q,R,S,T> operator-(const tuple<P,Q,R,S,T>& a, const tuple<P,Q,R,S,T>& b){return tup(a.g0-b.g0,a.g1-b.g1,a.g2-b.g2,a.g3-b.g3,a.g4-b.g4);}

template<typename P> inline const P dot(const tuple<P,P>& a, const tuple<P,P>& b){return a.g0*b.g0+a.g1*b.g1;}
template<typename P> inline const P dot(const tuple<P,P,P>& a, const tuple<P,P,P>& b){return a.g0*b.g0+a.g1*b.g1+a.g2*b.g2;}

template<typename P, typename Q, typename X> inline const tuple<P,Q> operator*(const tuple<P,Q>& a, const X& b){return tup(a.g0*b,a.g1*b);}
template<typename P, typename Q, typename R, typename X> inline const tuple<P,Q,R> operator*(const tuple<P,Q,R>& a, const X& b){return tup(a.g0*b,a.g1*b,a.g2*b);}
template<typename P, typename Q, typename R, typename S, typename X> inline const tuple<P,Q,R,S> operator*(const tuple<P,Q,R,S>& a, const X& b){return tup(a.g0*b,a.g1*b,a.g2*b,a.g3*b);}
template<typename P, typename Q, typename R, typename S, typename T, typename X> inline const tuple<P,Q,R,S,T> operator*(const tuple<P,Q,R,S,T>& a, const X& b){return tup(a.g0*b,a.g1*b,a.g2*b,a.g3*b,a.g4*b);}

template<typename P, typename Q, typename X> inline const tuple<P,Q> operator*(const X& b, const tuple<P,Q>& a){return tup(a.g0*b,a.g1*b);}
template<typename P, typename Q, typename R, typename X> inline const tuple<P,Q,R> operator*(const X& b, const tuple<P,Q,R>& a){return tup(a.g0*b,a.g1*b,a.g2*b);}
template<typename P, typename Q, typename R, typename S, typename X> inline const tuple<P,Q,R,S> operator*(const X& b, const tuple<P,Q,R,S>& a){return tup(a.g0*b,a.g1*b,a.g2*b,a.g3*b);}
template<typename P, typename Q, typename R, typename S, typename T, typename X> inline const tuple<P,Q,R,S,T> operator*(const X& b, const tuple<P,Q,R,S,T>& a){return tup(a.g0*b,a.g1*b,a.g2*b,a.g3*b,a.g4*b);}

template<typename P> inline vector<P> array(P a){vector<P> v;v+=a;return v;}
template<typename P> inline vector<P> array(P a,P b){vector<P> v;v+=a;v+=b;return v;}
template<typename P> inline vector<P> array(P a,P b,P c){vector<P> v;v+=a;v+=b;v+=c;return v;}
template<typename P> inline vector<P> array(P a,P b,P c,P d){vector<P> v;v+=a;v+=b;v+=c;v+=d;return v;}



#endif
