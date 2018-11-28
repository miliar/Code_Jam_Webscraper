#include <iostream>
#include <vector>
#include <climits>
using namespace std;

vector<vector<vector<int> > > t;

int solve(int l, int p, int c) {
	int i, accu = INT_MAX;
	if (t[c-2][l][p] != -1) return t[c-2][l][p];
	if (l*c >= p) return 0;
	for (i = l+1; i < p; ++i)
		accu = min(accu, max(solve(i,p,c), solve(l,i,c)));
	t[c-2][l][p] = accu + 1;
	return accu + 1;
}

int main(void) {
	int nt,l,p,c,n;
	t.resize(9, vector<vector<int> > (1000,vector<int> (1001,-1)));
	for(cin >> nt, n=1; n <= nt; ++n) {
		cin >> l >> p >> c;
		cout << "Case #" << n << ": " << solve(l,p,c) << endl;
	}
}
