#include <iostream>
using namespace std;

int abs(int n) { if (n < 0) return -n; return n; }

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int N;
		cin >> N;
		int o = 1, b = 1;
		int move = 0;
		int last = 0, since = 0;
		bool ostick = 0, bstick = 0;
		for (int i = 0; i < N; i++) {
			char r;
			int p;
			cin >> r >> p;
			if (r == 'O') {
				//use last move to reduce
				if (ostick) {
					last = abs(o-p) + 1;
					since += last;
					move += last;
				}
				else {
					last = max(0,abs(o-p)-since) + 1;
					since = last;
					move += last;
				}
				o = p;
				ostick = 1;
				bstick = 0;
			}
			if (r == 'B') {
				if (bstick) {
					last = abs(b-p) + 1;
					since += last;
					move += last;
				}
				else {
					last = max(0,abs(b-p)-since) + 1;
					since = last;
					move += last;
				}
				b = p;
				bstick = 1;
				ostick = 0;
			}
			//cout << o << " " << b << " " << move << endl;
		}
		
		cout << "Case #" << icase << ": " << move << endl;
	}
	return 0;
}
