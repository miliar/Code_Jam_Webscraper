#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);

	int T;
	fin >> T;

	for(int T_i = 1; T_i <= T; ++T_i) {
		// read input
		int N;
		fin >> N;
		char data[N][N];
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < N; ++j) {
				fin >> data[i][j];
			}


		// process
		double WP[N];
		double takeout[N][N];
		int win, lose;
		for(int i = 0; i < N; ++i) {
			win = lose = 0;
			for(int j = 0; j < N; ++j)
				switch (data[i][j]) {
					case '1':
						win++;
						break;
					case '0':
						lose++;
						break;
					case '.':
						break;
				}
			WP[i] = (double) win/(win+lose);
			for(int j = 0; j < N; j++) {
				switch (data[i][j]) {
					case '1':
						takeout[i][j] = (double) (win-1)/(win+lose-1);
						break;
					case '0':
						takeout[i][j] = (double) (win)/(win+lose-1);
						break;
					case '.':
						takeout[i][j] = (double) (win)/(win+lose);
						break;
				}
			}
		}
/*
		cout << "takeout" << endl;
		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < N; ++j)
				cout << takeout[i][j] << '\t';
			cout << '\n';
		}
*/
		double OWP[N];
		for(int i = 0; i < N; ++i) {
			double sum = 0;
			int count = 0;
			for(int j = 0; j < N; ++j)
				if (data[i][j] != '.') {
					sum += takeout[j][i];
					count++;
				}
			OWP[i] = sum/count;
		}
		/*
		cout << "OWP" << endl;
		for(int i = 0; i < N; ++i)
			cout << OWP[i] << endl;
		*/

		double OOWP[N];
		for(int i = 0; i < N; i++) {
			OOWP[i] = 0;
			int count = 0;
			double sum = 0;
			for(int j = 0; j < N; ++j)
				if (data[i][j] != '.') {
					sum += OWP[j];
					count++;
				}
			OOWP[i] = sum/count;
		}

		//fout << fixed;
		fout << "Case #" << T_i << ": " << endl;
		double RPI[N];
		for(int i = 0; i < N; i++) {
			RPI[i] = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
				fout << RPI[i] << endl;
		}



		// output
		/*
		fout << "Case #" << T_i+1 << ": ";
		if ()
			fout << "Succeeded" << endl;
		else
			fout << "Failed" << endl;
		*/

	}

	fin.close();
	fout.close();
}

