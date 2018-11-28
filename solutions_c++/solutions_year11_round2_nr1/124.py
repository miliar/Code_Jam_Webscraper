#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
using namespace std;

void tc(int tcn) {
	int n;
	cin>>n;
	vector<string> v(n);
	for (int i=0;i<n;i++)
			cin>>v[i];
	vector<double> plays(n);
	vector<double> wins(n);
	vector<double> wp(n);
	vector<double> owp(n);
	vector<double> oowp(n);
	for (int i=0;i<n;i++) {
		int w = 0, p = 0;
		for (int j=0;j<n;j++) {
			if (v[i][j] == '0')
				p++;
			else if (v[i][j] == '1') {
				p++; w++;
			}
		}
		plays[i] = p;
		wins[i] = w;
		wp[i] = double(w)/double(p);
	}

	for (int i=0;i<n;i++) {
		double sumwp = 0;
		int countwp = 0;
		for (int j=0;j<n;j++) {
			if (v[i][j] == '.') continue;
			sumwp += (v[j][i] == '1') ?
				double(wins[j]-1)/double(plays[j]-1) :
				double(wins[j])/double(plays[j]-1);
			countwp += 1;
		}
		owp[i] = sumwp / countwp;
	}

	for (int i=0;i<n;i++) {
		double sumowp = 0;
		int countowp = 0;
		for (int j=0;j<n;j++) {
			if (v[i][j] == '.') continue;
			sumowp += owp[j];
			countowp += 1;
		}
		oowp[i] = sumowp / countowp;
	}
	cout << "Case #"<<tcn << ":"<<endl;
	for (int i=0;i<n;i++) 
		printf("%.9f\n", (wp[i] * 0.25 + owp[i] * 0.5 + oowp[i]*0.25));
}
int main() {
	int t;
	cin>>t;
	for (int i=1;i<=t;i++) tc(i);
}
