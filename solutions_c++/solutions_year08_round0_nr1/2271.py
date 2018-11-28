#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <iostream>

using namespace std;

#define SZ(x) ((int)(x).size())
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FOREACH(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

typedef vector<string> vs;
vs engine, list;
const int INF = 1010;

char temp[200];
int s, q;

int Search(string s, int from)
{
	FOR(i, from, q)
		if (list[i] == s)
			return i;
	return INF;
}

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int testCase;
	string st;
	cin >> testCase;
	cin.get();
	FOR(cas, 1, testCase + 1)
	{
		cin >> s;
		cin.get();
		engine.clear();
		FOR(i, 0, s) { cin.getline(temp, 200); st = temp; engine.PB(st); }
		
		cin >> q;
		cin.get();
		list.clear();
		FOR(i, 0, q) { cin.getline(temp, 200); st = temp; list.PB(st); }
		int ans = -1;
		int furthest = 0, cur = 0;
		while (cur < q)
		{
			FOR(i, 0, s)
			{
				int tmp = Search(engine[i], cur);
				if (tmp > furthest) furthest = tmp;
			}
			ans++;
			cur = furthest;
		}
		if (ans < 0) ans = 0;
		cout << "Case #" << cas << ": " << ans << endl;
		
	}
	return 0;
}


