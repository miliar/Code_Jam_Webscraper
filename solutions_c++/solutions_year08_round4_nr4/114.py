#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;

#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

int main(int argc, char **argv) {
	COND = argc >= 2 && argv[1][0] == 'q';
	int C; cin >> C;
	FOR (my, 1, C) {
	  int k; cin >> k;
	  string str;
	  cin >> str;
	  VV<int> PR;
	  REP (i, k) PR.PB(i);

	  int ret = (int)1e9;
	  do {
	    int last = -1;
	    int cost = 0;
	    REP (bl, str.size() / k) {
	      string tmp;
	      REP (i, k) tmp.PB(str[bl * k + PR[i]]);
	      if (tmp[0] != last) cost++;
	      REP (i, k - 1) cost += tmp[i] != tmp[i + 1];
	      last = tmp[k - 1];
	    }

	    ret = min(ret, cost);
	  }
	  while (next_permutation(ALL(PR)));
	  printf("Case #%d: %d\n", my, ret);
	}
	return 0;
}
