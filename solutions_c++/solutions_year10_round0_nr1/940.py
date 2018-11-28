#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <math.h>

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
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		cout << "Case #" << (i+1) << ": ";
		long long N, K;
		file >> N >> K;
		long long on = pow(2, N) - 1;
		K = K % (long long)pow(2,N);
		if (K == on){
			cout << "ON" << endl;
		} else {
			cout << "OFF" << endl;
		}
	}
	file.close();
}
