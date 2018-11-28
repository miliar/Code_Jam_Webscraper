#include <iostream>
#include <string>
#include <map>

#define min(a,b) ((a<b)?(a):(b))

using namespace std;

int main()
{
	int n, s, q, count = 1;
	map <string, int> engines;

	cin >> n;
	for (; n>0; n--)
	{
		cin >> s;
		cin.ignore();
		for (int i=0; i<s; i++)
		{
			string str;
			getline(cin, str);
			engines[str] = i;
		}

		int t[s][2];
		int sel=0;
		for (int i = 0; i < s; i++) t[i][sel] = 0;

		cin >> q;
		cin.ignore();
		for (; q>0; q--)
		{
			sel = 1-sel;

			int minimum = 2000;

			for (int i = 0; i < s; i++)
				if (t[i][1-sel] != -1 && t[i][1-sel] < minimum) minimum = t[i][1-sel];

			string str;
			getline(cin, str);

			for (int i = 0; i < s; i++)
				if (engines[str] == i) t[i][sel] = 2000;
				else (t[i][sel] = min(t[i][1-sel], minimum + 1));

		}

		int minimum = 2000;
		for (int i = 0; i < s; i++) if (t[i][sel] < minimum) minimum = t[i][sel];
		cout << "Case #" << count++ << ": " << minimum << endl;
	}

	return 0;
}
