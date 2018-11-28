#include <iostream>
#include <vector>
using namespace std;

int borne = 100003;

vector<vector<int> > res;
vector<vector<bool> > set;

int binom(int n, int k) {
	if (k == 0) return 1;
	return n * binom (n-1,k-1) / k;
}

int pure (int v, int r) {
	int k, accu = 0;
	if (r == 1) return 1;
	if (set[v][r]) return res[v][r];
	for (k = 1; k < r; ++k) {
		accu += binom(v - r - 1, r - k - 1) * pure(r, k);
		accu %= borne;
	}
	res[v][r] = accu;
	set[v][r] = true;
	return accu;
}

int main(void) {
	int t,n,i,num,accu;
	set.resize(501, vector<bool> (501, false));
	res.resize(501, vector<int> (501, 0));
	for (cin >> t, num = 1; num <= t; ++num) {
		cin >> n;
		accu = 0;
		for (i = 1; i < n; ++i) {
			accu += pure(n,i);
			accu %= borne;
		}
		cout << "Case #" << num << ": " << accu << endl;
	}
}
