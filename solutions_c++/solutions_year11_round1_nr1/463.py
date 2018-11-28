#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t;

__int64 n;
int pd;
int pg;

int main() {
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		string input;
		in >> input; 
		n = _atoi64(input.c_str());
		in >> pd;
		in >> pg;

		string ans = "Broken";

		if (pg == 100 && pd < 100) {
			ans = "Broken";
		} else if (pg == 0 && pd > 0) {
			ans = "Broken";
		} else if (pg == 0 && pd == 0) {
			ans = "Possible";
		} else if (pg == 100 && pd == 100) {
			ans = "Possible";
		} else if (n >= 100) {
			ans = "Possible";
		} else {
			for (int j = 1; j <= n; j++) {
				if ((j * pd) % 100 == 0) {
					ans = "Possible";
				}
			}
		}

		out << "Case #" << i + 1 << ": " << ans << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
