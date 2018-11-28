#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	
	long C;
	file >> C;
	for (long i = 0; i < C; i++){
		long N, K, B, T;
		file >> N >> K >> B >> T;
		vector <long > xs;
		for (long j = 0; j < N; j++){
			long x;
			file >> x;
			xs.push_back(x);
		}
		vector <long > vs;
		for (long j = 0; j < N; j++){
			long v;
			file >> v;
			vs.push_back(v);
		}

		vector<bool> llega;
		for (long j = 0; j < N; j++){
			if (xs[j] + vs[j] * T >= B){
				llega.push_back(true);
			} else {
				llega.push_back(false);
			}
		}

		long totalSaltos = 0;
		long currentSaltos = 0;
		long llegan = 0;
		for (long j = N-1; j >= 0; j--){
			if (llega[j] == false){
				currentSaltos++;
			} else {
				totalSaltos += currentSaltos;
				llegan++;
				if (llegan == K)
					break;
			}
		}
		if (llegan != K){
			cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << (i+1) << ": " << totalSaltos << endl;
		}


	}


	file.close();
}
