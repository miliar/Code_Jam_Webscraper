#include <iostream>

using namespace std;

int main(){
	int cases;
	char myChars[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
	string s;
	cin >> cases;

	getline(cin, s); //empty line
	for(int i=0;i<(int)cases;i++){
		getline(cin, s);
		cout << "Case #" << (i+1) << ": ";
		for(int j=0;j<(int)s.size();j++){
			if(s[j] == ' ') cout << ' ';
			else cout << myChars[(int)s[j] - 'a'];
		}
		if(i != (cases - 1)) cout << endl;
	}
}