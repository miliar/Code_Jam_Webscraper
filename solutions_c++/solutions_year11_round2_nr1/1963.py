/* Author = Levan Kasradze */

#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>

using namespace std;

int main(int argc, char **argv) {
    ifstream fin("a.in", ios::in);
    ofstream fout("a.out", ios::out);

    int T;
    fin >> T;

    for (int i=1; i<=T; ++i) {
        fout << "Case #" << i << ":\n";
        int N;
        fin >> N;

	char **m = new char * [N];
	for (int j = 0; j < N; j++)
            m[j] = new char [N];

	double * nGames = new double [N];
	double * wp = new double [N];
	double * owp = new double [N];
	double * oowp = new double [N];

	for (int j=0; j<N; ++j) {
		nGames[j] = 0.0;
		wp[j] = 0.0;
		for (int k=0; k<N; ++k) {
			fin >> m[j][k];
			if (m[j][k] == '1') { nGames[j]++; wp[j]++;}
			if (m[j][k] == '0') nGames[j]++;
		}
	}

	/*for (int j=0; j<N; ++j)
	cout << nGames[j] << " ";
	cout<< endl;
	
	for (int j=0; j<N; ++j)
	cout << wp[j] << " ";
	cout<< endl;*/
	
	

	for (int j=0; j<N; ++j) {
		owp[j] = 0.0;
		for (int k=0; k<N; ++k) 
			if (m[j][k] != '.' && j != k) {
				double t = 0.0;
				if (m[k][j] == '1') t = 1.0;
				owp[j] += (wp[k] - t) / (nGames[k] - 1.0);
				//cout << j << " " << k << " " << owp[j] << endl;
			}
		owp[j] /= nGames[j];
	}

	/*for (int j=0; j<N; ++j)
	cout << owp[j] << " ";
	cout<< endl;*/


	for (int j=0; j<N; ++j) {
		oowp[j] = 0.0;
		for (int k=0; k<N; ++k)
			if (m[j][k] != '.' && j != k)
				oowp[j] += owp[k]; 

		oowp[j] /= nGames[j];
	}

	/*for (int j=0; j<N; ++j)
	cout << oowp[j] << " ";
	cout<< endl;*/


	for (int j=0; j<N; ++j)
		fout << (0.25 * wp[j]/nGames[j] + 0.5 * owp[j] + 0.25 * oowp[j]) << "\n";


	for (int j = 0; j < N; j++)
        	delete[] m[j];
        delete[] m;
        m = 0;
	delete [] nGames;
	delete [] wp;
	delete [] owp;
	delete [] oowp;
    }

    fin.close();
    fout.close();
    return 0;
}
