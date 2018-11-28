#include <iostream>
#include <string>

using namespace std;

string s = "zyeqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string gs = "qaozour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char map[50];

void translate(std::string& str)
{
	unsigned int i;
	for (i = 0; i < str.size(); ++i)
	{
		str[i] = map[str[i] - 'a'];
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	unsigned int t;
	cin >> t;
	unsigned int i;
	for (i = 0; i < s.size(); ++i)
	{
		map[s[i] - 'a'] = gs[i];
	}

	string input;
	// Read the newline symbol
	getline(cin, input);
	for (i = 1; i <= t; ++i)
	{
		getline(cin, input);
		translate(input);
		cout << "Case #" << i << ": " << input << "\n";
	}
	return 0;
}