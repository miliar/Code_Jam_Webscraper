#include<iostream>
using namespace std;

int main() {
	long T;
	int N;
	long K;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		bool rez = true;
		cin >> N >> K;
		K++;
		long daug = 1;
		for(int u = 1; u <= N; u++)
			daug = daug * 2;
			if (K % daug != 0)
				rez = false;
		cout << "Case #" << i << ": ";
		if (rez)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
	return 0;
}
