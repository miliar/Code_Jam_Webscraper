#include <iostream>
#include <cstdlib>
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

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT;
LL N,K;

int main(){
  cin >> TT;
  FOR(tt,TT){
    scanf("%Ld %Ld ",&N,&K);
    K%=(1<<N);
    if ( K != (1<<N)-1  ){ cout << "Case #" << (tt+1) << ": OFF" << endl;}
    else{ cout << "Case #" << (tt+1) << ": ON" << endl; }
  }
  return 0;
}
