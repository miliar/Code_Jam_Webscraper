#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

string s1 = "abcdefghijklmnopqrstuvwxyz";
string s2 = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		string s;
		scanf(" ");
		getline(cin, s);
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < (int)s.size(); j++){
			if(s[j] == ' ')
				cout << " ";
			else
				cout << s2[s[j]-'a'];
		}
		cout << endl;
	}
	return 0;
}

