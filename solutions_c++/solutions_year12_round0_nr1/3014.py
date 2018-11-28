#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	char *a = new char[26];
	char *des = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char *ori = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for (int i = 0; i < strlen(des); i++) {
		if (des[i] != ' ')
			a[des[i]-'a'] = ori[i];
	}
	a[25] = 'q';
	a[16] = 'z';
	
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int T;
	fin >> T;
	string line = ""; 
	getline(fin, line);
	for (int i = 1; i <= T; i++) {
		fout << "Case #" << i << ": ";
		getline(fin, line);
		for (int j = 0; j < line.length(); j++) {
			if (line[j] != ' ') {
				fout << a[line[j]-'a'];
			}
			else
				fout << ' ';
		}
		fout << endl;
	}
	
}