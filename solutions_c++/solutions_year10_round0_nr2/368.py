#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <math.h>
#include <vector>
#include "bigint/BigIntegerLibrary.hh" //Library downloaded from http://mattmccutchen.net/bigint/

//Algorithm
//Calculate DifSet = {|t0-t1|, |t2-t1|,...,|tn-tn-1|
//Calculate mcd = MCD(DifSet)
//Result is: mcd * (min(ti) / mcd) - min(ti). Note: division --> ceiling

using namespace std;

BigInteger getMCD(BigInteger r0, BigInteger r1){
	while(r1 != 0){
		BigInteger newR = r0 % r1;
		r0 = r1;
		r1 = newR;
	}
	return r0;
}
int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int C;
	file >> C;
	for (int i = 0; i < C; i++){
		int n;
		file >> n;
		string valueStr;
		BigInteger value;
		vector <BigInteger> values;
		BigInteger minValue = -1;
		for (int j = 0; j < n; j++){
			file >> valueStr;
			value = 0;
			for (int i = 0; i < valueStr.size(); i++){
				value = value*10 + (valueStr[i] - '0');
			}
			if ((minValue == -1) || (value < minValue))
				minValue = value;
			values.push_back(value);
		}
		//Calculate distances
		vector <BigInteger> distances;
		for (int j = 1; j < values.size(); j++){
			if (values[j] > values[j-1])
				distances.push_back(values[j] - values[j-1]);
			else
				distances.push_back(values[j-1] - values[j]);
		}

		//Calculate mcd
		BigInteger currentMCD = distances[0];
		for (int j = 1; j < distances.size(); j++){
			currentMCD = getMCD(currentMCD, distances[j]);
		}
		BigInteger r = minValue % currentMCD;
		BigInteger mult = minValue / currentMCD;
		if (r != 0){
			mult++;
		}
		cout << "Case #" << (i+1) << ": " << currentMCD * mult - minValue << endl;
	}
	file.close();
}
