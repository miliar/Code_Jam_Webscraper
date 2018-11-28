// Sunny Basi 
//
// you found your way here!
//

#include <cmath>
#include <iostream>
#include <utility>
#include <list>
#include <sstream>
#include <string>
using namespace std;

string itos(int num) {
	stringstream ss;
	ss << num;
	return ss.str();
}

string shift(string s) {
	int len = s.length();
	char last = s[len-1];	
	for (int i = len-1; i > 0; i--) {
		s[i] = s[i-1];
	}
	s[0] = last;
	return s;
}

bool check(int m, int n){
	if (m == n) return false;
	string M = itos(m);
	string N = itos(n);
	
	M = shift(M);
	for (int i = 0; i < M.length(); i++) {
		if (M.compare(N) == 0) return true;
		M = shift(M);
	}

	return false;
}

int main(){
	int T; cin >> T;
	for (int n = 1; n <= T; n++) {
		int A, B; cin >> A >> B;
		int tot = 0;

		for (int a = A; a <= B; a++) {
			for (int b = A; b < a; b++) {
				if (check(a,b)) tot++;
			}
		}

		cout << "Case #" << n << ": " << tot << endl;
	}
	return 0;
}
