#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

const string welcome = "welcome to code jam";
string s;
int progress = 0;

int forwardRecurse(int stringIndex, int index) {
	int subtotal = 0;
	int sind;
	progress++;

	// terminating case
	if(index == welcome.length() - 1) {
		for(sind = stringIndex; sind < s.length(); sind++) {
			if(s.at(sind) == welcome.at(index)) {
				subtotal += 1;
			}
		}		
		return subtotal;
	}
	for(sind = stringIndex; sind < s.length(); sind++) {
		if(s.at(sind) == welcome.at(index)) {
			// cout << s.substr(sind + 1, s.length()) << endl;
			subtotal += forwardRecurse(sind + 1, index + 1);
		}
	}
	return subtotal % 10000;
}

int main() {
	int wordCounter = 0;
	int alienCounter = 0;
	int total = 0;
	string totalString;

	ofstream outfile;
	outfile.open("C-small-attempt1.out");

	string line;
	ifstream myfile("C-small-attempt1.in");
	getline(myfile, line);
	string::size_type space = line.find_first_of(" ");
	string Lstring = line.substr(0, space);
	
	stringstream sl(Lstring);
	int L;
	sl >> L;

	int i, j, k, l;

	for(i = 0; i < L; i++) {
		total = 0;
		getline(myfile,line);

		s = line;

		for(j = 0; j < s.length(); j++) {
			if(s.at(j) == welcome.at(0)){
				total += (forwardRecurse(j + 1, 1) % 10000);
			}
		}

		total = total % 10000;
		std::stringstream out;
		out << total;
		if(total == 0) {
			totalString = "0000";
		}else if (total < 10) {
			totalString = "000" + out.str();
		}else if (total < 100) {
			totalString = "00" + out.str();
		}else if (total < 1000) {
			totalString = "0" + out.str();
		} else {
			totalString = out.str();
		}
		
		cout << "Case #" << i + 1 << ": " << totalString << endl;
		outfile << "Case #" << i + 1 << ": " << totalString << endl;
	}
	return 0;
}
