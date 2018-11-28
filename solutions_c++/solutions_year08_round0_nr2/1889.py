#include <iostream>
#include <fstream>
#include "Solver.h"
using namespace std;

int main(int argc, char *argv[]) {
	if(argc != 3){
		cerr << "Usage: " << argv[0] << " input_filename output_filename" << endl;
		return -1;
	}
	cout << argv[0] << " started." << endl;

	cout << "Opening " << argv[1] << endl;
	ifstream inputfile(argv[1]);
	if(inputfile.fail()) {
		cerr << "Cannot open " << argv[1] << endl;
		return -1;
	}

	cout << "Opening " << argv[2] << endl;
	ofstream outputfile(argv[2]);
	if(outputfile.fail()) {
		cerr << "Cannot open " << argv[2] << endl;
		return -1;
	}

	Solver solver;

	unsigned int N = 0;
	inputfile >> N;
	cout << N << " test cases." << endl;

	string temp;
	getline(inputfile, temp);

	for(unsigned int i = 1; i <= N; ++i){
		cout << "Executing test case " << i << endl;
		outputfile << "Case #" << i << ": ";
		solver.solve(inputfile, outputfile);
		outputfile << endl;
	}

	inputfile.close();
	outputfile.close();
	cout << argv[0] << " ends." << endl;
	return 0;
}
