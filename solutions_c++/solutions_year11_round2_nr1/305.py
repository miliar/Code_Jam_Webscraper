#include <string>
#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

char c[200][200];
long double wps[200][200];
long double owps[200];
long double oowps[200];
int n;

long double wp(int x, int away) {
	if (wps[x][away] > -0.5) {
		return wps[x][away];
	}
	int wp1 = 0;
	int wp2 = 0;
	for (int i = 0; i < n; ++i) {
		if (i == away) continue;
		if (c[x][i] == '1') {
			wp1++;
		}
		if (c[x][i] != '.') {
			wp2++;
		}
	}	
	return wps[x][away] = (wp1 * 1.0L / wp2);	
}

long double owp(int x) {
	if (owps[x] > -0.5) {
		return owps[x];
	}
	long double owp1 = 0.0;
	int owp2 = 0;
	for (int i = 0; i < n; ++i) {
		if (c[x][i] != '.') {
			owp1 += wp(i, x); 
			owp2++;
		}
	}
	return owps[x] = (owp1 * 1.0L / owp2);	
}

long double oowp(int x) {
	if (oowps[x] > -0.5) {
		return oowps[x];
	}
	long double oowp1 = 0;
	int oowp2 = 0;
	for (int i = 0; i < n; ++i) {
		if (c[x][i] != '.') {
			oowp1 += owp(i); 
			oowp2++;
		}
	}
	return oowps[x] = (oowp1 * 1.0L / oowp2);	
}


int main() {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ++ti) {
		printf("Case #%d:\n", ti);
		cin >> n;
		for (int i = 0; i < 200; ++i) {
			for (int j = 0; j < 200; ++j) {
				wps[i][j] = -1;
			}
			owps[i] = oowps[i] = -1;			
		}
		
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> c[i][j];
			}
		}
		for (int i = 0; i < n; ++i) {
			long double rpi = 0.25L * wp(i, 199) + 0.5L * owp(i) + 0.25L * oowp(i);
			printf("%.12Lf\n", rpi);
		}
	}

}
