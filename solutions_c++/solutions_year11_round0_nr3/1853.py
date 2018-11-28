#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream cin("G:\\gcj\\C-large.txt");
	ofstream cout("G:\\gcj\\out.txt");
	int Case,t;
	
	cin >> t;
	for ( Case = 1; Case <= t; Case++ ) {
		int ans = 0;
		int n;
		int min = 1000000;
		int sum = 0;
		cin >> n;
		while ( n-- ) {
					
			int temp;
			cin >> temp;
			if ( temp < min ) {
				min = temp;
			}
			
			sum += temp;
			ans ^= temp;
		}
		cout << "Case #" << Case << ": ";
		if ( ans != 0 ) {
			cout << "NO" << endl;
		}
		else {
			cout << sum - min << endl;
		}
		
	}
	return 0;
}