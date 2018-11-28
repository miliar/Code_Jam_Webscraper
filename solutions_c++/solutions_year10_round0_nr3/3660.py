#include <iostream>
#include <fstream>

using namespace std;

int t, r, k, n, ii;
long long res;
int idx=0;
int run;
ifstream in;
ofstream out;

int main() {
	in.open("C.in");
	out.open("C.out");
	in >> t;
	ii = 0;
	while (ii++<t) {
		in >> r >> k >> n;
		int g[n];
		for (int i=0; i<n; i++) in >> g[i];
		idx = 0;
		run = 0;
		res = 0;
		while (run++<r) {
			int sum=0;
			int grp=0;
			int tmp = sum+g[idx];
			while (tmp<=k && grp++<n) {
				sum = tmp;
				idx = (idx+1)%n;
				tmp = sum+g[idx];
			}
			res += sum;
		}
		out << "Case #" << ii << ": " << res << endl;
	}
    return 0;
}

