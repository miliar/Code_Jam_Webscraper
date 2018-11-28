#include <string>
#include <map>
#include <iostream>
#include <set>

using namespace std;

int main(){
	int T;
	cin >> T;

	for (int tt = 0; tt < T; ++tt){
		string S;
		cin >> S;

		set <char> tx;
		tx.clear();
		for (int i = 0; i < S.size(); ++i) tx.insert(S[i]);
		long long base = tx.size();
		if (base == 1) base = 2;

		long long sol = 0;
		int digitsUsed = 0;
		map <char, int> digits;
		digits.clear();
		for (int i = 0; i < S.size(); ++i){
			if (digits.count(S[i]) == 0){
				if (digitsUsed == 0){
					digits[S[i]] = 1;
				}else if (digitsUsed == 1){
					digits[S[i]] = 0;
				}else{
					digits[S[i]] = digitsUsed;
				}
				++digitsUsed;
			}

			sol = sol*base + digits[S[i]];
		}
		printf("Case #%d: %lld\n", tt+1, sol);
	}

	return 0;
}
