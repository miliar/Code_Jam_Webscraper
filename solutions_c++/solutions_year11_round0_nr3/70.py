#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define all(x) x.begin() , x.end()

#define N 1024
int n, v[N];

long long soma(long long a, long long b) {
	int s = 0;
	FOR(i,31) {
		if( (a & (1ll<<i)) + (b & (1ll<<i)) == (1ll<<i) ) s += (1ll<<i);
	}
	return s;
}

int solve_brute() {
	int ans = -1;
	FOR(i, (1<<n)) {
		long long a = 0, b = 0;
		int l1 = 0, l2 = 0;
		FOR(j, n) {
			if(i & (1<<j)) {
				a = soma(a, v[j]);
				l1 += v[j];
			} else {
				b = soma(b, v[j]);
				l2 += v[j];
			}
		}
		if(a == b && l1 && l2) ans = max(ans, max(l1,l2));
	}
	if(ans == -1) cout << "NO\n";
	else cout << ans << endl;
	return ans;
}

int solve_smart() {
	int ans = -1;
	sort(v, v+n);
	long long a = 0, sum = 0;
	FOR(i, n) {
		a = soma(a, v[i]);
		sum += v[i];
	}
	if(a == 0 && n >= 2) {
		ans = sum - v[0];
	}
	if(ans == -1) cout << "NO\n";
	else cout << ans << endl;
	return ans;
}



int main() {
	int T;
	cin >> T;
	for(int teste = 1; teste <= T; teste++) {
		printf("Case #%d: ", teste);
		scanf("%d", &n);
		FOR(i,n) cin >> v[i];

		solve_smart();
		//if(solve_brute() != solve_smart()) { cout << ">>>>EERRROOO>>>\n"; break; }

	}

    return 0;
}

