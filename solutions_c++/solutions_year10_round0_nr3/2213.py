#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
ifstream in ("input.in");
ofstream out ("output.out");
long long solve (int R, int K, queue <int> &q) {
	long long ans = 0LL;
	for (int i=0; i<R; i++) {
		queue <int> tmp;
		int count = 0;
		while ((count < K) && (!q.empty())) {
			int val = q.front();
			if (count + val <= K) {
				tmp.push (val);
				count += val;
				q.pop();
			}
			else break;
		}
		ans += (long long)(count);
		while (!tmp.empty()) {
			int val = tmp.front();
			q.push (val);
			tmp.pop();
		}
	}
	return ans;
}
int main() {
	int T;
	in >> T;
	for (int i=0; i<T; i++) {
		int R, K, N, tmp;
		queue <int> q;
		in >> R >> K >> N;
		for (int j=0; j<N; j++) {
			in >> tmp;
			q.push (tmp);
		}
		out << "Case #" << i+1 << ": " << solve (R, K, q) << "\n";
	}
	return 0;
}