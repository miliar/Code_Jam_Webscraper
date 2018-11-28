#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		int a, b;
		cin >> a >> b;
		
		int t = 1 << a;
		cout << "Case #" << i+1 << ": ";
		if ((b+1)%t == 0) 
			cout << "ON" << endl;
		else 
			cout << "OFF" << endl;
	}

	return 0;
}

