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

int main(){
  cin >> TT;
  FOR(tt,TT){
    int xorsum = 0;
    cin >> N;
    int sum = 0, lowest = 1000010;
    FOR(i,N){
      int x;
      cin >> x;
      lowest = MIN(lowest,x);
      sum += x;
      xorsum ^= x;
    }
    cout << "Case #" << (tt+1) << ": ";
    if (xorsum != 0){
      cout << "NO" << endl;
    }else{
      cout << sum-lowest << endl;
    }
  }
}
