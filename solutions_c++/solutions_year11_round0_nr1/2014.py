#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T, N;
	int Pk[100];
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N;
		for(int i=0; i<N; i++) {
			char c;
			cin >> c >> Pk[i];
			if (c == 'B')
				Pk[i] = -Pk[i];
		}
		int ans = 0;
		int lo = 0, lb = 0;
		int po = 1, pb = 1;
		for(;min(lo, lb) < N; ans++) {
			while(lo < N && Pk[lo] < 0) lo++;
			while(lb < N && Pk[lb] > 0) lb++;
			int l = min(lo, lb);
			if (lo < N) {
				if (po == Pk[lo]) lo += lo == l;
				else po += po < Pk[lo] ? 1 : -1;
			}
			if (lb < N) {
				if (pb == -Pk[lb]) lb += lb == l;
				else pb += pb < -Pk[lb] ? 1 : -1;
			}
		}
		/*
		int po = 1, pb = 1;
		int l = 0;
		int lo = 0, lb = 0;
		for(int l=0; l<N; l++) {
			int add = 0;
			if (Pk[l] > 0) {
				add = abs(Pk[l] - po);
				ans += add;
				po = Pk[l];
				lo = l + 1;
				while(lb < N && Pk[lb] > 0)
					lb++;
				if (lb < N) {
					if (abs(-Pk[lb] - pb) <= add)
						pb = -Pk[lb];
					else
						pb += (-Pk[lb]-pb) * (abs(-Pk[lb]-pb) - add) / abs(-Pk[lb]-pb);
				}
			} else {
				add = abs(-Pk[l] - pb);
				ans += add;
				pb = -Pk[l];
				lb = l + 1;
				while(lo < N && Pk[lo] > 0)
					lo++;
				if (lo < N) {
					if (abs(Pk[lo] - po) <= add)
						po = Pk[lo];
					else
						po += (Pk[lo]-po) * (abs(Pk[lo]-po) - add) / abs(Pk[lo]-po);
				}
			}
		}
		*/
		cout << "Case #" << t << ": " << ans << endl;

	}
	return 0;
}

