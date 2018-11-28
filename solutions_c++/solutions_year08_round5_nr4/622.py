#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <ctype.h>
#include <math.h>
using namespace std;
typedef long long LL;
typedef long double LD;

#define VI vector<int>
#define VVI vector<VI>
#define VD vector<double>
#define VVD vector<VD>
#define VS vector<string>
#define VVS vector<VS>

#define PB push_back
#define MP make_pair
#define ALL(t) t.begin(),t.end()
#define Size(x) (int(x.size()))

#define FOR(i,n) for(int i=0,_n=int(n);i<_n;i++)
#define FORV(i,v) FOR(i,int((v).size()))
#define FORR(i,n) for(int i=int(n)-1;i>=0;i--)
#define FORRV(i,v) FORR(i,int((v).size()))
#define FOREACH(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();i++)

#define INF 1000000000
#define PI atan(1.0)*4.0;
#define EPS 1e-8

string getLine();
int getNum();

inline string i2s(int val);
inline string d2s(double val);
inline string c2s(char c);

inline int s2i(string s);
inline double s2d(string s);
inline char s2c(string s);

VS s2vs(string s, string separator, bool empty_string);
VI vs2vi(VS vs);
inline VI s2vi(string s, string separator);
inline VVS vs2vvs(VS vs, string separator);
inline VVI vs2vvi(VS vs, string separator);

int gcd(int x, int y);
LL gcd(LL x, LL y);



struct kraw
{ int x, y;
 kraw(int a,int b) { x=a; y=b; }
};

// ---- start
const int prime = 10007;

int t[ 200 ][ 200 ];
queue<kraw> S;
void solveCase(int xz) {
  int H, W, R;
  scanf("%d%d%d", &H, &W, &R);
  FOR(y, H)
   FOR(x,W)
    t[ y ][ x ] = 0;

  for(int x=0, r, c; x<R; x++)
  {
    scanf("%d%d", &r, &c);
    t[ r-1 ][ c-1 ] = -1;
  }

  while ( ! S.empty() )  S.pop();
  S.push(kraw(0,0));
  t[0][0] = 1;

  while ( !S.empty() )
  {
	  kraw w = S.front();
	  S.pop();
	  if( w.x >= W  ||  w.y >= H )  continue;
	  if( t[w.y+1][w.x+2] != -1 )
	  {
		  if(t[w.y+1][w.x+2] == 0)  S.push(kraw(w.x+2, w.y+1));
		  t[w.y+1][w.x+2] += t[w.y][w.x];
		  t[w.y+1][w.x+2] %= prime;
	  }
	  if( t[w.y+2][w.x+1] != -1 )
	  {
		  if(t[w.y+2][w.x+1] == 0)  S.push(kraw(w.x+1, w.y+2));
		  t[w.y+2][w.x+1] += t[w.y][w.x];
		  t[w.y+2][w.x+1] %= prime;
	  }
  }

  printf("Case #%d: %d\n", xz+1, t[H-1][W-1]);
}

// ---- stop


int main() {  //n * solveCase(caseNum)
  int N;
  scanf("%d", &N);
  FOR(cnum,N)
    solveCase(cnum);
  return 0;
}

