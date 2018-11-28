#include <iostream>
#include <string>
#include <vector>

using namespace std;

char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	freopen("inp.txt", "r", stdin);	
	freopen("outp.txt", "w", stdout);
	int t;
	string s;
	cin >> t;
	getline(cin, s);
	for (int i=0;i<t;i++)
	{
		getline(cin, s);
		for (int j=0;j<s.size();j++)
			if (s[j] != ' ')
				s[j] = map[s[j]-'a'];
		cout << "Case #"<< i+1 << ": " << s << endl;
	}
	
	return 0;
}