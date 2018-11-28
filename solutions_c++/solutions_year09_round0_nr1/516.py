#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
	int l, d, n, k;
	int t;
	int i, j;
	string s;
	char c, a;
	vector <string> words;
	vector <string> test;
	int exist;

	// read l, d, n	
	cin >> l >> d >> n;

	// read words
	for(i=0; i<d; i++) {
		s.clear();
		cin >> s;
		words.push_back(s);
	}
	c=getchar();

	for(t=1; t<=n; t++) {

		// inti test
		test.clear();
		k=0;

		// read test
		c=getchar();
		while(c!='\n') {
			// the letter is known
			if(c!='(') {
				s.clear();
				s.push_back(c);
				test.push_back(s);
				c=getchar();
			}
			else {
				// the letter is not known
				c=getchar();
				s.clear();
				while(c!=')') {
					s.push_back(c);
					c=getchar();
				}
				test.push_back(s);
				c=getchar();
			}
		}

		for (i=0; i<d; i++) {
			exist = 1;
			for (j=0; j<l; j++) {
				if(find(test[j].begin(), test[j].end(), words[i][j]) == test[j].end())
					exist = 0;
			}
			if(exist==1)
				k++;
		}

		cout << "Case #" << t << ": " << k << endl;	
	}

	return 0;
}