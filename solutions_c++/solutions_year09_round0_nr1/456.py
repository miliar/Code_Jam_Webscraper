#include <iostream>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;

const int MAXL = 15;
const int CNUM = 26;

bool ptn[MAXL][CNUM];
vector<string> dict;

int main()
{
	int l, d, n, i, j, cn, res;
	string t;

	cin >> l >> d >> n;
	getline(cin, t);

	dict.resize(d);

	for (i = 0; i < d; i++)
		getline(cin, dict[i]);

	for (cn = 1; cn <= n; cn++)
	{
		res = 0;
		memset(ptn, 0, sizeof(ptn));
		getline(cin, t);

		i = 0;
		for (string::iterator it = t.begin(); it != t.end(); it++, i++)
			if (*it == '(')
			{
				it++;
				while (*it != ')')
				{
					ptn[i][*it - 'a'] = true;
					it++;
				}
			}
			else
				ptn[i][*it - 'a'] = true;

		for (i = 0; i < d; i++)
		{
			for (j = 0; j < l; j++)
				if (!ptn[j][dict[i][j] - 'a'])
					break;
			if (j == l)
				res++;
		}

		cout << "Case #" << cn << ": " << res << endl;
	}

	return 0;
}
