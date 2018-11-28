#include <iostream>
#include <string>

using namespace std;

int main()
{
	char f[64] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	int T;
	cin >> T;

	string str;
	getline(cin, str);

	for (int i = 0; i < T; i++)
	{
		cout << "Case #";
		cout << i + 1;
		cout << ": ";

		getline(cin, str);		

		for (int j = 0; j < str.size(); j++)
		{
			char c = str[j];
			if (c != ' ')
			{
				cout << f[c - 'a'];
			}
			else
			{
				cout << ' ';
			}
		}
		cout << endl;
	}
}