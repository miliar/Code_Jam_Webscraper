#pragma warning (disable: 4530) 
#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
#include<climits>


#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;

typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0,1,1,-1,-1},dy[]={0,-1,0,1,1,-1,-1,1};//right down left up
int test,tx,ty;
string stage[4];
bool Inner(int x,int y){
  return 0 <= x && x < 4 && 0 <= y && y < 4;
}
bool Win(char p){
  if(ty != -1 && tx != -1)
    stage[ty][tx] = p;
  rep(y,4){
    rep(x,4){
      rep(d,8){
	int nx = x,ny = y;
	bool four = true;
	rep(s,4){
	  four &= (Inner(nx,ny) && stage[ny][nx] == p);
	  nx += dx[d];
	  ny += dy[d];
	}
	if(four) return true;
      }
    }
  }
  return false;
}
int main(){
  scanf("%d",&test);
  rep(t,test){
    ty = -1,tx = -1;
    rep(y,4) cin>>stage[y];
    bool comp = true;
    rep(y,4){
      rep(x,4){
	if(stage[y][x] == '.')
	  comp = false;
	if(stage[y][x] == 'T')
	  ty = y,tx = x;
      }
    }
    printf("Case #%d: ",t + 1);
    if(Win('X')) printf("X won\n");
    else if(Win('O')) printf("O won\n");
    else if(comp) printf("Draw\n");
    else printf("Game has not completed\n");
  }
}
