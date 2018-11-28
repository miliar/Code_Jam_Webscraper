#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

#define forn(i, n) for (int i = 0; i < n; i ++)
#define ford(i, n) for (int i = n - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

queue < pair<int, int> > q[2];
int maxint = 1000000000; 

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(i, t){
		int n;
		scanf("%d ", &n);
		forn(j, n){
			char c;
			int t1;
			scanf("%c %d ", &c, &t1);
			if (c == 'O') q[0].push(mp(j, t1));
			else q[1].push(mp(j, t1));
		}
		int st1 = 1, st2 = 1, ans = 0;
		while (!q[0].empty() || !q[1].empty()){
			pair<int, int> k1 = ((q[0].empty())?(mp(maxint, maxint)):(q[0].front())), k2 = ((q[1].empty())?(mp(maxint, maxint)):(q[1].front()));
			if (k1.second != st1){
				if (k1.second > st1) st1 ++;
				else st1 --;
			} else {
				if (k1.first < k2.first)
					q[0].pop();
			}
			if (k2.second != st2){
				if (k2.second > st2) st2 ++;
				else st2 --;
			} else {
				if (k1.first > k2.first)
					q[1].pop();
			}
			ans ++;
		}
		//cout << ans << endl;
		printf ("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}