#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
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

#define pb push_back
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) FOR(i,0,n)
#define DBGV(_v) { REP(_i, n) { cout << _v[_i] << "\t";} cout << endl;}
#define GI ({int _t; scanf("%d", &_t); _t;})
#define sz size()
#define DBG(x) cout << #x << ":" << x << endl;

using namespace std;

int main()
{
	int kases = GI;	
	FOR(kase, 1, kases+1) {
		int r = GI, k = GI, n = GI;
		int g[1001];
		long long score_memoize[1001], jump_memoize[1001];
		int start = 0, cur = 0;
		long long res = 0, rides = 0;
		REP(i, n) { scanf("%d", &g[i]); score_memoize[i] = -1; }
		while (rides < r) {
			int sum = 0;
			bool first = true;
			if (score_memoize[cur] != -1) {
				res += score_memoize[cur];
				cur = jump_memoize[cur];
				rides++;
				continue;
			}
			while (1) {
				if ( (sum+g[cur]) <= k && (cur != start || first == true)) {
					sum += g[cur];
					cur = (cur+1)%n;
				}
				else {
					//DBG(sum);
					score_memoize[start] = sum;
					jump_memoize[start] = cur;
					
					res += sum;
					rides++;
					start = cur;
					break;
				}
				first = false;
			}
		}
		//DBGV(score_memoize);
		//DBGV(jump_memoize);
		printf("Case #%d: %lld\n", kase, res);
	}	
}
