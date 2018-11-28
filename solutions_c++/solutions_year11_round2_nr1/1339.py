#include<iomanip>
#include<string>
#include<fstream>
#include<iostream>

using namespace std;

#define MAX	1000
double p[MAX],w[MAX],wp[MAX],owp[MAX],oowp[MAX],rpi[MAX];
string s[MAX];


int main(){

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	int ntc,n;

	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		for (int i=0;i<n;i++){
			p[i] = w[i] = wp[i] = owp[i] = oowp[i] = rpi[i] = 0;
			cin >> s[i];
			for (int j=0;j<n;j++){
				if (s[i][j]=='0')
					p[i]++;
				else if (s[i][j]=='1')
					p[i]++,w[i]++;
			}
			wp[i] = w[i]/p[i];
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (s[i][j]=='1')
					owp[i]+=w[j]/(p[j]-1);
				else if (s[i][j]=='0')
					owp[i]+=(w[j]-1)/(p[j]-1);
			}
			owp[i]/=p[i];
		}
		cout << "Case #" << tc << ":" << endl;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (s[i][j]!='.' )
					oowp[i]+=owp[j];
			}
			oowp[i]/=p[i];
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			cout << setprecision(12) << fixed << rpi[i] << endl;
		}
		
	}

	return 0;
}