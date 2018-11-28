#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT,N;
char R[150];
int W[150],ET[150];

void computenext(char r, int w){
  int nx = w+1;
  while(nx < N && R[nx] != r)nx++;
  if (nx >= N) return;
  if (w > -1){ ET[nx] = ET[w] + abs(W[w] - W[nx]) + 1; }
  else{ ET[nx] = W[nx]; }
}

int main(){
  cin >> TT;
  FOR(tt,TT){
    cin >> N;
    FOR(i,N){
      cin >> R[i] >> W[i];
    }
    computenext('O',-1);
    computenext('B',-1);
    int ct = 0;
    FOR(w,N){
      ET[w] = MAX(ET[w],ct);
      ct = ET[w]+1;
//      cout << w << ", " << ct << endl;
      computenext(R[w],w);
    }
    cout << "Case #" << (tt+1) << ": " << ET[N-1] << endl;
  }
}
