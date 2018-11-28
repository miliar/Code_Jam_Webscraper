#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

typedef long double ld;
int main() {
	int T;
	cin >> T;
	string L[100];
	for(int t=1; t<=T; t++) {
		ld WP[100], OWP[100], OOWP[100];
		int N;
		cin >> N;
		for(int i=0; i<N; i++)
		 	cin >> L[i];
		int W[100] = {}, S[100] = {};
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++)
				W[i] += (L[i][j] == '1'), S[i] += (L[i][j] != '.');
			WP[i] = ld(W[i]) / S[i];
		}
		for(int i=0; i<N; i++) {
			ld s = 0;
			for(int j=0; j<N; j++)
				if (L[i][j] != '.')
					s += ld(W[j] - (L[j][i] == '1')) / (S[j] - 1);
			OWP[i] = s / S[i];
		}
		for(int i=0; i<N; i++) {
			ld s = 0;
			for(int j=0; j<N; j++)
				if (L[i][j] != '.')
					s += OWP[j];
			OOWP[i] = s / S[i];
		}

		cout << "Case #" << t << ": " << endl;
		for(int i=0; i<N; i++)
			printf("%Lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}

