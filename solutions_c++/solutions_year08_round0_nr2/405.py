#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int parseTime(string st)
{
	return ((st[0]-'0')*10+st[1]-'0')*60 + (st[3]-'0')*10+st[4]-'0';
}

int main()
{
	int tC;
	cin >> tC;

	for (int tcase=1;tcase<=tC;tcase++)
	{
		int T, NA, NB;
		vector< pair<int,int> > tab;

		cin >> T >> NA >> NB;

		for (int i=0;i<NA;i++)
		{
			string st, et;
			cin >> st >> et;
			tab.push_back(make_pair(parseTime(st),1));
			tab.push_back(make_pair(parseTime(et)+T,-2));
		}
		
		for (int i=0;i<NB;i++)
		{
			string st, et;
			cin >> st >> et;
			tab.push_back(make_pair(parseTime(st),2));
			tab.push_back(make_pair(parseTime(et)+T,-1));
		}
		
		sort(tab.begin(), tab.end());

		int resA = 0, resB = 0, rA = 0, rB = 0;
		for (int i=0;i<tab.size();i++)
			switch (tab[i].second)
			{
				case -1: rA++; break;
				case -2: rB++; break;
				case 1: if (rA-1<0) resA++, rA++; rA--; break;
				case 2: if (rB-1<0) resB++, rB++; rB--; break;
			}

		cout << "Case #" << tcase << ": " << resA << " " << resB << endl;
	}

	return 0;
}
