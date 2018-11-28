#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <list>
using namespace std;

ifstream in;
int len, dsize, n;
vector <string> dict;
string io;
bool allow [150];
ofstream out;

int main () {
	in.open ("a.in");
	out.open ("a.out");
	in >> len;
	in >> dsize;
	in >> n;
	bool rem [dsize];
	for (int c = 0; c!= dsize; ++c) {
		in >> io;
		dict.push_back (io);
	}
	for (int c = 0; c!= n; ++c) {
		int poss= dsize;
		in >> io;
		int i = 0;
		for (int d = 0; d != dsize; ++d)
			rem [d] = true;
		for (int f = 0; f != len; ++f) {
			for (int d = 0; d != 150; ++d)
				allow [d] = false;
			if (io [i] == '(') {
				++i;
				while (io [i] != ')')
					allow [io [i++]] = true;
			} else
				allow [io [i]] = true;
			++i;
			for (int d = 0; d != dict.size (); ++d)
				if (rem [d] && !allow [dict [d] [f]]) {
					--poss;
					rem [d] = false;
				}
		}
		out << "Case #" << c + 1 << ": " << poss << endl;
	}
	in.close ();
	out.close ();
}
