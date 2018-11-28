#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <stdint.h>
#include <cstring>
#include <cassert>
#include <iomanip>

using namespace std;

void Do(uint32_t i) {
	cout << "Case #" << i << ":" << endl;
	
	uint32_t n;
	cin >> n;
	
	uint32_t d[100][100];
	
	uint32_t p[100];
	uint32_t w[100];
	
	memset(p, 0, sizeof(p));
	memset(w, 0, sizeof(w));
	
	double wp[100];
	double owp[100];
	double oowp[100];
	
	memset(wp, 0, sizeof(wp));
	memset(owp, 0, sizeof(owp));
	memset(oowp, 0, sizeof(oowp));
	
	for (uint32_t j = 0; j < n; j++) {
		for (uint32_t i = 0; i < n; i++) {
			char c;
			cin >> c;
			d[j][i] = (c == '1' ? 1 : c == '0' ? 0 : 2);
			
			if (d[j][i] != 2) {
				p[j]++;
				if (d[j][i] == 1) {
					w[j]++;
				}
			}
		}
		wp[j] = double(w[j]) / double(p[j]);
	}
	
	for (uint32_t j = 0; j < n; j++) {
		uint32_t q = 0;
		for (uint32_t i = 0; i < n; i++) if (d[j][i] != 2) {
			q++;
			owp[j] += double (w[i] - (d[j][i] == 0)) / double (p[i] - 1);
		}
		owp[j] /= double (q);
	}

	for (uint32_t j = 0; j < n; j++) {
		uint32_t q = 0;
		for (uint32_t i = 0; i < n; i++) if (d[j][i] != 2) {
			q++;
			oowp[j] += owp[i];
		}
		oowp[j] /= double(q);
		
		cout << setiosflags(ios::fixed) << setprecision(12) << 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j] << endl;
	}
}

int main() {
	uint32_t n;
	cin >> n;
	
	for (uint32_t i = 1; i <= n; i++) {
		Do(i); 
	}
	return 0;
}
