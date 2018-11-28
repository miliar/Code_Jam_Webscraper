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
#define EPS 10e-9
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;} 
inline LL MIN(LL a, LL b){ return a < b ? a : b;} 

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

VI V;
int TT;
int C,D;

double over(double maxposun){
  double mimi = -1000000000;
  FOR(i,V.size()){
    if (mimi > V[i]){
      if (mimi - V[i] > maxposun) return false;
      mimi = mimi + D;
    }else{
      if (V[i] - mimi < maxposun){ mimi = mimi + D; }
      else{ mimi = V[i] - maxposun + D;  }
    }
  }
  return true;
}


int main(){
  scanf("%d ",&TT);
  FOR(tt,TT){
    double lo = 0.0;
    double hi = 1000000000;
    scanf("%d %d ",&C,&D);
    V.resize(0);
    FOR(i,C){
      int x,y;
      scanf("%d %d ",&x,&y);
      FOR(j,y) V.PB(x);
    }
    while( fabs(hi-lo) > EPS){
      double mi = (hi+lo)/2;
  //    printf("uverujem %lf\n",mi);
      if (over(mi)){
        hi = mi;
      }else{
        lo = mi;
      }
    }
    printf("Case #%d: %lf\n",tt+1,hi);
  }
}
