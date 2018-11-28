#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream in;
ofstream out;

int main () {
	char comb ['Z']['Z'];
	bool opp ['Z']['Z'];
	in.open ("small2.in");
	out.open ("small2.out");
	int n, nc, no;
	string io;
	in >> n;
	for (int m= 0;m != n; ++m) {
		for (int c= 0; c != 'Z'; ++c)
			for (int d= 0; d != 'Z'; ++d)
				comb [c][d] = opp [c] [d] = 0;
		in >> nc;
		for (int c = 0; c!= nc; ++c) {
			in >> io;
			comb [io[0]][io[1]] = comb [io[1]][io[0]] = io [2];
		}
		in >> no;
		for (int c = 0;c != no; ++c) {
			in >> io;
			opp [io[0]][io[1]] = opp [io[1]][io[0]] = true;
		}
		in >> no;
		in >> io;
		vector <char> elem;
		for (int c= 0; c!= io.size (); ++c) {
			if (elem.size ()>0 && comb [io[c]][elem[elem.size()-1]] != 0)  {
				char ch = elem[elem.size()-1];
				elem.pop_back ();
				elem.push_back (comb [io[c]][ch]);
				goto next;
			}
			for (int d = 'A'; d <= 'Z';++d)
				if (opp [io[c]][d] && find (elem.begin (), elem.end (), d) != elem.end()) {
					elem.clear();
					goto next;
				}
			elem.push_back (io[c]);
			next:;
		}
		out <<"Case #"<< m+1 << ": [";
		for (int c= 0;c != elem.size (); ++c) {
			out << elem[c];
			if (c != elem.size()-1) out << ", ";
		}
		out << "]" << endl;
	}
}
