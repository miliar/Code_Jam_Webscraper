#include <iostream>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <queue>
#include <string>

#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x)

using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef string::iterator si;

typedef unsigned long long ull;
typedef long long ll;

//const long long inf = (1LL <<60) + 0x3c;
const int inf = (1 <<30) + 0x3c;

void read_tt(int cnt, vector<int> *arr, vector<int> *dep) {
	for(int i = 0; i < cnt; ++i) {
		int shr, smn, ghr, gmn;
		scanf("%d:%d%d:%d", &shr, &smn, &ghr, &gmn);
		dep->push_back(shr * 60 + smn);
		arr->push_back(ghr * 60 + gmn);
	}
	sort(arr->begin(), arr->end());
	sort(dep->begin(), dep->end());
}

int count_train(const vector<int> &arr, const vector<int> &dep, const int T) {
	int ret = 0;
	F(it, dep) {
		if(distance(dep.begin(), it) >= distance(arr.begin(), upper_bound(arr.begin(), arr.end(), *it - T)) + ret)
			++ret;
	}
	return ret;
}

bool solve(int testcase) {
	int T;
	int NA, NB;
	if(scanf("%d", &T) != 1)
		assert(false);
	if(scanf("%d%d", &NA, &NB) != 2)
		assert(false);

	vector<int> aa, ba, ad, bd;
	read_tt(NA, &ba, &ad);
	read_tt(NB, &aa, &bd);

	int a = count_train(aa, ad, T);
	int b = count_train(ba, bd, T);

	printf("Case #%d: %d %d\n", testcase + 1, a, b);
	return true;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n && solve(i); ++i);
	return 0;
}
