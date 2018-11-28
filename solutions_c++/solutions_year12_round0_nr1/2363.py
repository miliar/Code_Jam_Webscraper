#include <iostream>
using namespace std;

const char* map = "yhesocvxduiglbkrztnwjpfmaq";

int n;
string s;

int main()
{
	cin >> n;
	getline(cin, s);
	for (int i=1; i<=n; ++i)
	{
		cout << "Case #" << i << ": ";
		getline(cin, s);
		for (int j=0; j<s.length(); ++j)
			if (s[j] >= 'a' && s[j] <= 'z')
				cout << map[s[j]-'a'];
			else
				cout << s[j];
		cout << endl;
	}
	return 0;
}
