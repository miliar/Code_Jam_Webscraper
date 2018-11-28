#include <iostream>

using namespace std;

int main() {
	unsigned int t, n, k;
	cin >> t;
	for(unsigned int i = 1; i != t+1; i++) {
		cin >> n;
		cin >> k;
		cout << "Case #" << i << ": ";
		if(k%(1<<n) == (1<<n)-1)
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
	return 0;
}
