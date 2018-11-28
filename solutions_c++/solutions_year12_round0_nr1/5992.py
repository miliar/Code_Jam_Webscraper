#include <fstream>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const string mapping = "yhesocvxduiglbkrztnwjpfmaq";

string s;

int main() {
	int t;
	fin >> t;
	getline(fin, s);
	for (int u = 0; u < t; u++) {
		getline(fin, s);
		fout << "Case #" << u + 1 << ": ";
		for (int i = 0; i < s.length(); i++)
			if (isalpha(s[i]))
				fout << mapping[s[i] - 'a'];
			else 
				fout << s[i];
		fout << endl;
	}
}