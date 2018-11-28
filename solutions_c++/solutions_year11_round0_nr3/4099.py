//Sat May  7 14:27:19 CDT 2011
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

vector<int> vol;
int sum;

void init(int N) {
	vol.clear();
	int sum = 0;
	int number;
	for (int i = 0; i < N; i++) {
		cin >> number;
		sum += number;
		vol.push_back(number);
	}
	sort(vol.rbegin(), vol.rend());
}

int solve(int N) {
	int mmax = 0;
	for (int i = 1; i < (1 << N) - 1; i++) {
		int sum1 = 0;
		int sum2 = 0;
		int sum3 = 0;
		for (int j = 0; j < N; j++) {
			if ((1 << j) & i) {
				sum1 ^= vol[j];
				sum3 += vol[j];
			} else
				sum2 ^= vol[j];
		}
		if (sum1 == sum2)
			mmax = max(mmax, sum3);
	}
	return mmax;
}

int main(int argc, const char* argv[]) {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		init(n);
		int ret = solve(n);
		if (ret == 0)
			cout << "NO" << endl;
		else
			cout << ret << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
