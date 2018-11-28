#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1000;

int arr[MAXN];
long long sum[MAXN + 1];

int main() {
	int caseNum;
	cin >> caseNum;
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		long long run, cap;
		int n;
		cin >> run >> cap >> n;
		sum[0] = 0;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
			sum[i + 1] = sum[i] + arr[i];
		}
		cout << "Case #" << caseIndex << ": ";
		if (sum[n] <= cap) {
			cout << run * sum[n] << endl;
			continue;
		}
		int cur = 0;
		long long res = 0;
		while (run-- > 0) {
			if (sum[n] - sum[cur] <= cap) {
				int pos = upper_bound(sum, sum + n + 1, sum[cur] + cap - sum[n]) - sum - 1;
				res += sum[pos] + sum[n] - sum[cur];
				cur = pos;
			} else {
				int pos = upper_bound(sum + cur, sum + n + 1, sum[cur] + cap) - sum - 1;
				res += sum[pos] - sum[cur];
				cur = pos;
			}
		}
		cout << res << endl;
	}
	
	return 0;
}
