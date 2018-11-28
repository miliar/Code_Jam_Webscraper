#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T, testid;
int N, M;
bool in[20000][26];
string word[20000];
string per;

bool isSame(string & s1, string & s2, set<char> added)
{
	if (s1.length() != s2.length()) return false;
	for (int i = 0; i < s1.length(); ++i)
		if (s1[i] != s2[i] && (added.find(s1[i]) != added.end() || added.find(s2[i]) != added.end())) 
			return false;
	return true;
}

void init()
{
	cin >> N >> M;
	for (int i = 0; i < N; ++i) 
		cin >> word[i];

	cout << "Case #" << testid << ": ";

	for (int i = 0; i < M; ++i)
	{
		cin >> per;
		int maxpoint = 0;
		string ans = word[0];

		for (int j = 0; j < N; ++j)
		{
			int nowpoint = 0;
			int L = word[j].length();
			set<int> validid;
			for (int k = 0; k < N; ++k)
				if (word[k].length() == L) 
					validid.insert(k);

			int off = 0;
			set<char> added;
			while (validid.size() > 1 && off < per.length())
			{
				added.insert(per[off]);
				off++;

				set<int> newvalid;
				for (set<int>::iterator itr = validid.begin(); itr != validid.end(); ++itr)
				{
					int id = *itr;
					if (isSame(word[id], word[j], added)) newvalid.insert(id);
				}

				bool contained = false;
				for (int m = 0; m < word[j].length(); ++m)
					if (word[j][m] == per[off - 1]) 
						contained = true;

				//debug4(validid.size(), newvalid.size(), per[off - 1], contained);
				if (newvalid.size() < validid.size() && !contained) 
				{
					nowpoint++;
				}
				validid = newvalid;
			}

			//debug2(nowpoint, word[j]);
			if (nowpoint > maxpoint)
			{
				maxpoint = nowpoint;
				ans = word[j];
			}
		}
		cout << ans << " ";
	}
	cout << endl;
}

void york()
{
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}



