// include {{{
#include <cstdio>
#include <iostream>
//#include <sstream>
#include <string>
#include <vector>
//#include <deque>
#include <stack>
#include <queue>
//#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <numeric>
//#include <complex>
// }}}
using namespace std;
// macro {{{
typedef long long ll;
typedef vector<int> vec;
typedef vector<vec> mat;
typedef pair<int,int> P;
#define rep(i,n) for(int i=0,_end=(n);i<_end;++i)
#define REP(i,j,k) for(int i=j,_end=(k);i<_end;++i)
//#define foreach(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define priority_queue_greater(T) priority_queue< T, vector<T>, greater<T> >
#define F .first
#define S .second
//test define...
#define D(x) #x<<"="<<(x)
#define DD(x) cout << #x << "=" << (x) << endl;
// }}}

int foo[][4] = {
  {0  , 1  , 2  , 3}  ,
  {4  , 5  , 6  , 7}  ,
  {8  , 9  , 10 , 11} ,
  {12 , 13 , 14 , 15} ,
  {0  , 4  , 8  , 12} ,
  {1  , 5  , 9  , 13} ,
  {2  , 6  , 10 , 14} ,
  {3  , 7  , 11 , 15} ,
  {0  , 5  , 10 , 15} ,
  {3  , 6  , 9  , 12}
};

int main(){
  int t;
  cin >> t;
  REP(times,1,t+1){
    vector<string> map(4);
    rep(i,4){ cin >> map[i]; }
    bool X = false, O = false, follow = false;

    rep(i,10){
      int x = 0, o = 0, t = 0;
      rep(j,4){
        int yy = foo[i][j] / 4;
        int xx = foo[i][j] % 4;
        //cout << "(" << yy << "," << xx << ") ";
        if( map[yy][xx] == 'X' ){ x++; }
        if( map[yy][xx] == 'O' ){ o++; }
        if( map[yy][xx] == 'T' ){ t++; }
      }
      //cout << x << o << t << endl;
      if( x == 4 || (x == 3 && t == 1) ){ X = true; }
      if( o == 4 || (o == 3 && t == 1) ){ O = true; }
    }

    rep(y,4)rep(x,4)if(map[y][x] == '.'){ follow = true; }

    cout << "Case #" << times << ": ";
    if( X ){
      cout << "X won" << endl;
    }else if( O ){
      cout << "O won" << endl;
    }else if( !follow ){
      cout << "Draw" << endl;
    }else{
      cout << "Game has not completed" << endl;
    }
  }
  return 0;
}


