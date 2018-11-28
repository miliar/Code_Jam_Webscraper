#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef long long ll;
typedef stringstream ss;

#define sz(v)		((int) v.size())
#define fv(v, i)	for (int i = 0; i < sz(v); ++i)
#define fn(n, i)	for (int i = 0; i < n; ++i)

#define FILENAME	"A-large"

int l[10240], d[10240], x[10240];

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {

		int N, D;
		in >> N;
		fn(N, i) {
			in >> d[i] >> l[i];
		}
		in >> D;
		d[N] = D;
		l[N] = 0;

		memset(x, 0xff, sizeof(x));
		x[0] = d[0];
		fn(N, i) {
			if (x[i] == -1) continue;
			for(int j = i + 1; j <= N && d[j] <= d[i] + x[i]; ++j) {
				x[j] = max(x[j], min(l[j], d[j]-d[i]));
			}
		}

		cout << "Case #" << test << ": " << (x[N] == -1 ? "NO" : "YES");
		cout << endl;

		out << "Case #" << test << ": " << (x[N] == -1 ? "NO" : "YES");
		out << endl;
	}

	return 0;
}