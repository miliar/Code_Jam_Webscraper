//#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("A-large.out");
vector<vector<int> > zmap;
int main() {
int T;
int N;
cin >> T;

for (int i=1; i<=T; i++) {
	cin >> N;
vector<int> empty;
zmap.clear();
string sp2;
getline(cin,sp2);
	for (int j=0; j<N; j++) {
	zmap.push_back(empty);
	string sp;
	getline(cin, sp);
		for (int k=0; k<N; k++) {
		zmap[j].push_back((int)sp[k]-48);
		}
	}
	vector<double> WP;
	vector<int> wong;
	vector<int> total;
	vector<double> OWP;
	vector<double> OOWP;
	for (int j=0; j<N; j++) {
		double myWP = 0;
		double totalplayed = 0;
		for (int k=0; k<N; k++) {
			if (zmap[j][k] == 1) { myWP +=1; totalplayed+=1; }
			else if (zmap[j][k] == 0) totalplayed+=1;
		}
		wong.push_back((int)myWP);
		total.push_back(totalplayed);
		WP.push_back(myWP/totalplayed);
	}
	for (int j=0; j<N; j++) {
		double OWP2=0;
		for (int k=0; k<N; k++) {
			if (zmap[j][k] == 1 || zmap[j][k] == 0) {
					if (zmap[k][j] == 1) OWP2 += (double)(wong[k]-1)/(double)(total[k]-1);
					else OWP2 += (double)(wong[k]/(double)(total[k]-1));
			}
		}
			OWP2 = OWP2 / (double)(total[j]);
			OWP.push_back(OWP2);
	}
	for (int j=0; j<N; j++) {
			double sumthem = 0;
			for (int k=0; k<N; k++) {
				if(zmap[j][k] == 1 || zmap[j][k] == 0) if (k!=j) sumthem += OWP[k];
			}
			OOWP.push_back(sumthem/(double)(total[j]));
	}
	cout << "Case #"<<i<<": " << endl;
	for (int j=0; j<N; j++) {
		cout << fixed << setprecision(9) << 0.25*WP[j] + 0.5*OWP[j] + 0.25*OOWP[j] << endl;
	}
}
return 0;
}
