#include <map>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>


using namespace std;

int main() {

	ifstream fin("A-large.in");	
// 	ifstream fin("in.txt");	
	ofstream fout("out.txt");
	int T;
	fin>>T;
	
	for (int Ti=1; Ti<=T; Ti++) {

		fout<<"Case #"<<Ti<<":"<<endl;
		
		int n;
		fin>>n;
		char ** m = new char * [n];
		for (int i=0; i<n; i++) {
			m[i] = new char [n];
			for (int j=0; j<n; j++) {
				fin>>m[i][j];
			}
		}
		
// 		vector<double> wp (n);
// 		for (int i=0; i<n; i++) {
// 			int tot = 0;
// 			wp[i] = 0;
// 			for (int j=0; j<n; j++) {
// 				if (m[i][j]=='.') continue;
// 				tot ++;
// 				if (m[i][j]=='1') wp[i]+=1;
// 			}
// 			wp[i] /= tot;
// 		}

		vector<int> win (n);
		vector<int> tot (n);
		for (int i=0; i<n; i++) {
			win[i] = 0;
			tot[i] = 0;
			for (int j=0; j<n; j++) {
				if (m[i][j]=='.') continue;
				tot[i] ++;
				if (m[i][j]=='1') win[i] ++;
			}
		}
		
// 		for (int i=0; i<n; i++) cout<<win[i]<<endl;
// 		for (int i=0; i<n; i++) cout<<tot[i]<<endl;
		
		vector<double> owp (n);
		for (int i=0; i<n; i++) {
			owp[i] = 0;
			int t = 0;
			for (int j=0; j<n; j++) {
				if (m[i][j]=='.') continue;
				t ++;
				owp[i] += (win[j]-m[j][i]+'0')*1.0/(tot[j]-1);
			}
			owp[i] /= t;
		}

// 		for (int i=0; i<n; i++) cout<<owp[i]<<endl;

		vector<double> oowp (n);
		for (int i=0; i<n; i++) {
			oowp[i] = 0;
			int t = 0;
			for (int j=0; j<n; j++) {
				if (m[i][j]=='.') continue;
				t ++;
				oowp[i] += owp[j];
			}
			oowp[i] /= t;
		}
// 		for (int i=0; i<n; i++) cout<<oowp[i]<<endl;
		
		for (int i=0; i<n; i++) {
			fout<<0.25*win[i]/tot[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
		}


	}
	
	fout.close();
	return 0;
}
