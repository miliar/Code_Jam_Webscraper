#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
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

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


const int BIGG = 12345678;

vector<int> compatible[11][1500];
int bitcount[1500];
void gen_compat()
{
  FOR(i, 1024) {
    bitcount[i] = 0;
    FOR(j, 10) if(i & (1 << j)) bitcount[i]++;
  }

  FOR(i, 11) FOR(j, 1500) compatible[i][j].clear();
  for(int num = 1; num <= 10; num++) {
    bool curplace[num];
    FOR(mask, (1 << num)) {
      FOR(i, num) curplace[i] = (mask & (1 << i));
      bool good = true;
      FOR(i, num - 1) if(curplace[i] && curplace[i+1]) {
	//	if(num == 3) cerr << " bad " << mask << endl;
	good = false;
	break;
      }
      if(good) {
	//	if(num == 3) cerr << mask << endl;
	FOR(numask, (1 << num)) {
	  bool g = true;
	  FOR(i, num) {
	    if(i > 0 && curplace[i] && (numask & (1 << (i-1)))) {
	      g = false;
	      break;
	    }
	    if(i < num - 1 && curplace[i] && (numask & (1 << (i+1)))) {
	      g = false;
	      break;
	    }
	  }
	  if(g) {
	    compatible[num][mask].pb(numask);
	    //  cerr << num << ' ' << mask << ' ' << numask << endl;
	  }
	}
      }
    }
  }
}    

int main()
{

  gen_compat();
  int tests;
  cin >> tests;
  //  cerr << tests;
  FOT(_t, 1, tests+1) {
    int M, N;
    // cerr << ":::::::" << _t << endl;
    cin >> M >> N;
    //  cerr << "::::" << M << ' ' << N << endl;
    bool desk[M][N];
    FOR(i, M) FOR(j, N) desk[i][j] = true;
    char cc;
    FOR(i, M) {
      FOR(j, N) {
	cin >> cc;
	desk[i][j] = (cc == '.');
      }
    }
    
    int oldans[1024], nuans[1024];

    FOR(i, (1 << N)) oldans[i] = 0;

    FOR(i, M) {
      FOR(tt, (1 << N)) nuans[tt] = 0;
      FOR(mask, (1 << N)) {
	bool good = (compatible[N][mask].size() > 0);
	if(good) {
	  FOR(j, N) if((mask & (1 << j)) && !desk[i][j]) {
	    good = false;
	    break;
	  }
	}
	if(good) {
	  FOR(j, compatible[N][mask].size()) {
	    nuans[mask] = max(nuans[mask], oldans[compatible[N][mask][j]]);
	  }
	  nuans[mask] += bitcount[mask];
	}
      }
      FOR(tt, (1 << N)) oldans[tt] = nuans[tt];
    }
    int ret = 0;
    FOR(i, (1 << N)) ret = max(ret, oldans[i]);
    cout << "Case #" << _t << ": " << ret << endl;
    //    FOR(i, 8)       FOR(j, compatible[3][i].size())      cerr << i << ' ' << j << endl;
    //    return 0;
  }
  return 0;
}
