#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T a) {return a > 0 ? a : (-a); }
template<class T> T sqr(T a) {return a * a; }

using namespace std;

void solve(int testnum) {
	int n;
	cin >> n;
	double ans = 0;
	for (int i = 0; i < n; ++i) {
		int a;
		cin >> a;
		if (a != i + 1) ans += 1.0;
	}
	printf("Case #%d: %.10lf\n", testnum, ans);
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {cerr << "Test " << i + 1 << endl; solve(i + 1);}
}
