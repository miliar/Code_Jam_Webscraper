#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int tn;
	cin >> tn;
	for(int cc=1;cc<=tn;++cc) {
		int n;
		cin >> n;
		vector<string> table(n);
		for(int i=0;i<n;++i) cin >> table[i];
		vector<int> win(n);
		vector<int> lose(n);
		vector<int> total(n);
		for(int i=0;i<n;++i) {
			win[i] = count( table[i].begin(), table[i].end(), '1' );
			total[i] = win[i] + count( table[i].begin(), table[i].end(), '0' );
		}

		vector<double> wp(n);
		for(int i=0;i<n;++i) {
			if( total[i] == 0 ) wp[i] = 0;
			else wp[i] = (double)win[i] / (double)(total[i]);
		}
		vector<double> owp(n,0.0);
		for(int i=0;i<n;++i) {
			for(int j=0;j<n;++j) {
				if( table[i][j] != '.' ) {
					int w = win[j];
					int t = total[j];
					if( table[j][i] == '1' ) --w, --t;
					else if( table[j][i] == '0' ) --t;
					if( t != 0 ) owp[i] += (double)w / (double)t;
				}
			}
			owp[i] /= total[i];
		}
		vector<double> oowp(n,0.0);
		for(int i=0;i<n;++i) {
			for(int j=0;j<n;++j) if( table[i][j] != '.' ) oowp[i] += owp[j];
			oowp[i] /= total[i];
		}
		vector<double> rpi(n,0.0);
		for(int i=0;i<n;++i) rpi[i] = .25 * wp[i] + .50 * owp[i] + .25 * oowp[i];

		cout << "Case #" << cc << ":" << endl;
		for(int i=0;i<n;++i) printf("%.9f\n", rpi[i]);

	}
}
