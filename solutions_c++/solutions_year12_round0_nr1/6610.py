#include <iostream>
#include <map>
#include <fstream>
#include <sstream>

using namespace std;

const string INPUT_FILE = "A-small-attempt0.in";
const string OUTPUT_FILE = "A-small-attempt0.out";

void initMap(map<char, char> & m) {
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
}

string translateLine(map<char, char>& googToEnglish, string line) {
	string result;
	
	for (int i = 0; i < line.length(); i++) {
		char ch = line[i];
		if (ch == ' ') result += ch;
		else {
			result += googToEnglish[ch];
		}
	}
	return result;
}

int main (int argc, char * const argv[]) {
    
	map<char, char> googToEnglish;
	initMap(googToEnglish);
	
	ifstream infile;
	infile.open(INPUT_FILE.c_str());
	
	ofstream outfile;
	outfile.open(OUTPUT_FILE.c_str());
	
	string line;
	getline(infile, line);
	
	stringstream ss;
	ss << line;
	int count;
	ss >> count;
	
	for (int i = 0; i < count; ++i) {
		getline (infile, line);
		string translate = translateLine(googToEnglish, line);
		
		outfile << "Case #" << i + 1 << ": " << translate << endl;
	}
	
	cout << "HI THERE" << endl;
	
	
	infile.close();
    return 0;
}
