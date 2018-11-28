#include<iostream>
#include<string>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<map>
using namespace std;
string SS = "yhesocvxduiglbkrztnwjpfmaq";


int main() {
	int n;
	string s;
	cin >> n;
	getline(cin,s);
	for (int i=0; i<n; i++) {
		getline(cin,s);
		cout << "Case #" << i+1 << ": ";
		for (int j=0;j<s.size();j++) {
			if (s[j]!=' ')
				cout << SS[s[j]-97];
			else cout << ' ';
		}
		cout << endl;
	}
	return 0;
}
