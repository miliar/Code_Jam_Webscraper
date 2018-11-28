#include<vector>
#include<iostream>
#include<iomanip>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T; cin>>T;

	for (int t=1; t<=T; t++) {

	vector<double> wp, owp, oowp, rpi;

	int N; cin>>N;
	char grid[N][N];
	for (int i=0; i<N; i++) for (int j=0; j<N; j++) cin>>grid[i][j];

	for (int i=0; i<N; i++) {
		int win=0,lose=0;
		for (int j=0; j<N; j++) {
			char ch=grid[i][j];
			switch(ch) {
				case '1': win++; break;
				case '0': lose++; break;
				case '.': break;
			}
		}

		wp.push_back(((double) win)/(win+lose));
	}

	for (int i=0; i<N; i++) {
		double curr=0;
		int total=0;
		for (int j=0; j<N; j++) {
			if(i!=j && grid[i][j]!='.') {
				int win=0,lose=0;
				for (int k=0; k<N; k++) {
					if(k!=i) {
						char ch=grid[j][k];
						switch(ch) {
							case '1': win++; break;
							case '0': lose++; break;
							case '.': break;
						}
					}
				}
				if(!(win==0 && lose==0)) total++;
				curr+=((double) win)/(win+lose);
			}
		}
		owp.push_back(curr/total);
	}

	for (int i=0; i<N; i++) {
		double curr=0;
		int total=0;
		for (int j=0; j<N; j++) {
			if(i!=j && grid[i][j]!='.') {curr+=owp[j]; total++;}
		}
		oowp.push_back(curr/total);
	}

	for (int i=0; i<N; i++) rpi.push_back(.25*wp[i]+.5*owp[i]+.25*oowp[i]);

	cout << "Case #" << t << ":" << endl;
	for (int i=0; i<N; i++) cout << setprecision(10) << rpi[i] << endl;

	}

	return 0;
}
