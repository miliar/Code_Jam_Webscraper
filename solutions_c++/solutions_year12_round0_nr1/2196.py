//#include <iostream>
#include <fstream>
using namespace std;

ifstream cin("A-small.in");
ofstream cout("A-small.out");

char M[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main () {
	int T; cin >> T >> ws;
	for (int t=0; t<T; t++) {
		string s;
		getline(cin, s);
		for (int i=0; i<s.length(); i++)
			if (s[i]!=' ')
				s[i] = M[s[i]-'a'];
		cout << "Case #" << t+1 << ": " << s << endl;
	}
}
