#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pi;

int main(void) { 
	int t, n;
	cin >> t;
	for (int i=0; i<t; i++) {
		cout << "Case #" << (i+1) << ": " << endl;
		cin >> n;
		vector < string > v;
		vector <vector <int> > vv;
		for (int j=0; j<n; j++) {
			string str;
			cin >> str;	
			v.push_back(str);
			vector <int> x;
			for (int k=0; k<n; k++) {
				if (str[k] == '0') {
					x.push_back(0);
				} else if (str[k] == '1') {
					x.push_back(1);
				} else {
					x.push_back(-1);
				}
			}
			vv.push_back(x);
		}
		vector <double> wp;
		vector <pair<int, int> > pv;
		for(int j=0; j<n; j++) {
				int w=0, d=0;
			for (int l=0; l<n; l++) {
				if (vv[j][l] == 0) {
					d++;
				} else if (vv[j][l] == 1) {
					w++;
				} 
			}
			double dd = (double)(w) / (double)(w+d);
			wp.push_back(dd);
			pv.push_back(pi(w, d));
			//cout << "dd: " << dd << endl;
		}

		vector <double> owp;
		for (int you=0; you<n; you++) {
			double sum=0.0;	
			int cnt=0;
			for (int k=0; k<n; k++) {
				if (vv[you][k] >= 0) {
					pi pp = pv[k];
					if (vv[you][k] > 0) {
						pp = pi(pp.first , pp.second-1);
					} else {
						pp = pi(pp.first-1, pp.second);
					}
					sum += (double)pp.first / (double)(pp.first + pp.second);
					cnt++;
				}
			}
			double ooo = sum / (double)(cnt);
			owp.push_back(ooo);
			//cout << "owp: " << ooo << endl;
		}

//		vector <double> oowp;
		for (int you=0; you<n; you++) {
			double sum=0.0;	
			int cnt=0;
			for (int k=0; k<n; k++) {
				if (vv[you][k] >= 0) {
					sum += owp[k];
					cnt++;
				}
			}
			double ooo = sum / (double)(cnt);
//			oowp.push_back(ooo);
	//		cout << "oowp: " << ooo << endl;
			double ret = 0.25 * wp[you] + 0.5 * owp[you] + 0.25 * ooo;
			cout << ret << endl;
		}
	}

}
