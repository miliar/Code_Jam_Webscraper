#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int main() {
  int tests;
  cin >> tests;
  FOT(t, 1, tests+1) {
    int n, K;
    cin >> n >> K;
    int price[n][K];
    FOR(i, n) FOR(j, K) cin >> price[i][j];
    
    bool edge[n][n];
    FOR(i, n) FOR(j, n) edge[i][j] = false;
    FOR(i, n) FOR(j, n) {
      if(i != j)
	FOR(k, K - 1)
	  if((ll(price[i][k]-price[j][k]) * ll(price[i][k+1]-price[j][k+1])) <= 0)
	    edge[i][j] = true;
      //      if(edge[i][j]) cerr << i << ' ' << j << endl;
    }
    
    int m = (1 << n);
    bool ind[m]; FOR(i, m) ind[i] = false;
    ind[0] = true;
    FOT(i, 1, m)
      if(ind[i&(i-1)]) {
	int what = 0;
	ind[i] = true;
	FOR(j, n) if(i & (1 << j)) {
	  what = j;
	  break;
	}
	FOR(j, n) if(i & (1 << j)) if(j != what) {
	    //	    if(i == 3 && edge[what][j]) cerr << "santoheu " << what << ' ' << j << endl;
	    ind[i] = ind[i] && (!edge[what][j]);
	  }
	//	if(ind[i]) cerr << i << endl;
      }
    vi maxi;
    
    FOR(i, m) {
      bool good = ind[i];
      //      if(good) cerr << i << ':';
      FOR(j, n) if(((i ^ (1 << j)) > i ) && (ind[i^(1<<j)])) good = false;
      if(good) maxi.pb(i);
      //      if(ind[i]) cerr << endl;
    }

    int best[m];
    FOR(i, m) best[i] = n;
    best[0] = 0;
    FOT(i, 1, m) {
      FOR(j, s(maxi)) {
	best[i] = min(best[i], 1 + best[i - (i & maxi[j])]);
      }
    }

    


    cout << "Case #" << t << ": " << best[m-1] << endl;
  }
  return 0;
}
