#include <iostream>
#include <string>

using namespace std;

int
main(void)
{
	char c[26] = { 'y', 'h', 'e', 's', 'o',
				   'c', 'v', 'x', 'd', 'u',
				   'i', 'g', 'l', 'b', 'k',
				   'r', 'z', 't', 'n', 'w',
				   'j', 'p', 'f', 'm', 'a',
				   'q' };
	int t;
	string s;

	cin >> t;
	getline(cin, s);
	for (int n = 0; n < t; n++) {
		getline(cin, s);
		for (unsigned int i = 0; i < s.length(); i++) {
            if (s[i] >= 'a' && s[i] <= 'z')
                s[i] = c[s[i] - 'a'];
		}
		cout << "Case #" << (n+1) << ": " << s << endl;
	}

	return 0;
}
