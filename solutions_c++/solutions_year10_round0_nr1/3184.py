#include <iostream>

using namespace std;

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	long long t, n, k;
	cin >> t;
                
	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		k %= (1<<n);
		cout << "Case #" << i+1 << ": ";
		if (k == (1<<n)-1)  cout << "ON";
		else		    cout << "OFF";
		cout << "\n";
	}



	return 0;
}