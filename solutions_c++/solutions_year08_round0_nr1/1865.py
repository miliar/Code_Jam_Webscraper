
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>

using namespace std;

void saveUniverse(string input_file) {

	int no_tcs, S, Q, Sw;
	map<string,int> engines;
	map<string,int>::iterator iter;
	char tmp[100];

	ifstream fin(input_file.c_str());
	ofstream fout("output_file");

	fin.getline(tmp, 100);

	no_tcs = atoi(tmp);

	for(int i=0; i<no_tcs; i++) {
		engines.clear();
		Sw = 0;
		fin.getline(tmp, 100);
		S = atoi(tmp);

		unsigned int mask = 0, max;
		max = (unsigned int)pow((double)2, (double)S) - 1;

		for(int j=0; j<S; j++) {
			fin.getline(tmp, 100);
			engines.insert(make_pair(tmp, j));
		}

		fin.getline(tmp, 100);
		Q = atoi(tmp);

		for(int j=0; j<Q; j++) {
			fin.getline(tmp, 100);

			iter = engines.find(tmp);
			int in = iter->second;

			mask |= (1 << in);

			if(mask == max) {
				Sw++;
				mask = 0;
				mask |= (1 << in);
			}
		}

		fout << "Case #" << i+1 << ": " << Sw << endl;
	}

	fout.close();
	fin.close();

	cout << "Output File: ./output_file";
}


int main() {

	string input_file;
	cout << "Enter the path of the input_file: ";
	cin >> input_file;
	saveUniverse(input_file);
}
