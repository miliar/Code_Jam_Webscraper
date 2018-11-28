#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define R(v,i,k) ((i) - (i) % (k) + (v)[(i) % (k)])

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int k;
		string s;
		cin >> k >> s;

		vector<int> v(k);
		for(int i = 0; i < k; i++) { v[i] = i; }

		int m = s.length();

		do {
			int n = 1;

			for(int i = 0; i < s.length() - 1; i++) {
				n += (s[R(v, i, k)] == s[R(v, i + 1, k)]) ? 0 : 1;
			}

			m = min(m, n);
		}
		while(next_permutation(v.begin(), v.end()));

		cout << "Case #" << iCase << ": " << m << endl;
	}

	return 0;
}
