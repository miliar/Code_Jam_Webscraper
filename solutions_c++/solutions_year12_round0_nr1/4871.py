#include <iostream>
#include <string>


using namespace std;

int main()
{
	char Rep[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	cin >> t;
	cin.ignore();
	for (int i = 0; i < t; i++)
	{
		string s;
		getline(cin, s);
		cout << "Case #" << i + 1 << ": ";
		for (int i = 0; i < s.length(); i++)
		{
			if (s[i] >= 'a' && s[i] <= 'z')
				cout << Rep[s[i] - 'a'];
			else
				cout << s[i];
		}
		cout << endl;
	}
}