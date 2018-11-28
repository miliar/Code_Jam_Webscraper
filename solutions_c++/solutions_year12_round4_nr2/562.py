#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

unsigned long xor128(){
  static unsigned long x=123456789, y=362436069, z=521288629, w=88675123;
  unsigned long t;
  t=(x^(x<<11));
  x=y; y=z; z=w;
  return w=(w^(w>>19))^(t^(t>>8));
}
double frand(){
  return xor128()%10000000/static_cast<double>(10000000); 
}

struct ST{
  double x, y;
  double r;
};
bool operator<(const ST& a, const ST& b){
  return a.r > b.r;
}

double dist(const ST& a, const ST& b){
  return sqrt((a.x-b.x)*(a.x-b.x) +(a.y-b.y)*(a.y-b.y));
}

int N, W, L;
vector<ST> st;

void solve(){
  bool flg = true;;
  
  while(flg){
    flg = false;
    rep(i,st.size()){
      bool check = true;
      rep(j,st.size()){
        if(i==j) continue;
        if(dist(st[i], st[j])<st[i].r+st[j].r){
          check = false;
          break;
        }
      }
      if(!check){
        st[i].x = frand()*W;
        st[i].y = frand()*L;
        flg = true;
      }
    }
  }

  rep(i,st.size()){
    printf(" %.9lf %.9lf", st[i].x, st[i].y);
    //cout << " " << st[i].x << " " << st[i].y;
  }
  printf("\n");
  //cout << endl;
}


int main(){
  int T;
  cin >> T;

  int tmp;
  rep(t,T){
    st.clear();
    cin >> N >> W >> L;
    rep(i,N){
      cin >> tmp;
      st.push_back((ST){0.0,0.0,tmp});
    }
    printf("Case #%d:", t+1);
    //cout << "Case #" << t+1 << ":";
    solve();
  }
  
  return 0;
}
