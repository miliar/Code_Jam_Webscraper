#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

typedef vector<int> vint;

ostream& operator<<(ostream& o, const vint& v)
{
	for (int i = 0; i < v.size(); ++i) {
		o << v[i] << " ";
	}return o;
}
static int dot(const vint& v1, const vint& v2)
{
	int rv = 0;
	for (int i = 0; i < v1.size(); ++i) {
		rv += v1[i] * v2[i];
	}
	return rv;
}

static int solve(vint& v1, vint& v2)
{
	int rv = INT_MAX;
	sort(v2.begin(), v2.end());
	do {
		rv = min(rv, dot(v1, v2));
	} while (next_permutation(v2.begin(), v2.end()));
	return rv;
}

int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int n;
		vint v[2];
		cin >> n;
		for (int i = 0; i < 2; ++i) {
			v[i].resize(n);
			for (int j = 0; j < n; ++j) {
				cin >> v[i][j];
			}
		}
		cout << "Case #" << (t+1) << ": " << solve(v[0], v[1]) << endl;
	}
	return 0;
}
