#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
using namespace std;

bool isHappy(int num, int base) {
	set<int> seen;
	while(seen.find(num) == seen.end()) {
		seen.insert(num);
		int sum = 0;
		for(int basis = base; num != 0; basis *= base) {
			int thisDig = num % base;
			sum += thisDig * thisDig;
			num = num / base;
		}
		num = sum;
	}
	return (num == 1);
}

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ofstream out;
	out.open(outFileName.c_str());
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int T;
	
	paramsStream >> T;
	
	for(int i = 0; i < T; i++) {
		out << "Case #" << i + 1 << ": ";
		string bases;
		getline(in, bases);
		stringstream basesStream;
		basesStream << bases;
		vector<int> bVec;
		
		while(true) {
			int b;
			basesStream >> b;
			bVec.push_back(b);
			if(basesStream.eof())
				break;
		}
		
		int num = 2;
		bool happy = false;
		while(true) {
			happy = true;
			for(vector<int>::iterator it = bVec.begin(); (it != bVec.end()) && happy; ++it) {
				happy = happy && isHappy(num, *it);
			}
			if(happy)
				break;
			num++;
		}
		out << num << endl;
	}
	
	cout << "Done!";
	string dummy;
	getline(cin, dummy);
    return 0;
}
