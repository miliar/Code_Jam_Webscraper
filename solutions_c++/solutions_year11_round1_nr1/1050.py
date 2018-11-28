#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<string>

using namespace std;

int main() {
	ifstream cin("F:\\gcj\\A-large.in");
	ofstream cout("F:\\gcj\\outputA.txt");

	int t,Case,i,j;
	cin >> t;

	for ( Case = 1; Case <= t; Case++ ) {
		int pd,pg;
		long long n;
		string ans;
		cin >> n >> pd >> pg;

		if ( n < 100 ) {
			bool flag = true;
			for ( int i = 1; i <= n; i++ ) {
				if ( (i * pd * 1.0 / 100 ) == (int)(i * pd * 1.0 / 100 ) ) {
					flag = false;
					break;
				}
			}
			if ( !flag ) {
				ans = "Possible";
			} else {
				ans = "Broken";
			}
		}
		else {
			ans = "Possible";
		}

		if ( pd != 100 && 100 == pg ) {
			ans = "Broken";
		} 
		if ( pd != 0 && 0 == pg ) {
			ans = "Broken";
		}

		cout << "Case #" << Case <<": " << ans << endl; 	
	}

	return 0;
}