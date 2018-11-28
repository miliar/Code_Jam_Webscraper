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
#include <sstream>
#include <cstring>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

vector<int> mat[50];

	int n;

bool ok(int i, int j) {
	bool re = 1;
	rep (k, n) {
		if (k > i && mat[j][k]) re = 0;
	}
	return re;
}

void solve() {
	scanf("%d", &n);
	db(n);
	rep (i, 50) mat[i] = vector<int>(50);
	int ret = 0;
	rep (i, n) rep (j, n) {
		char x = 0;
	       	scanf(" %c", &x);
		mat[i][j] = x - '0';
		db(i<<" "<<j<<" "<<x);
	}
	rep (i, n) {
		if (ok(i,i) == 0) {
			db(i);
			fo (j, i + 1, n - 1) if (ok(i, j)) {
				ford (g, j - 1, i) { 
					swap(mat[g], 
							mat[g+1]); ret++; }
				break;
			}
		}
	}



	printf("%d", ret);
}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);
    cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
    int t;
    scanf("%d", &t);
    fo (i, 1, t) {
	    printf("Case #%d: ", i);
	    solve();
	    printf("\n");
    }
    return 0;
}

