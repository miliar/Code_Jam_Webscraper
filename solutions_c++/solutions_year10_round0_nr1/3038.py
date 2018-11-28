#include <iostream>

using namespace std;

unsigned long long squares[64];

inline bool calculate(int snap, int k) {
	int calc = squares[snap] - 1;
	float val = (k + 1) / (float)(calc + 1);	
	return k >= calc && val == (int) val;
}

inline void generateSquares() {
	squares[0] = 1;
	for(int i = 1; i < 64; i++) {
		squares[i] = 2 * squares[i - 1];
	}
}

int main(int argc, char *argv[]) {
	generateSquares();
	int n, nSnappers, k;
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> nSnappers >> k;
		if(k == 0) 
			cout << "Case #" << i + 1 << ": OFF" << endl;
		else {
			if(calculate(nSnappers, k))
				cout << "Case #" << i + 1 << ": ON" << endl;
			else
				cout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}
	return 0;
}
