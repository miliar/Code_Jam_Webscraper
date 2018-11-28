#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

int visited[2000001];
int pows[] = { 10, 100, 1000, 10000, 100000, 1000000 };

int _A; int _B;

int process(int num) {
	int tot = 0;
	int dig = 6;
	for (int i = 0; i < 6; i++) {
		if (pows[i] >= num) {
			dig = i;
			break;
		}
	}
	//cout << "DIG: " << dig << "\n";
	for (int i = 0; i < dig; i++) {
		int m = num;
		int j = m % pows[i];
		m /= pows[i];
		m += j * pows[dig-i-1];
		if (m > _B) continue;
		if (m <= num) { visited[m] = 1; continue; }
		if (m >= _A && m <= _B && !visited[m]) {
			//cout << num << " and " << m << "\n";
			tot++;
		}
		if (m < 2000001) visited[m] = 1;
	}
	return (tot*(tot+1))/2;
}

int main() {
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		memset(visited,0,sizeof(visited));
		int A, B; cin >> A >> B;
		_A = A; _B = B;
		long long ans = 0;
		for (int i = A; i <= B; i++) {
			if (visited[i]) continue;
			ans += process(i);
		}
		cout << "Case #" << (t+1) << ": " << ans << "\n";
	}
	return 0;
}