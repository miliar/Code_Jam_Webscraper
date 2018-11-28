#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int MAXN = 1000;

typedef pair<int, int> PII;

int sums[MAXN + 1];
int len[MAXN];

int main() {
	int caseNum;
	cin >> caseNum;
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int limit, n, cycle;
		long long buildTime;
		cin >> limit >> buildTime >> n >>  cycle;
		sums[0] = 0;
		for (int i = 0; i < cycle; i++) {
			cin >> len[i];
			sums[i + 1] = sums[i] + len[i];
		}
		long long preCycle = buildTime / sums[cycle] / 2;
		int cycStart;
		for (cycStart = 0; preCycle * sums[cycle] * 2 + sums[cycStart] * 2 < buildTime; cycStart++);
		long long preRemain = (preCycle * sums[cycle] * 2 + sums[cycStart] * 2 - buildTime) / 2;
		int end = n % cycle;
		long long ans = 2 * ((long long) sums[cycle] * (n / cycle) + sums[end]);
		if (limit == 0 || preCycle * cycle + cycStart - (preRemain != 0 ? 1 : 0) >= n) {
			// No speed up
		} else if (limit >= 1 && preCycle * cycle + cycStart == n) {
			ans -= preRemain;
		} else {
			vector<PII> dec;
			dec.reserve(cycle);
			for (int i = 0; i < cycle; i++) {
				int cur = (n / cycle) - preCycle - 1;
				if (i >= cycStart) {
					cur++;
				}
				if (i < end) {
					cur++;
				}
				if (cur > 0) {
					dec.push_back(PII(len[i], cur));
				}
			}
			if (preRemain > 0) {
				dec.push_back(PII(preRemain, 1));
			}
			sort(dec.begin(), dec.end());
			int remain = limit;
			for (int i = dec.size() - 1; i >= 0 && remain > 0; i--) {
				if (dec[i].second <= limit) {
					remain -= dec[i].second;
					ans -= (long long) dec[i].first * dec[i].second;
				} else {
					ans -= (long long) dec[i].first * remain;
					remain = 0;
				}
			}
		}
		cout << "Case #" << caseIndex << ": " << ans << endl;
	}
	
	return 0;
}
