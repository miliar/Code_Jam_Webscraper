#include <algorithm>
#include <iostream>
using namespace std;

#define MAX 30

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T;
	cin >> T;
	for (int test=1; test<=T; ++test) {
		char s[MAX];
		cin >> s;		

		int l=strlen(s);
		
		cout << "Case #" << test << ": ";		
		
		if (next_permutation(s, s+l)) {
			cout << s;
		} else {
			for (int i=0; i<l; ++i)
				if (s[i]!='0') {
					swap(s[0],s[i]);
					break;
				}
			cout << s[0];
			cout << 0;
			for (int i=1; i<l; ++i)
				cout << s[i];
		}

		cout << endl;

	}
	return 0;
}
