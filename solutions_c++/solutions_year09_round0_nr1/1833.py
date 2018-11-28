#include <iostream>
#include <string>

using namespace std;

int main(){
	int L,D,N;
    cin >> L >> D >> N;

	string words[D];
	for (int d = 0; d < D; ++d) {
		cin >> words[d];
	}
	
	for (int n = 1; n <= N; ++n) {
		string pattern;
		cin >> pattern;
		
		int tbl[L];
		int pos = 0;
		for (int l = 0; l < L; ++l) {
			if (pattern[pos] == '(') {
				++pos;
				for (tbl[l] = 0; pattern[pos] != ')'; ++pos) {
					tbl[l] |= 1 << (pattern[pos] - 'a');
				}
			} else {
				tbl[l] = 1 << (pattern[pos] - 'a');
			}
			++pos;
		}
		
		int match;
		match = 0;
		for (int d = 0; d < D; ++d) {
			bool ok = true;
			for (int l = 0; l < L; ++l) {
				if ((tbl[l] & (1 << (words[d][l] - 'a'))) == 0) {
					ok = false;
					break;
				}
			}
			if (ok) {
				++match;
			}
		}
		cout << "Case #" << n << ": " << match << endl;
	}
}
