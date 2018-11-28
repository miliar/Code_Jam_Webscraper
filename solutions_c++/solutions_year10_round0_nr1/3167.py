#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int t, z = 0;
	cin >> t;
	
	while (t--) {
		z++;
		int n, k;
		cin >> n >> k;
	
		int p = 0, q = 1;
		for (int i = 0; i < n; i++) {
			p += q;
			q *= 2;	
		}
		
		cout << "Case #" << z << ": ";
		if (k < p) {
			cout << "OFF" << endl;
		} else if (k == p) {
			cout << "ON" << endl;
		} else {
			while (k > p) {
				k -= (p+1);
			}
			if (k == p) {
				cout << "ON" << endl;
			} else if (k < p) {
				cout << "OFF" << endl;
			}
		}				
	}
	
//	c1 = clock();
//	cout << (double)(c1-c0) / CLOCKS_PER_SEC << endl;

	return 0;
}
