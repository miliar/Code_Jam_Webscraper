#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream in("input");
	if (!in) {cout << "!"; return 0;}
	ofstream out("output");
	int t;
	in >> t;
	for (int z = 0; z < t; z++) {
		int n;
		in >> n;
		char** j = new char*[n];
		for (int i = 0; i < n; i++)
			j[i] = new char[n];
		string s;
		getline(in, s);
		for (int i = 0; i < n; i++) {
			getline(in, s);
			memcpy(j[i], s.data(), n*sizeof(char));
		}
		double* wp = new double[n];
		double* owp = new double[n];
		double* oowp = new double[n];
		int c;
		for (int i = 0; i < n; i++) {
			wp[i] = 0;
			c = 0;
			for (int k = 0; k < n; k++)
				switch (j[i][k]) {
				case '1':
					wp[i] += 1;
				case '0':
					c++;
				}
			wp[i] /= c;
		}
		double r;
		int u;
		for (int i = 0; i < n; i++) {
			owp[i] = 0;
			u = 0;
			for (int k = 0; k < n; k++) {
				r = 0;
				c = 0;
				if (j[i][k] != '.') {
					for (int l = 0; l < n; l++)
						if (l != i)
							switch (j[k][l]) {
							case '1':
								r += 1;
							case '0':
								c++;
							}
					r /= c;
					u++;
					owp[i] += r;
				}
			}
			owp[i] /= u;
		}
		for (int i = 0; i < n; i++) {
			oowp[i] = 0;
			c = 0;
			for (int k = 0; k < n; k++)
				if (j[i][k] != '.') {
					oowp[i] += owp[k];
					c++;
				}
			oowp[i] /= c;
		}
		out << "Case #" << (z+1) << ": " << endl;
		for (int i = 0; i < n; i++) {
			out << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << endl;
			delete[] j[i];
		}
		delete[] j;
		delete[] wp;
		delete[] owp;
		delete[] oowp;
	}
	in.close();
	out.close();
}