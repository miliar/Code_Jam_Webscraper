#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <map>
#include <queue>
using namespace std;

#define REP(i,n) for(int i=0; i < (n); i++)
#define REP2(i,s,n) for(int i=(s); i < (n); i++)

struct NODE { int n; int pos; int reach; };
bool operator < (const NODE &a, const NODE &b) { 
	return a.pos + a.reach < b.pos + b.reach;
}
bool flag[100000000] = { };

int main()
{
	int TESTCASES; cin >> TESTCASES;
	for (int CASE = 1; CASE <= TESTCASES; CASE++)
	{
		int N; cin >> N;
		vector< pair<int, int> > vines;
		REP(i, N) { int d, l; cin >> d >> l; vines.push_back(make_pair(d, l)); }
		int D; cin >> D;
		sort(vines.begin(), vines.end());
		
		int flag[10010] = { };

		priority_queue<NODE> q;
		bool OK = false;
		NODE n = { 0, vines[0].first, vines[0].first };
		q.push( n );
		while(!q.empty())
		{
			NODE c = q.top(); q.pop();
			//cerr << " > "  <<  c.n << " > "<< c.pos << " > "<< c.reach << endl;
			if (flag[c.n] >= c.reach) continue;
			flag[c.n] = c.reach;

			if (c.pos + c.reach >= D) { OK = true; break; }
			for (int i = c.n + 1; i < N; i++)
			{
				if (vines[i].first <= c.pos + c.reach)
				{
					if (flag[i] >= min(vines[i].first - c.pos, vines[i].second)) continue;
					NODE n = { i, vines[i].first, min(vines[i].first - c.pos, vines[i].second) };
					q.push(n);
				}
				else 
					break;
			}
		}

		if (OK)
			cout << "Case #" << CASE << ": YES"  << endl;
		else
			cout << "Case #" << CASE << ": NO"  << endl;

	}

	return 0;
}