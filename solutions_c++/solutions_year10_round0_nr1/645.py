#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

long long T, N, K;

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N >> K;
		if ((K + 1) % (1LL << N) == 0) {
			printf("Case #%d: ON\n",t);
		}	else {
			printf("Case #%d: OFF\n",t);
		}
	}
	return 0;
}
