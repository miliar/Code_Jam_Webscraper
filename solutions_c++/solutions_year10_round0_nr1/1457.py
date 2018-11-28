#include <iostream>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

long long int pow (int b, int p) {
	long long int ret = 1;
	while (p--)
		ret *= b;
	return ret;
};

int main () {
	in.open ("a.in");
	out.open ("a.out");
	long long int n, k, m;
	in >> n;
	for (int b = 1; b <= n; ++b) {
		in >> m >> k;
		out << "Case #" << b << ": ";
		if ((k+1) % pow (2, m) == 0)
			out << "ON";
		else
			out << "OFF";
		out << endl;
	}
	in.close ();
	out.close ();
}
