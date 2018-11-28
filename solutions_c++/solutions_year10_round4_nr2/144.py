#include<cstdio>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<sstream>
#include<cassert>
#include<complex>

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) v.begin() , v.end()
#define set(x, with) memset(x , with , sizeof(x))
#define same(a,b) (fabs((a)-(b))<0.000000001)
#define even(a) ((a) % 2 == 0)
#define odd(a) ((a) % 2 == 1)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int , int> ii;
typedef complex<int> pnt;

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

void init(void);
int process(int, vi);
void out(int);

const int pn = 4;
const pnt pv[pn] = {
	pnt (0 , -1),
	pnt (0 , 1),
	pnt (-1 , 0),
	pnt (1 , 0)
};

const int MaxN = 1024;
const int MaxW = 10;
const int MaxP = 10;
map<vi, int> Dy[MaxP + 1];
int Prices[MaxP + 1][MaxN + 1];
int M[MaxN + 1];
int N, P;
int Ans;

vi mk(int s, int e, int wm){
  vi ret;
  ret.pb(s);
  ret.pb(e);
  ret.pb(wm);
  return ret;
}

int main(void){
  int K;
  cin >> K;
  FOR(i, 1, K){
  	init();
    vi start = mk(0, N-1, 0);
  	Ans = Dy[0][start] = process(0, start);
  	out(i);
  }
	return 0;
}

void init(void){
  cin >> P;
  N = (1<<P);
  FOR(i, 0, (1<<P)-1){
    cin >> M[i];
    M[i] = min(M[i], P);
  }
  FOR(i, 0, MaxP){
    Dy[i].clear();
  }
  FORD(i, P-1, 0){
    FOR(j, 0, (1<<i)-1){
      cin >> Prices[i][j];
    }
  }
}

int process(int r, vi p){
  int ret = INT_MAX;
  if(r == P){
    int i = p[0];
    //p[0] == p[1];
    if(p[2] <= M[i]){
      ret = 0;
    }    
  } else if(Dy[r].find(p) != Dy[r].end()){
    ret = Dy[r][p];
  } else{
    int s = p[0];
    int e = p[1];
    int wm = p[2];
    int mid = (s + e) >> 1;
    //buy
    {
      vi p1 = mk(s, mid, wm);
      int r1 = process(r+1, p1);
      vi p2 = mk(mid+1, e, wm);
      int r2 = process(r+1, p2);
      if(r1 != INT_MAX && r2 != INT_MAX){
        int p = Prices[r][s / (1<<(P-r))];
        ret = min(ret, r1+r2+p);
      }
    }
    //not
    {
      vi p1 = mk(s, mid, wm+1);
      int r1 = process(r+1, p1);
      vi p2 = mk(mid+1, e, wm+1);
      int r2 = process(r+1, p2);
      if(r1 != INT_MAX && r2 != INT_MAX){
        int p = 0;
        ret = min(ret, r1+r2+p);
      }
    }
  }
  Dy[r][p] = ret;
  return ret;
}

void out(int cn){
  printf("Case #%d: %d\n", cn, Ans);
}
