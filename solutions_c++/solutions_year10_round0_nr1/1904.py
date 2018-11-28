#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int nsz;
	ifstream in("large.in");
	ofstream out("large.out");
	in >> nsz;
	for (int nth = 1; nth <= nsz; nth++) {
		int n, k;
		in >> n >> k;
		bool flag = true;
		for (int i = 0; i < n; i++) {
			if (!(1 & (k >> i))) {
				flag = false;
				break;
			}
		}
		out << "Case #" << nth << ": ";
		if (flag) {
			out << "ON" << endl;
		}
		else {
			out << "OFF" << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}
