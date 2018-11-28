#include <fstream>
#include <string>
#include <iostream>

using namespace std;

char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
			  'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	string filename;
	cout << "File name: ";
	cin >> filename;
	ifstream in(filename + ".in");
	ofstream out(filename + ".out");

	int T;
	in >> T;
	in.get();
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		out << "Case #" << caseNum << ": ";
		char c;
		while ((c = in.get()) != '\n' && in.good()) {
			if (c == ' ')
				out << ' ';
			else
				out << map[c - 'a'];
		}
		out << endl;
	}
}
