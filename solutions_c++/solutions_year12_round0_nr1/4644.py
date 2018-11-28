#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

char ch[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("A-small-attempt1.in", "rt" ,stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	int m;
	cin >> m;
	string s;
	getline(cin, s);
	for (int i=0; i < m; i++)
	{
		getline(cin, s);
		int n = s.size();
		for (int j=0; j<n; j++)
			if (s[j] != ' ')
				s[j] = ch[s[j] - 'a'];
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	return 0;
}