#include <iostream>

using namespace std;

//#define __TEST

int main() {
	int T, N, K;
	int p, s;
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		cin >> K;
		
		p = 1;
		s = 0;	
#ifdef __TEST
		cout << "N: " << N << " K: " << K << endl;
#endif
	
		for (int j = 0; j < K; j++) {
			s = s ^ p;
			p = -1;
			if (s == 0) {
				p = 1;
#ifdef __TEST					
					cout << "[NOPE] j: " << j << " s: " << s << " p: " << p << endl;		
#endif
			} else {
				for (int k = 0; k < N; k++) {
#ifdef __TEST					
					cout << "(1 << k): " << (1 << k) << " s&(1 << k): " << (s&(1 << k)) << endl;
#endif
					if ((s & (1 << k)) == 0) {
						p = (1 << (k + 1)) - 1;
#ifdef __TEST					
					cout << "[HERE] j: " << j << " k: " << k << " s: " << s << " p: " << p << endl;		
#endif
						break;
					}
				}
				if (p == -1)
					p = (1 << (N+1)) - 1;
			}
			//p = (((p & s) << 1) | 1) & ((1 << N) - 1);
#ifdef __TEST
			cout << "j: " << j << " s: " << s << " p: " << p;
			if (((1 << (N-1)) & p & s) != 0)
				cout << " ON" << endl;
			else 
				cout << endl;
#endif			
		}

		cout << "Case #" << (i+1) << ": ";
		if (((1 << (N-1)) & p & s) != 0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	
	return 0;	
}
