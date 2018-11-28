#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
using namespace std;

int main() {
	//ifstream cin("F:\\TDDOWNLOAD\\A-large.txt");
	//ofstream cout("F:\\TDDOWNLOAD\\out.txt");

	int t,Case;
	cin >> t;

	for ( Case = 1; Case <= t; Case++ ) {
		int n,i;
		cin >> n;
		
		int loc1 = 1, loc2 = 1;
		int count1 = 0, count2 = 0;
		int ans = 0;
		for ( i = 0; i < n; i++ ){
			char name;
			int num;
			cin >> name >> num;
			
			if ( 'O' == name ) {
				if ( abs(loc1 - num) <= count1) {
					ans++;
					count2++;
				}
				else {
					ans += (abs(loc1 - num ) - count1 + 1);
					count2 += abs(loc1 - num ) - count1 + 1;
				}

				count1 = 0;
				loc1 = num;
			} else {
				if ( abs(loc2 - num) <= count2) {
					ans++;
					count1++;
				}
				else {
					ans += (abs(loc2 - num ) - count2 + 1);
					count1 += abs(loc2 - num ) - count2 + 1;
				}
				count2 = 0;
				loc2 = num;
			}
		}

		cout<< "Case #" << Case << ':'	<< ' ' << ans << endl;
	
	}

	return 0;
}