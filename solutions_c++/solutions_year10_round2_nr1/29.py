#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

const int N = 128;

set<string> g[N];

int add(string dir)
{
	for(int i = 0; i < (int)dir.size(); i++) if(dir[i] == '/') dir[i] = ' ';
	stringstream ss(dir);
	string folder, path = "";
	int res = 0;
	for(int i = 0; ss >> folder; i++) {
		path += "/"+folder;
		if(g[i].count(path)) continue;
		g[i].insert(path);
		// cout << i << " " << folder << endl;
		res++;
	}
	return res;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < N; i++) g[i].clear();
		for(int i = 0; i < n; i++) {
			string tmp;
			cin >> tmp;
			add(tmp);
		}
		int res = 0;
		for(int i = 0; i < m; i++) {
			string tmp;
			cin >> tmp;
			res += add(tmp);
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	
	return 0;
}

