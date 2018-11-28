
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long LL;

void init(void) {
  // init_primes();
}

int table[10010];
int mini;
int maxi;

bool isOK(int len) {
  deque<int> cur;
  for(int i = mini; i <= maxi+1; ++i){
    if(table[i] < cur.size()){
      int diff = (int)cur.size() - table[i];
      REP(j, diff){
	if(i - cur.front() < len)
	  return false;
	cur.pop_front();
      }
    }else if(table[i] > cur.size()){
      int diff = table[i] - cur.size();
      REP(j, diff)
	cur.push_back(i);
    }
  }
  return true;
}

void solve(void) {
  int n;
  cin >> n;
  memset(table, 0, sizeof(table));
  mini = 10000;
  maxi = 1;
  REP(i, n){
    int v;
    cin >> v;
    table[v]++;
    mini = min(mini, v);
    maxi = max(maxi, v);
  }
  
  int upper = n;
  int lower = 0;
  
  {
    int last = -1;
    REP(i, maxi+2){
      if(table[i] > 0){
	if(last < 0)
	  last = i;
      }else{
	if(last >= 0){
	  upper = min(upper, i - last);
	  last = -1;
	}
	
      }
    }
  }
  
  while(lower < upper){
    int mid = (upper + lower + 1) / 2;
    if(isOK(mid)){
      lower = mid;
    }else{
      upper = mid - 1;
    }
  }
  cout << lower << endl;
}

/////////////////////////////////////////////////////////

int main() {
  init();
  int nCases;
  cin >> nCases;
  REP(iCase, nCases) {
    cout << "Case #" << (iCase+1) << ": ";
    solve();
  }
  
  return 0;
}
