#include <iostream>
#include <vector>

using namespace std;

int R,K,N;
const int SCALE = 1001;
long long a[SCALE];
long long index[SCALE];
long long status[SCALE];

long long Solve() {
	long long ans = 0;
	memset(index,-1,sizeof(index));
	long long cur = 0;
	long long time = 0;
	while (index[cur] == -1 && time < R) {
		index[cur] = time;
		status[cur] = ans;
		++time;
		long long num = 0;
		long long take = 0;
		// cout << "time:" << time << endl;
		while (num < N && take + a[cur] <= K) {
			// cout << a[cur] << " ";
			take += a[cur];
			cur = (cur + 1)%N;
			++num;
		}
		// cout << endl;
		ans += take;
	}
	if (time == R) {
		return ans;
	}
	long long cycle_step = time - index[cur];
	long long cycle_sum = ans - status[cur];
	R -= time;
	ans += cycle_sum * (R/cycle_step);
	R %= cycle_step;

	time = 0;
	while (time < R) {
		++time;
		long long num = 0;
		long long take = 0;
		while (num < N && take + a[cur] <= K) {
			take += a[cur];
			cur = (cur + 1)%N;
			++num;
		}
		ans += take;
	}
	return ans;
}

int main() {
	// freopen("in.txt","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	while (cin >> t) {
		for (int i = 0; i < t; ++i) {
			cin >> R >> K >> N;
			for (int j = 0; j < N; ++j) {
				cin >> a[j];
			}
			cout << "Case #" << i + 1 << ": ";
			long long res = Solve();
			cout << res << endl;
		}
	}
}