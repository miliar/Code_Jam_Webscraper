#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

map<char,vector<int> > e;
const string S = "welcome to code jam";

void init()
{
	for (int i = 0; i < S.length(); ++i)
	{
		if (e.count(S[i]) == 0)
		{
			vector<int> v;
			e[S[i]] = v;
		}
		e[S[i]].push_back(i);
	}
}

int main()
{
	init();

	int N;
	cin >> N;
	map<char, map<int,ll> > count;
	string s;
	getline(cin,s);
	for (int i = 0; i < N; ++i)
	{
		count.clear();
		getline(cin,s);
		for (int j = 0; j < s.length(); ++j)
		{
			char c = s[j];
			if (e.count(c) == 0)
				continue;
			if (count.count(c) == 0) {
				map<int,ll> m;
				count[c] = m;
			}
			for (int k = 0; k < e[c].size(); ++k)
			{
				if (count[c].count(e[c][k]) == 0)
					count[c][e[c][k]] = 0;
				if (e[c][k] == 0)
					count[c][0] = (count[c][0] + 1) % 10000;
				char prev = S[e[c][k]-1];
				count[c][e[c][k]] += count[prev][e[c][k]-1];				
				count[c][e[c][k]] %= 10000;
			}			
		}
		printf("Case #%d: %.4d\n",i+1,count['m'][S.length()-1]);
	}
}
