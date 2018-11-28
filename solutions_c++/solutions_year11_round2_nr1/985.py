#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>
#include <cfloat>

using namespace std;

const int NN = 128;

int T;
int n;
char m[NN][NN];
double wp[NN], owp[NN], oowp[NN], rpi[NN];

int main(void) {
	scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%s", m[i]);

		// WP
		for(int i = 0; i < n; i++) {
			double den = 0.0, num = 0.0;
			for(int j = 0; j < n; j++) {
				if(m[i][j] == '.') continue;
				num += m[i][j] == '1';
				den++;
			}
			wp[i] = num/den;
		}

		// OWP
		for(int i = 0; i < n; i++) {
			double den = 0.0, num = 0.0;
			for(int j = 0; j < n; j++) {
				double x = 0.0, y = 0.0;
				for(int k = 0; k < n; k++) {
					if(k == i) continue;
					if(m[i][j] == '.') continue;
					if(m[j][k] == '.') continue;
					x += m[j][k] == '1';
					y++;
				}
				if(y < 1e-9) continue;
				num += x/y;
				den++;
			}
			owp[i] = num/den;
		}

		// OOWP
		for(int i = 0; i < n; i++) {
			double den = 0.0, num = 0.0;
			for(int j = 0; j < n; j++) {
				if(m[i][j] == '.') continue;
				num += owp[j];
				den++;
			}
			oowp[i] = num/den;
		}

		// RPI
		for(int i = 0; i < n; i++)
			rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];

		printf("Case #%d:\n", C);
		for(int i = 0; i < n; i++) {
			printf("%.20lf\n", rpi[i]);
		}
	}


	return 0;
}
