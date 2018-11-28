#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 104;

int solve() {
	int n;
	cin >> n;	
	int nb = 0, no = 0;
	vector<int> b;
	b.assign(n, 0);
	vector<int> o;
	o.assign(n, 0);
	vector<int> p;
	p.assign(n, 0);
	for (int i = 0; i < n; ++i) {
		char color;
		cin >> color;
		int pos;
		cin >> pos;
		if (color == 'O') {
			o[no++] = pos;
			p[i] = 0;
		} else {
			b[nb++] = pos;
			p[i] = 1;
		}
	}
	int io = 0, ib = 0, curO = 1, curB = 1;
	int result = 0;
	for (int i = 0; i < n; ++i) {
		if (p[i] == 0) {		// O
			int nMove = abs(curO - o[io]) + 1;
			curO = o[io++];
			
			if (nMove >= abs(curB - b[ib])) curB = b[ib];
			else 
				if (curB > b[ib]) curB -= nMove;
				else curB += nMove;
			
			result += nMove;
		} else {				// B
			int nMove = abs(curB - b[ib]) + 1;
			curB = b[ib++];

			if (nMove >= abs(curO - o[io])) curO = o[io];
			else 
				if (curO > o[io]) curO -= nMove;
				else curO += nMove;
			
			result += nMove;
		}
	}
	return result;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}


