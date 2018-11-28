#include <iostream>
#include <cstdio>
using namespace std;

char s[26] =  {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

main()
{
	string p;
	int n, i, j;
	cin >> n;
	getchar();
	for (i = 0; i < n; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		getline(cin, p);
		//cout << "P: " << p << endl;
		for (j = 0; j < p.size(); ++j)
		{
			if (p[j] == ' ')
				cout << ' ';
			else
			{
				cout << s[p[j]-'a'];
			}
		}
		cout << endl;
	}
}




