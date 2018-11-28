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
#define mk make_pair
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
void process(void);
void out(int);

const int pn = 4;
const pnt pv[pn] = {
	pnt (0 , -1),
	pnt (0 , 1),
	pnt (-1 , 0),
	pnt (1 , 0)
};

set<ii> Bac;
int Ans;

int main(void){
  int K;
  cin >> K;
  FOR(i, 1, K){
  	init();
  	process();
  	out(i);
  }
	return 0;
}

void init(void){
  Ans = 0;
  int R;
  cin >> R;
  FOR(i, 1, R){
    int sx, sy, ex, ey;
    cin >> sx >> sy >> ex >> ey;
    FOR(y, sy, ey){
      FOR(x, sx, ex){
        Bac.insert(mk(y,x));
      }
    }
  }
}

void process(void){
  while(Bac.size()){
    Ans++;
    set<ii> newBac;
    for(set<ii>::iterator it = Bac.begin(), endIt = Bac.end(); it != endIt; it++){
      ii yx = *it;
      int y = yx.first;
      int x = yx.second;
      {//survive
        if(Bac.find(mk(y-1,x)) != Bac.end() || Bac.find(mk(y,x-1)) != Bac.end()){
          newBac.insert(yx);
        }
      }
      {//north
        if(Bac.find(mk(y+1,x-1)) != Bac.end()){
          newBac.insert(mk(y+1,x));
        }
      }
      {//west
        if(Bac.find(mk(y-1,x+1)) != Bac.end()){
          newBac.insert(mk(y,x+1));
        }
      }
    }
    Bac = newBac;
  }
}

void out(int cn){
  printf("Case #%d: %d\n", cn, Ans);
}
