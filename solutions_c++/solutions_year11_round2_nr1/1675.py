#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for(int i=1; i<=t; ++i) {
		int n;
		cin >> n;
		vector<string> v;
		for(int j=0; j<n; ++j) {
			string line;
			cin >> line;
			v.push_back(line);
		}
		vector<double> wp(n, 0.0);
		vector<double> owp(n, 0.0);
		vector<double> oowp(n, 0.0);
		
		for(int j=0; j<n; ++j) {
			int a = 0;
			int b = 0;
			for(int k=0; k<n; ++k) {
				if(v[j][k] == '1') {
					++ a; ++ b;
				} else if(v[j][k] == '0') {
					++ b;
				}
			}
			wp[j] = (double)a/(double)b;
		}

		for(int j=0; j<n; ++j) {
			int a = 0;
			for(int k=0; k<n; ++k) {
				if(v[j][k] != '.') {
					++ a;
					int b = 0;
					int c = 0;
					for(int l=0; l<n; ++l) {
						if(l == j) continue;
						if(v[k][l] == '1') {
							++ b; ++ c;
						} else if(v[k][l] == '0') {
							++ c;
						}
					}
					owp[j] += (double)b/(double)c;
				}
			}
			if(a > 0) owp[j] /= a;
		}

		for(int j=0; j<n; ++j) {
			int a = 0;
			for(int k=0; k<n; ++k) {
				if(v[j][k] != '.') {
					++ a;
					oowp[j] += owp[k];
				}
			}
			if(a > 0) oowp[j] /= a; 
		}

		cout << "Case #" << i << ": " << endl;
		for(int j=0; j<n; ++j) {
			double rpi = 0.25*wp[j] + 0.50*owp[j] + 0.25*oowp[j];
			cout << setprecision(12) << rpi << endl;
		}
	}

	return 0;
}
