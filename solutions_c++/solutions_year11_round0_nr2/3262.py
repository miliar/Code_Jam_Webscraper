#include <iostream>
#include <algorithm>
#include <string>
#include <list>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0 ; i < T ; i ++)
	{
		int C;
		cin >> C;
		vector<string> vc(C);
		for (int j = 0 ; j < C ; j ++)
			cin >> vc[j];

		int D;
		cin >> D;
		vector<string> vd(D);
		for (int j = 0 ; j < D ; j ++)
			cin >> vd[j];

		int _;
		cin >> _;
		string s;
		cin >> s;

		list<char> l;

		for (int j = 0 ; j < s.length() ; j ++)
		{
			l.push_back(s[j]);

			list<char>::reverse_iterator il = l.rbegin();
			char el1 = *il;
			++ il;

			if (il != l.rend())
			{
				bool flag = false;
				char el2 = *il;

				// replace
				for (int k = 0 ; k < C ; k ++)
				{
					if ((el1 == vc[k][0] && el2 == vc[k][1]) || (el1 == vc[k][1] && el2 == vc[k][0]))
					{
						l.pop_back();
						l.pop_back();
						l.push_back(vc[k][2]);
						flag = true;
						break;
					}
				}

				// opposed
				if (!flag)
				{
					for (int k = 0 ; k < D ; k ++)
					{
						int q = 2;
						if (el1 == vd[k][0])
							q = 1;
						else if (el1 == vd[k][1])
							q = 0;

						if (q != 2)
						{
							list<char>::iterator itf = find(l.begin(), l.end(), vd[k][q]);
							if (itf != l.end())
							{
								l.clear();
								break;
							}
						}
					}
				}
			}
		}

		list<char>::iterator itl = l.begin();
		cout << "Case #" << i+1 << ": [";
		while (itl != l.end())
		{
			cout << *itl ++;
			if (itl != l.end())
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
