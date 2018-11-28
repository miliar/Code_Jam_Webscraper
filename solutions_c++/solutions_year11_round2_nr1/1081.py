#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>

#include <iostream>
#include <fstream>

#include <set>
#include <map>
#include <stack>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream fp;
	fp.open(argv[1]);
	int T;
	fp >> T;
	for (int t=0; t<T; t++) {
		cout << "Case #" << t+1 << ": " << endl;

		int N;
		fp >> N;
		int** m = new int *[N];
		for (int i=0; i<N; i++) m[i] = new int [N];
		int *g = new int [N];
		int *w = new int [N];
		memset(g, 0, sizeof(int)*N);
		memset(w, 0, sizeof(int)*N);
		for (int i=0; i<N; i++) {
			string s;
			fp >> s;
			for (int j=0; j<N; j++)
				if (s[j] == '1') { g[i] += 1; m[i][j] = 1; w[i] += 1; }
				else if (s[j] == '0') { g[i] += 1; m[i][j] = 0; }
				else m[i][j] = -1;		
		}
		
		double* WP = new double[N];
		double* OWP = new double[N];
		double* OOWP = new double[N];
		for (int i=0; i<N; i++)  WP[i] = w[i]/static_cast<double>(g[i]);
		for (int i=0; i<N; i++) {
			OWP[i] = 0;
			for (int j=0; j<N; j++) {
				if (m[i][j]>=0) {
					if (m[i][j] == 0)  OWP[i] += (w[j]-1)/static_cast<double>(g[j]-1);
					else  OWP[i] += w[j]/static_cast<double>(g[j]-1);
				}			
			}
			OWP[i] /= g[i];		
		}
		for (int i=0; i<N; i++) {
			OOWP[i] = 0;
			for (int j=0; j<N; j++)
				if (m[i][j]>=0)  OOWP[i] += OWP[j];
			OOWP[i] /= g[i];
			cout << 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i] << endl;
		
		}
		for (int i=0; i<N; i++) delete[] m[i];
		delete[] m;
		delete[] g;
		delete[] w;
		delete[] WP;
		delete[] OWP;
		delete[] OOWP;
	}
	fp.close();
}
