#include <iostream>

using namespace std;

int main() {
	int T, N, S, p, ti;
	int iT, iN;
	int med, mod;
	int a = 0, q = 0;

	cin >> T;
	for(iT = 1; iT <= T; iT++) {
		q = 0;
		a = 0;
		cin >> N >> S >> p;

		for(iN = 0; iN < N; iN++) {
			cin >> ti;

			if(ti == 0) { if(p == 0) q++; continue; }
			if(ti == 1) { if(p <= 1) q++; continue; }

			med = ti / 3;
			mod = ti % 3;

			if(p <= med) q++;
			else if (p - med == 1) {
				if (mod == 0) a++;
				else if(mod > 0) q++;
			}
			else if (p - med == 2 && mod == 2) a++;
		}

		cout << "Case #" << iT << ": " << q+min(a,S) << endl;
	}


}
