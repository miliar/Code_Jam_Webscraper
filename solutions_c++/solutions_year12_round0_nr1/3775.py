#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	int alphabet[26], i = 0, n;
	char c;
	string line;
	char example [2][200] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv\0", 
							 "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up\0"};
	
	
	while (example[0][i] != '\0' && i < 200) {
		alphabet[example[0][i] - 'a'] = example[1][i];
		i++;
	}
	alphabet[25] = 'q';
	alphabet['q' - 'a'] = 'z';
	
	ifstream fin;
	ofstream fout;
	fout.open("output.txt");
	fin.open("input.txt");
	
	getline(fin, line);
	n = atoi (line.data());

	for (i = 1; i <= n; ++i) {
		fout << "Case #" << i << ": ";

		getline(fin, line);

		for (int j = 0; j < line.length(); ++j) {
			if (line[j] == ' ') {
				fout << ' ';
			} else {
				fout << (char)alphabet[line[j] - 'a'];
			}
		}
		fout << '\n';
 	}
	fout.close();
	fin.close();
	return 0;
}