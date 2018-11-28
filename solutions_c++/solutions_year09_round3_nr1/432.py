#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

inline int getIndex(char in) {
	if(in > '9')
		return in - 'a';
	else
		return in - '0' + 26;
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
		string num;
		getline(in, num);
	
		int vals[26+10];
		
		for(int j = 0; j < 26 + 10; j++)
			vals[j] = -1;
		
		vector<int> digits;
		
		digits.push_back(1);
		vals[getIndex(num[0])] = 1;
		int nextVal = 0;
		
		for(int j = 1; j < num.length(); j++) {
			int ind = getIndex(num[j]);
			if(nextVal == 1)
				nextVal++;
			if(vals[ind] == -1)
				vals[ind] = nextVal++;

			digits.push_back(vals[ind]);

		}
		
		
		int base = nextVal;
		if(base < 2)
			base = 2;
		long long result = 0;
		for(int j = 0; j < digits.size(); j++) {
			result *= base;
			result += digits[j];
		}
		out << result << endl;
	}
	
	cout << "Done!";
	string dummy;
	getline(cin, dummy);
    return 0;
}




