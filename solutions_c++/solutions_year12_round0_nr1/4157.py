#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
const char _trans[]="yhesocvxduiglbkrztnwjpfmaq";
const char *trans = _trans - 'a';
string s;
int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);

	int T;
	cin >> T; getline(cin, s);
	for (int i = 1; i <= T; i++)
	{
		getline(cin, s);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < s.length(); j++)
			if (s[j] != ' ')
				cout << trans[s[j]];
			else
				cout << ' ';
		cout << endl;
	}
	//fclose(stdin); fclose(stdout);
	return 0;
}
