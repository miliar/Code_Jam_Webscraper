#include <iostream>
#include <string>
using namespace std;

int main() {

	char orig[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char newar[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	int cases;
	cin >> cases;
	
	string str;
	getline(cin, str);
	char c, print;
	int z;
	for(int i = 0; i < cases; i++) {
		getline(cin, str);
		cout << "Case #" << i + 1 << ": ";
		for(int j = 0; j < str.length(); j++) {
			c = str[j];
			z = 0;
			while(1) {
				if(c == ' ') {
					print = ' ';
					break;
				}
				if(orig[z] == c) {
					print = newar[z];
					break;
				}
				z++;
			}
		
			cout << print;
		}
		cout << endl;
	}
	
	return 0;
}
