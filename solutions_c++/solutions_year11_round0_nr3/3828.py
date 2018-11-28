/*
 * C.CandySplitting.cpp
 *
 *  Created on: May 7, 2011
 *      Author: ahmed
 */
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
#include <cstring>
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

int main()
{
	freopen("a.txt", "wt", stdout);
	int t;scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		int n;scanf("%d", &n);
		vector<int >frq(32, 0);
		ll res = 0;
		int f = oo;
		for (int i = 0; i < n; ++i) {
			int cur;
			scanf("%d", &cur);
			f = min(f, cur);
			res+=cur;
			for (int j = 0; j < 30; ++j)
				if(cur&(1<<j))
					frq[j]++;
		}
		int isodd = 0;
		for (int i = 0; i < (int)frq.size(); ++i) {
			if(frq[i]&1)
				isodd = 1;
		}
		printf("Case #%d: ", ii+1);
		if(isodd)
			printf("NO\n");
		else
			printf("%lld\n", res-f);
	}
	return 0;
}
/*
2
5
1 2 3 4 5
3
3 5 6
 */
