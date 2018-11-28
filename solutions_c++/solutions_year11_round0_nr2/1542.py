#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);
	int cas = 0;
	for(cas = 1; cas <= T; cas++)
	{
		int C, D, N;
		cin >> C;
		int i, j;
		vector <string> comb(C);
		for(i = 0; i < C; i++)
			cin >> comb[i];
		cin >> D;
		vector <string> opp(D);
		for(i = 0; i < D; i++)
			cin >> opp[i];
		cin >> N;
		string s;
		cin >> s;
		string cur = "";
		cur += s[0];
		
		for(i = 1; i < s.size(); i++)
		{
			cur += s[i];
			//cout << cur << "\t";
			if(s.size() <= 1)
				continue;
			bool done = false;
			for(j = 0; j < comb.size(); j++)
			{
				if((cur[cur.size() - 2] == comb[j][0] && cur[cur.size() - 1] == comb[j][1]) || (cur[cur.size() - 2] == comb[j][1] && cur[cur.size() - 1] == comb[j][0]))	
				{
					cur = cur.substr(0, cur.size() - 2);
					cur += comb[j][2];
					done = true;
					break;
				}
			}
			//cout << cur << "\t";
			if(!done)
			{
				for(j = 0; j < opp.size(); j++)
				{
					if(cur.find(opp[j][0]) != string::npos && cur.find(opp[j][1]) != string::npos)
					{
						cur = "";
						break;
					}
				}
			}
			//cout << cur << endl;
		}
		cout << "Case #" << cas << ": [";
		if(cur.size() == 0)
			cout << "]\n";
		for(i = 0; i < cur.size(); i++)
			if(i != cur.size() - 1)
				cout << cur[i] << ", ";
			else
				cout << cur[i] << "]\n";
	}
	return 0;
}
