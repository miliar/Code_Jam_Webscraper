#include <iostream>
#include <stdio.h>

using namespace std;

int main() {

	int test;
	scanf("%d", &test);
	for(int k = 1; k <= test; k++) {

		int n;
		scanf("%d", &n);
		char a[n][n];
	
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				cin >> a[i][j];
			}
		}
		long double wp[n];
		long double owp[n];
		long double oowp[n];
		for(int i = 0; i < n; i++) {
			int ret = 0, r = 0;
			for(int j = 0; j < n; j++) {
				if(a[i][j] == '1') { ret++;}
				if(a[i][j] == '0') {r++;}
			}
			wp[i] = ret*1.0/(ret+r);
		}
	
		for(int i = 0; i < n; i++) {
			long double ret = 0, r = 0, l = 0.0;int p = 0;
			for(int j = 0; j < n; j++) {int x = 0, y = 0;
				if(a[i][j] != '.'){p++;
					for(int t = 0; t < n; t++) {
						if(t != i) {
						if(a[j][t] == '1') {x++;}
						if(a[j][t] == '0') { y++;}
						}
					} l += x*1.0/(x+y);
				}}
				owp[i] = l/p;
		}
		for(int i = 0; i < n; i++) {
			long double f = 0.0;
			int g = 0;
			for(int j = 0; j < n; j++) {
				if(a[i][j] != '.') {
				g++;
				f += owp[j];
				}
			}
		oowp[i] = f/g;
		}	long double rpi[n];
		for(int i = 0; i < n; i++) {
			rpi[i] = (.25*wp[i]) + (.5*owp[i]) + (.25*oowp[i]);
		}
		cout << "Case #" << k << ":" << endl;
		for(int i = 0; i < n; i++) {	
			cout <<  rpi[i] << endl;
		}
			
                
	}

	return 0;
}

 
		
