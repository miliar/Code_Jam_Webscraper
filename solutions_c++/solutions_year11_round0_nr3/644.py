#include <iostream>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for(int num = 1; num <= t; num++) {
		int n, c[1000];
		cin >> n;
		for(int i=0;i<n;i++) {
			cin >> c[i];
		}
		
		int exor = 0, sum = 0, m = 2000000;
		for(int i=0;i<n;i++) {
			exor ^= c[i];
			sum += c[i];
			if(c[i]<m) m = c[i];
		}
		
		cout << "Case #" << num << ": ";
		if(exor!=0) {
			cout << "NO" << endl;
		} else {
			cout << (sum-m) << endl;
		}
	}
}
