#include <iostream>
#include <set>
#include <string>
using namespace std;

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz"; // -___- q <-> z
string b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq", str;

string solve()
{
	getline(cin, str);
	string ret;
	for (int i=0; i<str.length(); i++)
		for (int j=0; j<a.length(); j++)
			if (a[j] == str[i])
				ret += b.substr(j,1), j = a.length();
	return ret;
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	getline(cin, str);
	for (int x=1; x<=T; x++) printf("Case #%d: %s\n", x, solve().c_str());
}