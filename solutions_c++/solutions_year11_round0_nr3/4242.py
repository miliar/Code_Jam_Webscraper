#include <iostream>

using namespace std;

int main(void){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int N, sum = 0, minE = 2000047, xsum = 0;
		cin >> N;
		for (int i = 0; i < N; i++){
			int x;
			cin >> x;
			sum += x;
			if (x < minE) minE = x;
			xsum ^= x;
		}
		cout << "Case #" << t << ": ";
		if (xsum != 0) cout << "NO";
		else cout << sum-minE;
		cout << endl;
	}
}
