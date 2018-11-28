#include <iostream>
#include <string>
using namespace std;

char alpha[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char goo[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {
	int numCases(0);
	string junk, str;
	cin >> numCases;
	getline(cin, junk);

	for(int i = 1; i <= numCases; i++) {
		getline(cin, str);
		int index(0);
		for(int j = 0; j < str.length(); j++) {
			if(str[j] != ' ') {
				for(int k = 0; k < 26; k++) {
					if(str[j] == alpha[k]) {
						index = k;
						break;
					}
				}
				str[j] = goo[index];
			}
		}

		cout << "Case #" << i << ": " << str << endl;
	}


}


