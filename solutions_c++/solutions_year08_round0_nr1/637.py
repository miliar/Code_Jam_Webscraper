#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <cstring>

using namespace std;

const int MAXENGINE = 105;
const int MAXQUERY = 1005;

int numOfEngine, numOfQuery;
map<string, int> engine;
int query[MAXQUERY];

void init()
{
	engine.clear();
}

void input()
{
	int i;
	string s;
	// input engines
	cin >> numOfEngine;
	cin.get();
	for (i = 0; i < numOfEngine; i++) {
		getline(cin, s);
		engine[s] = i;
		//cout << "E: " << s << " " << engine[s] << endl;
	}

	// input queries.
	cin >> numOfQuery;
	cin.get();
	for (i = 0; i < numOfQuery; i++) {
		getline(cin, s);
		query[i] = engine[s];
		//cout << "Q: " << s << " " << query[i] << endl;
	}
}

void solve()
{
	int i, j;
	int dist[MAXENGINE], ans;
	i = ans = 0;
	while (i < numOfQuery)
	{
		for (j = 0; j < numOfEngine; j++)
			dist[j] = INT_MAX;
		for (j = i; j < numOfQuery; j++)
			if (j-i < dist[query[j]])
				dist[query[j]] = j - i;
		int max_dist = -1, id = -1;
		for (j = 0; j < numOfEngine; j++)
			if (dist[j] > max_dist){
				max_dist = dist[j];
				id = j;
			}
		if (max_dist == INT_MAX){
			cout << ans << endl;
			return;
		}
		for (j = i; query[j] != id && j < numOfQuery; j++);
		ans++;
		i = j;
	}
	cout << ans << endl;
}

int main()
{
	int numOfCase, kase;
	cin >> numOfCase;
	for (kase = 1; kase <= numOfCase; kase++)
	{
		init();
		input();
		cout << "Case #" << kase << ": ";
		solve();
	}
return 0;
}

