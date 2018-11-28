/*
 * A.BotTrust.cpp
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
		int res = 0;
		int b, k, lb = 1, lo = 1, mb = 0, mo = 0, f = -1;
		scanf("%d ", &b);
		char c;
		for (int i = 0; i < b; ++i) {
			cin>>c;
			scanf("%d", &k);
			/*if(c == 'O')
				mo+=fabs(k-lo)+1, res+=max(0, (int)(fabs(k-lo))+1-mb), mb = 0, lo = k;
			else
				mb+=fabs(k-lb)+1, res+=max(0, (int)(fabs(k-lb))+1-mo), mo = 0, lb = k;*/
			if(c =='O') {
				if(f == 0 || f == -1) {
					res+=(fabs(k-lo))+1;
					mo+=abs(k-lo)+1;
				}
				else if(f == 1) {
					res+=max(0, (abs(k-lo)) - mb) + 1;
					mo = max(0, abs(k-lo) - mb) + 1;

				}
				lo = k;
				mb = 0;
				f = 0;
			}
			else {
				if(f == 1 || f == -1) {
					res+=abs(k-lb) + 1;
					mb+=abs(k-lb)+1;
					lb = k;
				}
				else if(f == 0) {
					res+=max(0, abs(k-lb) - mo) + 1;
					mb = max(0, abs(k-lb) - mo) + 1;
				}
				lb = k;
				mo = 0;
				f = 1;
			}
		}
		printf("Case #%d: %d\n", ii+1, res);
	}
	return 0;
}

