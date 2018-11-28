
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T, N;	
	cin >> T;
	string A[100];

	cout.precision(20);

	double OWP[100], OOWP[100];
	int NB[100];
  int W[100];

	for(int t = 1; t <= T; t++) {
		cin >> N;
		for(int i = 0; i < N; i++)
			cin >> A[i];

		for(int i = 0; i < N; i++) {
			NB[i] = 0;
			W[i] = 0;
			for(int j = 0; j < N; j++) if(A[i][j] != '.') {
				NB[i]++;
				if(A[i][j] == '1') W[i]++;
			}
		}
		for(int i = 0; i < N; i++) {
			OWP[i] = 0.;
			for(int j = 0; j < N; j++) if(A[i][j] != '.') OWP[i] += (W[j] - (A[j][i] - '0')) / double(NB[j] - 1);
			OWP[i] /= double(NB[i]);
		}

		for(int i = 0; i < N; i++) {
			OOWP[i] = 0.;
			for(int j = 0; j < N; j++) if(A[i][j] != '.') OOWP[i] += OWP[j];
			OOWP[i] /= double(NB[i]);
		} 

		cout << "Case #" << t << ":" << endl;
		for(int i = 0; i < N; i++) cout << 0.25 * (W[i]/double(NB[i])) + 0.5 * OWP[i] + 0.25 * OOWP[i] << endl;


	}


}
