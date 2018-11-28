#include <vector>
#include <iostream>
#include <cstdio>
using namespace std;

int main(void) {
	vector<double> v(1001);
	v[1] = 0.0;
	for (int i = 2; i <= 1000; i++) {
		v[i] = 1.0;
		for (int j = 1; j < i; j++) {
			v[i] += v[j] / j;
		}
		v[i] *= i / double(i - 1);
	}
	int T;
	cin >> T;
	for (int testNo = 1; testNo <= T; testNo++) {
		int N;
		cin >> N;
		vector<int> ar(N);
		for (int i = 0; i < N; i++) {
			cin >> ar[i];
			ar[i]--;
		}
		double res = 0.0;
		for (int i = 0; i < N; i++) {
			if (ar[i] == -1)
				continue;
			int cnt = 0;
			for (int j = i; ar[j] != -1; cnt++) {
				int nj = ar[j];
				ar[j] = -1;
				j = nj;
			}
			res += v[cnt];
		}
		printf("Case #%d: %.6lf\n", testNo, res);
	}
	return 0;
}
