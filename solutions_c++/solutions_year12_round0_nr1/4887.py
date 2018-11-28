#include <iostream>
#include <string>
using namespace std;

char a[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
string s;
int n;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n;
	getline(cin, s);
	for (int i = 0; i < n; i++) 
	{
		getline(cin, s);
		for (int j = 0; j < s.size(); j++)
			if (s[j] != ' ') s[j] = a[s[j] - 'a'];
		cout << "Case #" << i + 1 << ": " << s << endl;
	}
	return 0;
}