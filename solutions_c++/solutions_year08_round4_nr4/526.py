#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int k, i, j, p[5], r = 1000000000;
		string s;
		
		cin >> k >> s;
		
		for (i = 0; i < k; i++) p[i] = i;
		do {
			string t = s;
			int r1 = 0;
			
			for (i = 0; i < s.size() / k; i++) {
				for (j = 0; j < k; j++) {
					t[i * k + j] = s[i * k + p[j]];
				}
			}
			for (i = 0; i < t.size(); i++) {
				if (!i || t[i - 1] != t[i]) r1++;
			}
			r = min(r, r1);
		} while (next_permutation(p, p + k));
		
		cout << "Case #" << it << ": " << r << '\n';
	}
	
	return 0;
}
