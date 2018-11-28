#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

typedef unsigned nat;

int main() {

	nat tc;
	cin >> tc;
	for (nat cs  = 0; cs != tc; ++cs) {
		nat k;
		cin >> k;
		string s;
		cin >> s;

		vector<nat> A(k);
		for (nat i = 0; i != k; ++i)
			A[i] = i;

		vector<char> ans(s.size());
		nat mn = 1000000000;
		do {
			for (nat j = 0; j < s.size(); j+= k) {
				for (nat i = 0; i != k; ++i)
					ans[j+i] = s[j+A[i]];
			}
			nat sz = 0;
			for (nat i = 0; i != s.size();) {
				char x = ans[i];
				while (ans[i] == x && i < s.size())
					++i;
				++sz;
			}

			if (sz < mn)
				mn = sz;
		} while (next_permutation(A.begin(), A.end()));

		printf("Case #%u: %u\n", cs+1, mn);
	}

	return 0;
}




