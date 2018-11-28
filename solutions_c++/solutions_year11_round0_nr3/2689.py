#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T, N;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cin >> N;
		int c = 0, s = 0;
		int m = 999999999;
		for (int i = 0; i < N; i++){
			int n;
			cin >> n;
			c ^= n;
			s += n;
			m = min(m, n);
		}
		cout << "Case #" << t << ": ";
		if (c == 0)
			cout << s - m << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
