#include <iostream>
#include <fstream>

using namespace std;

int main() {

	int n, s, p, t, l;
	ifstream in("input.in");
	ofstream out("output.txt");
	in >> n;
	for (int i = 1; i <= n; i++) {
		int count = 0;
		in >> l;
		in >> s;
		in >> p;
		for (int j = 0; j < l; j++) {
			in >> t;
			if (t>=p) {
				if (3 * p - 2 <= t)
					count++;
				else {
					if (s > 0) {
						if (3 * p - 4 <= t) {
							s--;
							count++;
						}
					}
				}
			}
		}
		out << "Case #" << i << ": " << count;
		if(i<n) out<<endl;

	}
}
