#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
using namespace std;

int tests;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tests;

	for (int i = 0; i < tests; i++)
	{
		int a, b;
		cin >> a >> b;

		char aChars[15];
		itoa(a, aChars, 10);
		string aNum = aChars;

		char bChars[15];
		itoa(b, bChars, 10);
		string bNum = bChars;

		int answer = 0;

		for (int j = a; j <= b; j++)
		{
			char buffer[15];
			itoa(j, buffer, 10);
			string num = buffer;

			set<string> used;

			for (int indent = 1; indent < num.length(); indent++)
			{
				string cycled = num.substr(indent) + num.substr(0, indent);
				if (cycled[0] == '0') continue;
				if (num < cycled && cycled <= bNum && used.find(cycled) == used.end())
				{
					answer++;
					used.insert(cycled);
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << answer << endl;
	}

	return 0;
}