#include <iostream>
#include <cstdio>

using namespace std;

int as[1010];
int used[1010];

int main() {
	int T;
	cin >> T;
	for(int TT = 1; TT <= T; ++TT) {
		int n;
		double res = 0;
		cin >> n;
		for(int i = 0; i < n; ++i) cin >> as[i];
		for(int i = 0; i < n; ++i) if(used[i] < TT) {
			int pos = as[i] - 1, num = 1;
			used[i] = TT;
			while(used[pos] < TT) {
				used[pos] = TT;
				++num;
				pos = as[pos] - 1;
			}
			if(num > 1) res += num;
		}
		printf("Case #%d: %.10f\n", TT, res);
	}
	return 0;
}
