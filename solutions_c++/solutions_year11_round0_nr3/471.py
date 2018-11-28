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

const int OMAX = 1048576;
int max_value[OMAX];

void solve(int testnum) {
	int n;
	cin >> n;
	vector<int> c(n);
	for (int i = 0; i < n; ++i) cin >> c[i];
	int sum = 0;
	for (int i = 0; i < n; ++i) sum ^= c[i];
	cout << "Case #" << testnum << ": ";
	if (sum != 0)
		cout << "NO" << endl;
	else {
		int m = c[0];
		for (int i = 0; i < n; ++i) if (c[i] < m) m = c[i];
		m *= -1;
		for (int i = 0; i < n; ++i) m += c[i];
		cout << m << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {cerr << "Case " << i + 1 << endl; solve(i + 1);}
}
