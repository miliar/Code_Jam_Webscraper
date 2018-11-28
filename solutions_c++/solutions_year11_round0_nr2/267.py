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

int T;
int testid;

map<pair<char, char> , char> com;
set<pair<char, char> > rem;

void init()
{
	int C, D, N;
	
	com.clear();
	rem.clear();

	cin >> C;
	for (int i = 0; i < C; ++i)
	{
		string c;
		cin >> c;
		com[make_pair(c[0], c[1])] = c[2];
		com[make_pair(c[1], c[0])] = c[2];
	}

	cin >> D;
	for (int i = 0; i < D; ++i)
	{
		string c;
		cin >> c;
		rem.insert(make_pair(c[0], c[1]));
		rem.insert(make_pair(c[1], c[0]));
	}

	cin >> N;
	string line;
	cin >> line;

	string ans = "";
	for (int i = 0; i < line.length(); ++i)
	{
		ans.append(1, line[i]);
		while (ans.length() >= 2)
		{
			char c1 = ans[ans.length() - 2];
			char c2 = ans[ans.length() - 1];
			pair<char, char> p = make_pair(c1, c2);
			if (com.find(p) != com.end())
			{
				ans = ans.substr(0, ans.length() - 2);
				ans.append(1, com[p]);
			}
			else break;
		}

		for (int x = 0; x < ans.length(); ++x)
			for (int y = x + 1; y < ans.length(); ++y)
				if (rem.find(make_pair(ans[x], ans[y])) != rem.end())
				{
					ans = "";
					break;
				}
	}

	cout << "Case #" << testid << ": ";
	if (ans.length() == 0)
		cout << "[]" << endl;
	else
	{
		cout << "[";
		cout << ans[0];
		for (int i = 1; i < ans.length(); ++i)
			cout << ", " << ans[i];
		cout << "]" << endl;
	}
}

void york()
{
}

int main()
{
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}

	return 0;
}



