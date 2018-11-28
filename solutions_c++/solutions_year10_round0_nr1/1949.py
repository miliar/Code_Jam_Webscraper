#include <iostream>

using namespace std;

bool check(int n, int k) {
	for (int i = 0; i < n; i++) {
		if (k % 2 == 0) return false;
		k /= 2;
	}
	return true;
}

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, k;
		cin >> n >> k;
		if (check(n,k)) cout << "Case #"<<i+1<<": ON" << endl;
		else cout << "Case #"<<i+1<<": OFF" << endl;
	}
	return 0;
}