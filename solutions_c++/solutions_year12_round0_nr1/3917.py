#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	//freopen("a.in", "r", stdin);
	//freopen("a.out", "w", stdout);

	char g[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int  n;
	cin >> n;
	getchar();
	for (int i = 1; i <= n; i++)
	{
		char s[120];
		gets(s);
		int len = strlen(s);
		cout << "Case #" << i << ": ";
		for (int i = 0; i < len; i++)
		{
			printf("%c", s[i] == ' ' ? ' ' : g[s[i]-'a']);
		}
		cout << endl;
	}

	return 0;
}
