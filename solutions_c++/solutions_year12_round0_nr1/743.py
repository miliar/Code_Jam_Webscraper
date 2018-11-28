#include <iostream>

using namespace std;

char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	int T;
	string s;

	cin >> T >> ws;
	for (int j=0; j<T; ++j){
		cout << "Case #" << j+1 << ": ";
		getline(cin, s);
		for (int i=0; i<s.length();++i){
			if (s[i]==' ')
				cout << ' ';
			else 
				cout << mapping[s[i]-'a'];
		}
		cout << endl;
	}



}
