#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <limits.h>
#include <vector>

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
		int N; //number of candies
		file >> N;
		vector<long> candiesValue;
		long minValue = LONG_MAX;
		long sum = 0;
		long xored = 0;
		for (int j = 0; j < N; j++){
			long value;
			file >> value;
			xored ^= value;
			sum += value;
			if (value < minValue){
				minValue = value;
			}
			candiesValue.push_back(value);
		}
		cout << "Case #" << (i+1) << ": ";
		if (xored == 0){
			cout << (sum - minValue) << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}
