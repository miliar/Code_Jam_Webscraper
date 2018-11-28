#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#include<string>
#include<sstream>
#include<numeric>
#include<cassert>

#define f first
#define s second
#define mp make_pair

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define rep(i,s,n) for(int i=(s); i<(int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define ALL(c) (c).begin(), (c).end()
#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))
#define print(x) printf("%d\n",x)

using namespace std;

typedef unsigned int uint;
typedef long long ll;

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};

int getInt(){
  int ret = 0,c;
  c = getchar();
  while(!isdigit(c)) c = getchar();
  while(isdigit(c)){
    ret *= 10;
    ret += c - '0';
    c = getchar();
  }
  return ret;
}

bool memo[1000 * 1000 + 10];

int main(){
  int T = getInt();

  REP(tt, T){
    int x = getInt();
    int s = getInt();
    int r = getInt();
    int t = getInt();
    int n = getInt();

    vector<pair<int, pair<int, int> > > w(n);

    REP(i, x) memo[i] = true;
    memo[x] = false;

    REP(i, n){
      w[i].s.f = getInt();
      w[i].s.s = getInt();
      w[i].f = getInt();

      for(int j = w[i].s.f; j < w[i].s.s; j++)
	memo[j] = false;
    }

    REP(i,x) if(memo[i]){
      int j = i;
      while(memo[j]) j++;
      w.push_back(mp(0, mp(i, j)));
      i = j;
    }

    sort(ALL(w));

    double remain = static_cast<double>(t);

    double ans = 0.0;

    REP(i, w.size()){
      double len = w[i].s.s - w[i].s.f;
      int sp  = w[i].f;

      double tm = len / (sp + r);

      if(tm <= remain){
	remain -= tm;
	ans += tm;
      }else{
	double len2 = len - (sp + r) * remain;
	ans += remain + len2 / (sp + s);
	remain = 0.0;
      }
    }
    
    printf("Case #%d: %.9f\n", tt+1, ans);
  }

  return 0;
}
