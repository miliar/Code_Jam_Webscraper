#include <iostream>
#include <string>

using namespace std;

char cipher[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 
	'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {

	int T;
	char line[101];
	string G;

	cin >> T;
	cin.getline(line, 101);
	
	for (int n = 1; n <= T; n++) {

		cin.getline(line, 101);
		G = string(line);

		for (string::iterator i = G.begin(); i != G.end(); i++) {
			if (isalpha(*i)) {
				*i = cipher[*i - 'a'];
			}
		}

		cout << "Case #" << n << ": " << G;
		if (n != T) cout << endl;
	}

	return 0;
}