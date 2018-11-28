#include <iostream>
#include <string>
#include <cstdio>
#include <cctype>
using namespace std;

int main()
{
	int n;
	string s;
	char replace[] = "yhesocvxduiglbkrztnwjpfmaq";

	cin >> n;
	getline(cin, s);

	for (int j = 1; j <= n; j++) {
		getline(cin, s);
		for (int i = 0; i < s.size(); i++) {
			if (isspace(s[i]))
				continue;
			s[i] = replace[s[i]-'a'];
		}
		printf("Case #%d: ", j);
		cout << s << endl;
	}

	return 0;
}
