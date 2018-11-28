#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int dp(int v, int d) {

}

int main () {
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++) {
		long long int N, acc = 0, tmp, sum = 0;
		cin >> N;
		vector<long long int> val;
		for(int i = 0;i < N; i++) {
			cin >> tmp;
			val.push_back(tmp);
			acc ^= tmp;
			sum+= tmp;
		}
		if(acc != 0) {
			printf("Case #%d: NO\n", caso);
			continue;
		}
		sort(val.begin(),val.end());
		printf("Case #%d: %lld\n", caso, sum-val[0]);
	}
	return 0;
}

