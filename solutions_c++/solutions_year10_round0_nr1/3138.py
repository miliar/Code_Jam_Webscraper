#include <iostream>
using namespace std;

int n,k,t;
string on;

int main() {
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> k;
		if (k == 0) { cout << "Case #" << i+1 << ": OFF" <<endl; continue;}
		int pow = 1 << n;
		on = (k+1)%pow == 0 ? "ON" : "OFF";
		cout << "Case #" << i+1 << ": " << on <<endl;
	}	
}	
