#include <string.h>
#include <fstream>

using namespace std;

int main() {
	string line;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	string conversion = "yhesocvxduiglbkrztnwjpfmaq";
	int num;
	fin >> num;
	
	getline(fin, line);
	for (int j = 1; j <= num; ++j){
		fout << "Case #" << j << ": ";
		getline(fin, line);
		for (int i = 0; i < line.size(); ++i) {
			if (line[i] - 97 < 0)
				fout << ' ';
			else fout << conversion[line[i] - 97];
		}
		fout << "\n";
	}
	return 0;
}