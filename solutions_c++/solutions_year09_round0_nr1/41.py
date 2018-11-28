#define PROBLEM "A"
#define PATH "d:\\code\\gcj09\\"
#define INPUTFILE "D:\\code\\gcj09\\A-large.in" //PATH PROBLEM ".in"
#define OUTPUTFILE INPUTFILE ".out.txt"

#include <vector>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
int GI() { int t; scanf("%d", &t); return t; }

const int MaxL = 15, MaxD = 5000, MaxNodes = MaxL * MaxD;
int Trie [MaxNodes + 1][26], Nodes = 1;
int L, D, N;

int main()
{
	assert (freopen (INPUTFILE, "r", stdin));
	assert (freopen (OUTPUTFILE, "w", stdout));
	L = GI(); D = GI(); N = GI();
	while (D -- )
	{
		string s;
		cin >> s;
		int x = 0;
		for (int i = 0; i < s.size(); ++ i)
		{
			int a = s[i] - 'a';
			if (!Trie[x][a])
			{
				Trie[x][a] = Nodes;
				memset(Trie[Nodes], 0, sizeof(Trie[Nodes]));
				Nodes ++;
			}
			x = Trie[x][a];
		}
	}

	int kase = 1;
	while (N --)
	{
		cout << "Case #" << kase ++ << ": ";
		vector <int> poss (1, 0);
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); )
		{
			vector <int> edges;
			if (s[i] != '(')
			{
				edges.push_back(s[i] - 'a');
				i ++;
			}
			else
			{
				while (s[i ++] != ')')
				{
					int a = s[i] - 'a';
					if (a <0 || a >= 26) continue;
					edges.push_back(a);
				}
			}

			vector<int> nposs;
			for (int i = 0; i < poss.size(); ++ i)
			{
				for (int e = 0; e < edges.size(); ++ e)
				{
					int x = poss[i], a = edges[e];
					if (Trie[x][a])
					{
						nposs.push_back(Trie[x][a]);
					}
				}
			}
			poss = nposs;
		}

		cout << poss.size() << endl;
	}
	return 0;
}