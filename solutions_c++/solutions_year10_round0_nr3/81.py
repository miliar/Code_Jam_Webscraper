#include <iostream>
using namespace std;

int main() {
	long long T;
	cin >> T;
	for (long long c = 1; c <= T; c++) {
		long long R, k, N;
		cin >> R >> k >> N;
		long long groups[N];
		long long sum = 0;
		for (long long i = 0; i < N; i++) {
			cin >> groups[i];
			sum += groups[i];
		}
		if (sum <= k) {
			cout << "Case #" << c << ": " << sum*R << endl;
			continue;
		}
		
		long long firstVisited[N+1], moneyMade[N+1], wasAt[N+1];
		for (long long i = 0; i < N; i++) firstVisited[i] = -1;
		long long curPos = 0, curBucks = 0;
		for (long long j = 0;; j++) {
			if (j == R) {
				cout << "Case #" << c << ": " << curBucks << endl;
				break;
			}
			if (firstVisited[curPos] >= 0) {
				cout << "Case #" << c << ": " << (curBucks-moneyMade[curPos])*((R-firstVisited[curPos])/(j-firstVisited[curPos]))+moneyMade[wasAt[(R-firstVisited[curPos])%(j-firstVisited[curPos])+firstVisited[curPos]]] << endl;
				break;
			}
			firstVisited[curPos] = j;
			moneyMade[curPos] = curBucks;
			wasAt[j] = curPos;
			
			long long space = k;
			while (groups[curPos] <= space) {
				space -= groups[curPos];
				curBucks += groups[curPos];
				curPos = (curPos+1)%N;
			}
		}
	}
	return 0;
}
