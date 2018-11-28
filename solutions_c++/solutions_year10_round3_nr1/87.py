#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openfiles()
{
#ifndef ONLINE_JUDGE
	string file = "A-large";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}


#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	int n; scanf("%d ",&n);
	vector<pair<int,int> > v;
	for (int i = 0; i < n; i++) {
		pair<int, int> p;
		scanf("%d %d ",&p.first,&p.second);
		v.push_back(p);
	}
	int sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (v[i].first > v[j].first && v[i].second < v[j].second) {
				sum++;
			}
			else if (v[i].second > v[j].second && v[i].first < v[j].first) {
				sum++;
			}
		}
	}
	printf("Case #%d: %d\n", test + 1, sum);
}
#endif

int main()
{
	openfiles();
	#ifdef SOLVE_BOOL
		while(solve());
	#endif
	#ifdef SOLVE_VOID
		int n; scanf("%d ",&n); REP(i,n) solve(i);
	#endif
	
	return 0;
}