#include<iostream>
#include<string>

using namespace std;

int main() {
	int T, N, K;
	string result;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> N >> K;
		cout << "Case #" << i + 1 << ": ";
		int a = 0, r;
		for (int j = 0; j < N; j++) 
			a += 1 << j;
		if (K % (a + 1) == a)
			cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
