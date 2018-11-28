#include <iostream>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

int main () {
	in.open ("c.in");
	out.open ("c.out");
	long long int n, r,s, m, sum, fill, ret, d;
	in >> n;
	for (int b = 1; b <= n; ++b) {
		in >> r >> s >> m;
		long long int group [m], val [m] , next [m];
		sum = 0;
		for (int c= 0; c!= m; ++c) {
			in >> group [c];
			sum += group [c];
			val [m] = 0;
		}
		for (int c = 0; c != m; ++c) {
			d = c;
			val [c] = 0;
			while (s >= val [c] + group [d] && sum >= val [c] + group [d]) {
				val [c] += group [d++];
				if (d == m) d = 0;
			}
			next [c] = d;
		}
		d = ret = 0;
		for (; r; --r) {
			ret += val [d];
			d = next [d];
		}
		out << "Case #" << b << ": " << ret << endl;
	}
	in.close ();
	out.close ();
}
