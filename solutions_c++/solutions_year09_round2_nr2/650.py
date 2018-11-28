#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		cin >> s;
		if (!next_permutation(s.begin(), s.end())) {
			s.insert(0, "0");
			for (int i = 0; i < (int) s.length(); ++i) if (s[i] != '0') {
				char t = s[i];
				s[i] = '0';
				s[0] = t;
				break;
			}
		}
		cout << "Case #" << (i + 1) << ": " << s << endl;
	}
}
