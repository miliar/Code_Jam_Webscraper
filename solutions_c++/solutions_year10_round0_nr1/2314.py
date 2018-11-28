#include <iostream>

using namespace std;

int main()
{
	int t, n, k;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;
		
		bool flag = true;
		for (int j = 0; j < n; ++j) {
			if (!(k % 2)) {
				flag = false;
				break;
			}
			k /= 2;
		}
		
		cout << "Case #" << i << ": ";
		if (flag) cout << "ON\n";
		else cout << "OFF\n";
	}
	
}