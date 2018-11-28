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

const int MaxR = 150;
int R;
string Input[MaxR + 1];
int Matrix[MaxR + 1][MaxR + 1];
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
  cin >> R;
  getline(cin, Input[0]);
  FOR(i, 0, 2 * R - 1 - 1){
    getline(cin, Input[i]);
  }
  //transform
  int sj = R-1;
  FOR(i, 0, R-1){
    int ii = i;
    int jj = sj;
    FORD(j, R-1, 0){
      Matrix[i][j] = Input[ii][jj] - '0';
      ii++;
      jj--;
    }
    sj++;
  }
  Ans = INT_MAX;
}

void process(void){
  if(R <= 1){
    Ans = 0;
  } else{
    FOR(R2, R, R*4){//size
//    FOR(R2, 6,6){//size
      //where to put
      if(R2 * R2 - R * R >= Ans) break;
      FOR(sy, 0, R2-R){
         FOR(sx, 0, R2-R){
          int Base = R2 * R2 - R * R;
          if(Base >= Ans) break;
          //starting from sy, sx
          FOR(y, sy, sy+R-1){
            FOR(x, sx, sx+R-1){
              //dig1
              {
                //x+y+xx+yy == 2*(R2-1)
                //x-y==xx-yy
                int yy = R2-1-x;
                int xx = R2-1-y;
                if(sy <= yy && yy <= sy + R - 1){
                  if(sx <= xx && xx <= sx + R - 1){
                    if(Matrix[y - sy][x - sx] != Matrix[yy - sy][xx - sx]){
                      Base = INT_MAX;
                      break;
                    }
                  }
                }
              }
              //dig2
              {
                //x-y+xx-yy=0
                //x+y=xx+yy
                int xx = y;
                int yy = x;
                if(sy <= yy && yy <= sy + R - 1){
                  if(sx <= xx && xx <= sx + R - 1){
//                    cerr << y << ' ' << x << ' ' << yy << ' ' << xx << endl;
                    if(Matrix[y - sy][x - sx] != Matrix[yy - sy][xx - sx]){
                      Base = INT_MAX;
                      break;
                    }
                  }
                }
              }
            }
            if(Base == INT_MAX) break;
          }
          Ans = min(Ans, Base);
        }
      }
    }
  }
}

void out(int cn){
  printf("Case #%d: %d\n", cn, Ans);
}
