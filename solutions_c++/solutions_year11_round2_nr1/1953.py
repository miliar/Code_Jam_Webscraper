#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	int t, n;
	string s[103];
	
	cin >> t;
	for(int c=0; c<t; c++) {
		double rpi[101], wp[100], owp[100], oowp[100];
		int match[100], win[100];
		int m = 0, w = 0;	
		cin >> n;
		for(int i=0; i<n; i++)
			cin >> s[i];

		for(int i=0; i<n; i++) {
			win[i] = 0;
			match[i] = 0;
			for(int j=0; j<n; j++) {				
				switch( s[i][j] ){
				case '1':
					win[i]++;
					match[i]++;
					break;
				case '0':				
					match[i]++;
					break;
				}
			}
			wp[i] = double(win[i])/double(match[i]);
		}
		
		

		for(int i=0; i<n; i++) {
			double sum = 0;
			int d = 0;
			for(int j=0; j<n; j++) {
				switch(s[j][i]) {
				case '1':
					sum += ( double(win[j]-1) / double(match[j]-1) );
					d++;
					break;
				case '0':
					sum += ( double(win[j]) / double(match[j]-1) );
					d++;
					break;			
				}
			}
			owp[i] = sum / (double)d;
		}
	
		for(int i=0; i<n; i++) {
			double sum = 0;
			int d = 0;
			for(int j=0; j<n; j++) {
				if(s[j][i] != '.') {
					sum += owp[j];
					d++;			
				}
			}
			oowp[i] = sum / (double)d;
		}
		
		cout << "Case #" << c+1 << ":\n";
		for(int i=0; i<n; i++) {
			double tmp = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.12f\n", tmp);
		}
		
		
			
	}
}
