#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

int k;
string s;
vector<int> perm;

int calc()
{
	int i, j;

	string ss = s;
	for (i=0; i<(int)s.length(); i+=k) {
		for (j=0; j<k; ++j) {
			ss[i+j] = s[i+perm[j]];
		}
	}

	int ans = 0;
	ss += ' ';
	int pre = 0;

	for (i=1; i<(int)ss.length(); ++i) {
		if (ss[i] != ss[pre]) {
			ans ++;
			pre = i;
		}
	}

	return ans;
}

int main(void)
{
	int N;
	cin >> N;


	for (int i=1; i<=N; ++i) {
		cin >> k;
		cin >> s;

		perm.clear();
		for (int j=0; j<k; ++j) {
			perm.push_back(j);
		}

		int ans = s.length();
		do {
			int t = calc();
			if (t < ans) ans = t;
		} while (next_permutation(perm.begin(), perm.end()));

		cout << "Case #" << i << ": " << ans << endl;
	}

	return 0;
}
