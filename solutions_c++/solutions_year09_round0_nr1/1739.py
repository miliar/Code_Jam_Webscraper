#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef pair<int, int> ii;

string tok;
int id;
int l, d, n;

map<string, int> m;
vector<char> var[20];

void nexttok(int i)
{
	var[i].clear();
	if (tok[id] != '(')
	{
		var[i].push_back(tok[id]);
		id++;
		return;
	}
	id++;
	while (tok[id] != ')')
	{
		var[i].push_back(tok[id]);
		id++;
	}
	id++;
}

int ans;

void check(int id, string& prev)
{
	if (id == l)
	{
		ans++;
		return;
	}
	for (int i = 0; i < var[id].size(); ++i)
	{
		prev.push_back(var[id][i]);
		if (m[prev] > 0)
			check(id+1, prev);
		prev.erase(prev.end()-1);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	cin >> l >> d >> n;
	for (int i = 0; i < d; ++i)
	{
		string v;
		cin >> v;
		for (int j = 1; j <= l; ++j)
			m[string(v.begin(), v.begin()+j)]++;
	}
	for (int i = 0; i < n; ++i)
	{
		cin >> tok;
		id = 0;
		for (int j = 0; j < l; ++j)
			nexttok(j);
		ans = 0;
		string st = "";
		check(0, st);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}