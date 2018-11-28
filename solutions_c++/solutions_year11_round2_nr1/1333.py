#include <iostream>
#include <fstream>

using namespace std;

fstream in("in.txt", fstream::in);
fstream out("out.txt", fstream::out);

void SolveCase(int t){
	int N, *W, *P; in >> N;
	char **table;
	double *OWP, *OOWP;
	table = new char* [N];
	for(int row = 0; row < N; row++){
		table[row] = new char [N + 1];
		in >> table[row];
	}
	
	W = new int [N];
	P = new int [N];
	
	for(int row = 0; row < N; row++){
		P[row] = 0; W[row] = 0;
		for(int col = 0; col < N; col++){
			if(table[row][col] != '.') P[row]++;
			if(table[row][col] == '1') W[row]++;
		}
	}

	OWP = new double [N];

	for(int i = 0; i < N; i++){
		OWP[i] = 0.0; int op = 0;
		for(int j = 0; j < N; j++){
			if(table[i][j] != '.'){
				OWP[i] += 1.0 * (W[j] - (table[i][j] == '0' ? 1 : 0)) / (P[j] - 1);
				op++;
			}
		}
		OWP[i] /= op;
	}

	OOWP = new double [N];
	for(int i = 0; i < N; i++){
		OOWP[i] = 0; int op = 0;
		for(int j = 0; j < N; j++){
			if(table[i][j] != '.'){
				OOWP[i] += OWP[j];
				op++;
			}
		}
		OOWP[i] /= op;
	}

	out << "Case #" << t << ":" << endl;
	for(int i = 0; i < N; i++){
		out << 0.25 * W[i] / P[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
	}

	delete[] OOWP;

	delete[] OWP;

	delete[] W;
	delete[] P;

	for(int row = 0; row < N; row++){
		delete[] table[row];
	}
	delete[] table;
}

int main(){
	int T; in >> T;
	for(int t = 0; t < T; t++)
		SolveCase(t+1);
	return 0;
}
