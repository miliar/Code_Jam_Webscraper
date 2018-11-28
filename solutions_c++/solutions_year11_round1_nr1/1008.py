#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}
template<typename Integer>
Integer GCD(Integer a, Integer b){
  if(!b)return a;
  else return GCD(b,a%b);
}

// 有理数型
struct Rational{
  int p,q;
  Rational():p(1),q(1){}
  Rational(int p, int q):p(p),q(q){}
 
  // 四則演算
  const Rational operator+(const Rational &t)const{
    Rational r; r.p = p * t.q + t.p * q; r.q = q*t.q; return r.Simplify();
  }
  const Rational operator-()const{
    Rational r(-p,q); return r.Simplify();
  }
  const Rational operator-(const Rational &t)const{
    return *this+(-t);
  }
  const Rational operator*(const Rational &t)const{
    Rational r(p*t.p,q*t.q);
    return r.Simplify();
  }
  const Rational operator/(const Rational &t)const{
    assert(t.p!=0); Rational r(t.q,t.p);
    return (*this) * r;
  }
 
  // 浮動小数点変換
  double toDouble()const{
    return double(p)/q;
  }
 
  // 比較演算子、若干遅くなる可能性あり
  bool operator<(const Rational &t)const{
    Rational a = *this; Rational b = t; a.Simplify(); b.Simplify();
    return a.p * b.q - a.q * b.p < 0;
  }
  bool operator==(const Rational &t)const{
    Rational a = *this; Rational b = t; a.Simplify(); b.Simplify();
    return a.p == b.p && a.q == b.q;
  }
  bool operator>(const Rational &t)const{
    Rational a = *this; Rational b = t; a.Simplify(); b.Simplify();
    return a.p * b.q - a.q * b.p > 0;
  }
 
  // 既約分数形への変換
  const Rational Simplify(){
    int r = GCD(abs(p),abs(q));
    p /= r;
    q /= r;
    return *this;
  }
};
 
int main(){
  int T;
  cin >> T;
  rep(i, T){
    cout << "Case #" << i+1 << ": ";
    lli N, PD, PG;
    cin >> N >> PD >> PG;
    bool ok = true;
    if(PD != 100 && PG == 100)ok = false;
    if(PD != 0 && PG == 0)ok = false;
    if(ok){
      lli d = 100 / GCD(PD, (lli)100);
      if(d > N)ok = false;
    }
    if(ok)cout << "Possible" << endl;
    else cout << "Broken" << endl;
  }
  return 0;
}
