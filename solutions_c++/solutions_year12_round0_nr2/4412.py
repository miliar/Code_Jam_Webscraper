#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define fori(i,start,end) for(int(i)=int(start);(i)<int(end);(i)++)
#define all(a) (a).begin(), (a).end()
#define rep(i, end) fori((i), 0, (end))

int main( int argc, char* argv[] ) {
	string S;
	int T;
	cin >> T;
	getline(cin, S); // read the newline character
	for (int case_number = 1; case_number <= T; ++case_number) {
		int N, S, p, t, m = 0;
		cin >> N >> S >> p;
		for (int i = 0; i < N; ++i) {
			cin >> t;
			
			int const quotient = t / 3;
			if (quotient >= p) {
				++m;
				continue;
			}

			int const rem = t % 3;
			
			if (0 == rem) {
				if (quotient >= 1 && quotient + 1 >= p && S > 0) {
					++m;
					--S;
					continue;
				}
			}
			else if (1 == rem) {
				if (quotient + 1 >= p) {
					++m;
					continue;
				}
			}
			else {
				if (quotient + 1 >= p) { // distribute btw. two
					++m;
					continue;
				}
				if (quotient + 2 >= p && S > 0) {
					++m;
					--S;
					continue;
				}
			}
		}
			
		cout << "Case #" << case_number << ": " << m << endl;
	}
}