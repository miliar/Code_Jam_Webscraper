#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int nth;
	ifstream in("c_large.in");
	ofstream out("c_large.out");
	in >> nth;
	for (int T = 0; T < nth; T++) {
		int r, k, n;
		in >> r >> k >> n;
		int g[n], money[n], next[n];
		for (int i = 0; i < n; i++) {
			in >> g[i];
		}
		for (int i = 0; i < n; i++) {
			int szb = 0;
			int sz = 0;
			int j = i;
			int jb = 0;
			while (sz <= k) {
				szb = sz;
				jb  = j;
				sz += g[j];
				j = (j+1)%n;
				if (j == i) {
					if (sz <= k) {
						szb = sz;
						jb = j;
					}
					break;
				}
			}
			money[i] = szb;
			next[i] = jb;
		}

		int pos = 0;
		long long ret = 0;
		for (int i = 0; i < r; i++) {
			ret += money[pos];
			pos = next[pos];
		}
		out << "Case #" << T+1 << ": " << ret << endl;
	}
	in.close();
	out.close();
	return 0;
}
