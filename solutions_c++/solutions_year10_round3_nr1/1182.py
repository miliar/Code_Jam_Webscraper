#include<iostream>
#include<utility>
#include<cstdio>
#include<complex>
#include<vector>

using namespace std;

#define EPS 10e-10

// 点
typedef complex<double> P;

// 線分・半直線・直線
struct L { P pos, dir; };
 
// 円
struct C { P p; double r; }; 

// 二つのベクトルの内積を計算する
inline double inp(const P& a, const P& b) {
    return (conj(a)*b).real();
}
 
// 二つのベクトルの外積を計算する
inline double outp(const P& a, const P& b) {
    return (conj(a)*b).imag();
}

bool ll_intersects(const L& l, const L& m) {
  return (abs(outp(l.dir, m.dir)) > EPS || abs(outp(l.dir, m.pos-l.pos)) < EPS);
}

P line_cross(const L& l, const L& m) {
    double num = outp(m.dir, m.pos-l.pos);
    double denom = outp(m.dir, l.dir);
    return P(l.pos + l.dir*num/denom);
}

bool sp_intersects(const L& s, const P& p) {
    return ( abs(s.pos - p) + abs(s.pos + s.dir - p) - abs(s.dir) < EPS );
}

int main(){
  int t;
  cin >> t;
  for(int xx=1;xx<=t;xx++){
    int a,b;
    vector<L> v;
    int y1,y2;
    int n; cin >> n;
    for(int i=0;i<n;i++){
      cin >> y1 >> y2;
      L a; a.pos=P(-1,y1); a.dir=P(2,y2-y1);
      v.push_back(a);
    }
    int ans=0;
    for(int i=0;i<n;i++){
      for(int j=i+1;j<n;j++){
	if(ll_intersects(v[i],v[j])){
	  if(sp_intersects(v[i],line_cross(v[i],v[j])))
	     ans++;
	}
      }
    }
    printf("Case #%d: ",xx);
    cout << ans << endl;
  }
  return 0;
}
