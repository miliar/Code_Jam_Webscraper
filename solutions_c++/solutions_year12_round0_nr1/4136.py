#include <iostream>
#include <fstream>

using namespace std;

ifstream f1("a.in");
ifstream f2("b.in");
ifstream fin("input.txt");
ofstream fout("output.txt");

char h[255];

int main() {
	string s1;
	char x, y;
	while (!f1.eof()) {
		f1 >> x; f2 >> y;
		if (x != ' ') h[x] = y;
	}
	h['q'] = 'z'; h['z'] = 'q'; h[' '] = ' ';
	h['\n'] = '\n';
	
	int n;
	fin >> n;
	getline(fin, s1);
	for (int cnt = 1; cnt <= n; ++cnt) {
		fout << "Case #" << cnt << ": ";
		getline(fin, s1);
		for (int i = 0; i < s1.size(); ++i) fout << h[s1[i]];
		fout << endl;
	}
}
