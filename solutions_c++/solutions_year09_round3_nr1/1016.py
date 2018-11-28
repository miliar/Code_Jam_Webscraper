#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int main(){
	string ifile;
	cout << "enter the filename: ";
	cin >> ifile;

	ifstream infile(ifile.c_str());
	ofstream outfile((ifile.substr(0,ifile.length()-2)+"out").c_str());
	// check that the open succeeded
	if (!infile) {
		cerr << "error: unable to open input file: "
			<< ifile << endl;
		return -1;
	}
	if (!outfile) {
		cerr << "error: unable to create output file: "
			<< ifile.substr(0,ifile.length()-2)+"out" << endl;
		return -1;
	}

	int count = 1;
	int cases;
	infile >> cases;

	while(cases--){
		string line;
		infile >> line;
		int base = 1;
		int num[61];
		num[0] = 1;
		bool flag = true;
		long long ret = 0;
		for (size_t i = 1; i != line.size(); ++i) {
			string s(line, 0, i);
			size_t found = s.find(line[i], 0);
			if (found == string::npos) {
				if (flag) {
					num[i] = 0;
					flag = false;
					base++;
				}
				else
					num[i] = base++;
			}
			else {
				num[i] = num[int(found)];
			}
		}

		if(base == 1)
			base++;
		for (int i = 0; i != line.size(); ++i) {
			ret += num[i] * pow(double(base),int(line.size()-i-1));
		}

		outfile << "Case #" << count++ << ": " << ret << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}