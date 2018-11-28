#include <fstream>
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

ifstream in;
ofstream out;
int n, mlen, len;
char io [501];
char msg [] = "welcome to code jam";

int main () {
	mlen = strlen (msg);
	in.open ("c.in");
	out.open ("c.out");
	in >> n; in.get ();
	for (int m = 0; m != n; ++m) {
		in.getline (io, 500, '\n');
		len = strlen (io);
		long long int ways [len] [mlen];
		for (int c = 0; c!= len; ++c)
			for (int d = 0; d!= mlen; ++d)
				ways [c] [d] = 0;
		for (int c = 0; c!= len; ++c)
			if (io [c] == 'w')
				ways [c] [0] = 1;
		for (int c = 1; c!= mlen; ++c)
			for (int d = 0; d!= len; ++d)
				if (io [d] == msg [c]) {
					long long int sum = 0;
					for (int e = 0; e != d; ++e)
						if (io [e] == msg [c - 1])
							sum += ways [e] [c -1];
					ways [d] [c] = sum;
				}
		long long int fways = 0;
		for (int c =0; c!= len; ++c)
			if (io [c] == 'm')
				fways += ways [c] [mlen - 1];
		for (int c = 0; c!= len; ++c) {
			for (int d = 0; d != mlen; ++d)
				cout << ways [c] [d] << ' ';
			cout << endl;
		}
		cout << endl;
		out << "Case #" << m + 1 << ": ";
		out.fill ('0');
		out << setw (4) << fways % 10000 << endl;
	}
	in.close ();
	out.close ();
}
