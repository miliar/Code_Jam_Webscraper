#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t, n;

int bgoals[100];
int ogoals[100];

int which[100];
int num[100];

int max (int x, int y) {
	if (x > y) return x;
	return y;
}

int ab (int x) {
	if (x < 0) return -x;
	return x;
}

int main() {
	in.open("proba.in", fstream::in);
	out.open("proba.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> n; 
		
		char temp;
		int t2;
		int bcount = 0;
		int ocount = 0;
		for (int j = 0; j < n; j++) {
			in >> temp >> t2;
			if (temp == 'B') {
				which[j] = 0;
				bgoals[bcount] = t2;
				num[j] = bcount;
				bcount++;
			} else {
				which[j] = 1;
				ogoals[ocount] = t2;
				num[j] = ocount;
				ocount++;
			}
		}
		int bprev = 1;
		int btprev = 1;
		int oprev = 1;
		int otprev = 1;

		int ans = 1;
		for (int k = 0; k < n; k++) {
			if (which[k] == 0) {
				ans = max(btprev + 1 + ab(bgoals[num[k]] - bprev), otprev + 1);
				bprev = bgoals[num[k]];
				btprev = ans;
			} else if (which[k] == 1) {
				ans = max(otprev + 1 + ab(ogoals[num[k]] - oprev), btprev + 1);
				oprev = ogoals[num[k]];
				otprev = ans;
			}
		}

		out << "Case #" << i + 1 << ": " << ans - 1 << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
