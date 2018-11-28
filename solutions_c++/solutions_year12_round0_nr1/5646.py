#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int N;
ifstream fin("a.in");
ofstream fout("a.out");
char alpha[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	fin >> N;
	string s;
	getline(fin, s);

	for (int i = 0; i < N; i++) {
		getline(fin, s);
		fout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < s.length(); j++)
			fout << ((s[j] == ' ') ? ' ' : alpha[s[j] - 'a']);
		fout << "\n";
	}

	system("PAUSE");
}