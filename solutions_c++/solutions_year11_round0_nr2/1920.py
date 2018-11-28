# include <iostream>
# include <deque>
# include <string>
# include <memory.h> 

using namespace std;

int Base2Id(char c)
{
	if (c == 'Q')
		return 0;
	if (c == 'W')
		return 1;
	if (c == 'E')
		return 2;
	if (c == 'R')
		return 3;
	if (c == 'A')
		return 4;
	if (c == 'S')
		return 5;
	if (c == 'D')
		return 6;
	if (c == 'F')
		return 7;
	return 8;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int tests;
	cin >> tests;

	for(int tcase = 1; tcase <= tests; ++tcase)
	{
		char comb[9][9];
		memset(comb, '*', sizeof(comb));
		int c;
		string s;

		cin >> c;
		for (int i = 0; i < c; ++i)
		{
			cin >> s;
			comb[Base2Id(s[0])][Base2Id(s[1])] = s[2];
			comb[Base2Id(s[1])][Base2Id(s[0])] = s[2];
		}

		bool oppos[30][30];
		memset(oppos, false, sizeof(oppos));

		cin >> c;
		for (int i = 0; i < c; ++i)
		{
			cin >> s;
			oppos[s[0] - 'A'][s[1] - 'A'] = true;
			oppos[s[1] - 'A'][s[0] - 'A'] = true;
		}

		cin >> c;
		cin >> s;
		string res;
		int present[30];
		memset(present, 0, sizeof(present));

		for (int i = 0; i < c; ++i)
		{
			res.push_back(s[i]);
			++present[s[i] - 'A'];
			while (res.length() > 1 && comb[Base2Id(res.back())][Base2Id(res[res.length() - 2])] != '*')
			{
				char com = comb[Base2Id(res.back())][Base2Id(res[res.length() - 2])];
				--present[res.back() - 'A'];
				--present[res[res.length() - 2] - 'A'];
				res.pop_back();
				res.back() = com;
				++present[res.back() - 'A'];
			}
	
			if (present[res.back() - 'A'] == 1)
				for (int j = 0; j < 30; ++j)
					if (present[j] && oppos[res.back() - 'A'][j])
					{
						res.clear();
						memset(present, 0, sizeof(present));
						break;
					}
		}

		cout << "Case #" << tcase << ": [";
		for (string::iterator i = res.begin(); i != res.end(); ++i)
		{
			cout << *i;
			if (i != --res.end())
				cout << ", ";
		}
		cout << ']' << endl;		
	}

	return 0;
}