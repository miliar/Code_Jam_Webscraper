#include <iostream>
#include <map>

using namespace std;

int main() {
	char diccionari[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
	string linia;
	int casos;
	cin >> casos;
	
	getline(cin,linia);
	for (int i=0; i<casos; ++i) {
		getline(cin, linia);
		string traduit;
		for (int j=0; j<linia.size(); ++j) {
			if (linia[j] == ' ') {
				traduit += ' ';
			} else {
				traduit += diccionari[(int)linia[j] - 'a'];
			}
		}
		cout << "Case #" << i+1 << ": " << traduit << endl;
	}
}