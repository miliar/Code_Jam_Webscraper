#include <iostream>

using namespace std;

void solve(){
	int n, myXor = 0;
	int minn = 1 << 30;
	long long sum = 0;

	cin >> n;
	for (int i = 0; i < n; i++){
		int temp;
		cin >> temp;
		if (temp < minn){
			minn = temp;
		}
		myXor ^= temp;
		sum += temp;
	}

	if (myXor == 0){
		cout << sum - minn << endl;
	}
	else {
		cout << "NO" << endl;
	}
}

int main(){
	int tests;
	cin >> tests;

	for (int t = 1; t <= tests; t++){
		cout << "Case #" << t << ": ";
		solve();
	}

	return 0;
}
