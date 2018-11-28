#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define all(x) x.begin(), x.end()
#define sz(v) int(v.size())
#define fori(i,b,n) for (int i = b; i < n; i++)
#define forn(i,n) fori(i,0,n)
#define forall(i,v) forn(i,sz(v))
#define var(x,y) typeof(y) x = y
#define foreach(it,v) for (var(it,v.begin()); it != v.end(); it++)
#define forreach(it,v) for (var(it,v.rbegin()); it != v.rend(); it++)
#define pb(x) push_back(x)

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef set<int> iset;
typedef set<string> sset;

typedef map<int,int> iimap;

typedef vector<int> ivec;
typedef vector<vector<int> > iivec;

int main() {
	int T, C, D, N;
	string str;
	char a, b, c;
	cin >> T;
	forn(CASE,T) {
		vector <char> res;
		char map[256][256] = {0};
		char op[256] = {0};
		cin >> C;
		while (C--) {
			cin >> a >> b >> c;
			map[a][b] = c;
			map[b][a] = c;
		}
		cin >> D;
		while (D--) {
			cin >> a >> b;
			op[a] = b;
			op[b] = a;
		}
		cin >> N >> str;
		forall(i,str) {
			if (!res.empty() && map[str[i]][res.back()]) {
				res.pop_back();
				res.push_back(map[str[i]][str[i-1]]);
			} else if (find(all(res), op[str[i]]) != res.end())
				res.clear();
			else
				res.push_back(str[i]);
		}
		printf("Case #%d: [", CASE+1);
		foreach(it,res) {
			if (it != res.begin()) cout << ", ";
			cout << *it;
		}
		printf("]\n");
	}
	return 0;
}
