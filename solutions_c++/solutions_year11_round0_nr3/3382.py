#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

	#define cin fin
	#define cout fout
	ifstream fin("C-large.in");
	ofstream fout("C.out");

int main() {
	int cs; cin >> cs;
	for (int cn=1; cn<=cs; ++cn) {
		int N; cin >> N;
		long long X = 0, S = 0, M = 1e18;
		for (int i=0; i<N; ++i) {
			int n; cin >> n;
			X ^= n;
			S += n;
			M <?= n;
		}

		if (X != 0)
			cout << "Case #" << cn << ": NO\n";
		else
		    cout << "Case #" << cn << ": " << S - M << '\n';
	}
	system("pause");
	return 0;
}
