#include<iostream>
#include<string>

using namespace std;

// Get table from samples?
//#define CREATE_TAB
char map[256];

int main()
{
#ifdef CREATE_TAB
	for(int i = 0; i < 255; ++i)	map[i] = '~';

	int n;
	cin >> n;

	string s, t;
	getline(cin, s);

	// Reads pairs of encrypted and plain text
	for(int i = 0; i < n; ++i)
	{
		getline(cin, s);
		getline(cin, t);

		for(int i = 0; i < s.size(); ++i)	map[s[i]] = t[i];
	}

	for(int i = 'a'; i <= 'z'; ++i)	cout << map[i];
	cout << endl;
#else
	// Table created by above code
	string s = "yhesocvxduiglbkrztnwjpfma";
	
	// Missing character for z can be deduced as it is the only missing character
	// and all characters need to appear
	s += "q";

	for(int i = 0; i < s.size(); ++i)	map['a' + i] = s[i];
	map[' '] = ' ';

	int N;
	cin >> N;

	string t;
	getline(cin, t);

	for(int i = 0; i < N; ++i)
	{
		getline(cin, t);
		for(int j = 0; j < t.size(); ++j)	t[j] = map[t[j]];
		cout << "Case #" << (i + 1) << ": " << t << endl;
	}
#endif
	return 0;
}
