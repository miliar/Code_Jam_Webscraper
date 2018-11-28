#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

ifstream fin("in");
ofstream fout("out");

const int MAX_N = 105;

vector<int> played[MAX_N];
int sched[MAX_N][MAX_N];
int n[MAX_N];
double wp[MAX_N];
double owp[MAX_N];
double oowp[MAX_N];
double rpi[MAX_N];

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int N; fin>>N;
		for(int i=0; i<N; i++) {
			played[i].clear();
			for(int j=0; j<N; j++) {
				char ch; fin>>ch;
				if(ch!='.') {
					played[i].push_back(j);
					sched[i][j]=(int)(ch-'0');
				}
			}
			n[i] = (int)played[i].size();
		}

		// Compute WP
		for(int i=0; i<N; i++) {
			wp[i]=0.0;
			for(int j1=0; j1<n[i]; j1++) {
				int j=played[i][j1];
				wp[i] += sched[i][j];
			}
			wp[i] /= n[i];
		}

		// Compute OWP
		for(int i=0; i<N; i++) {
			owp[i] = 0.0;
			for(int j1=0; j1<n[i]; j1++) {
				int j=played[i][j1];
				owp[i] += (n[j]*wp[j] - sched[j][i]) / (n[j]-1);
			}
			owp[i] /= n[i];
		}
		
		// Compute OOWP
		for(int i=0; i<N; i++) {
			oowp[i] =0.0;
			for(int j1=0; j1<n[i]; j1++) {
				int j=played[i][j1];
				oowp[i] += owp[j];
			}
			oowp[i] /= n[i];
		}

		fout << "Case #" << t << ":" << endl;
		// Compute RPI
		for(int i=0; i<N; i++) {
			rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			fout << setprecision(12) << rpi[i] << endl;
		}
	}
	
	return 0;
}












