#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;


int main () {
	int t, T;
	char c;
	string s, s1;
	int i;

	cin >> T;

	for(t=1; t<=T; t++) {

		cout << "Case #" << t << ": ";
		cin >> s;
		s1=s;
		if(next_permutation(s.begin(), s.end()))
			cout << s << endl;
		else {
			sort(s.begin(), s.end());
			s.insert(1, "0");
			for(i=0; i<s.size(); i++)
				if(s[i]!='0') {
					c = s[i];
					s.erase(i, 1);
					s.insert(s.begin(), c);					
					break;
				}
			cout << s << endl;
		}
	}

	return 0;
}