// Sunny Basi 
//
// you found your way here!
//

#include <iostream>
#include <utility>
#include <list>
#include <string>
using namespace std;

int main(){
	// Translation Table
	char tt[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}; 

	int N; cin >> N;
	string temp; getline (cin, temp); // quick move string buffer to next line
	for (int n = 1; n <= N; n++) {
		cout << "Case #" << n << ": ";
		
		string l; getline(cin, l);
		for (int i = 0; i < l.length(); i++) {
			if (l[i] == ' ') cout << ' ';
			else cout << tt[l[i] - 'a'];
		}
		
		cout << endl;
	}
	return 0;
}

