#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int a[128];
int best[128][256];
int D, I, M, N;

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		//if (M == 0)	cout << nc << endl;
		cin >> D >> I >> M >> N;
		FOR (i, 1, N+1)	{
			cin >> a[i];
		}
		
		FOR (last, 0, 256)	{
			best[0][last] = 0;
		}
		
		FOR (i, 1, N+1)	{
			FOR (last, 0, 256)	{
				best[i][last] = 1000000;
			}
		}
		
		FOR (i, 1, N+1)	{
			FOR (last, 0, 256)	{
				
				if (M > 0)	{
					FOR (now, 0, 256)	{//a[i] changes to now and stuff gets inserted if necessary
						int cost = best[i-1][last] + abs(now - a[i]);
						int inc = (abs(now - last) + M - 1) / M;
						if (inc >= 1)	cost += I * (inc - 1);
						best[i][now] = min(best[i][now], cost);
					}
				}
				
				FOR (now, max(0, last - M), min(255, last + M) + 1)	{	//a[i] changes to now
					best[i][now] = min(best[i][now], best[i-1][last] + abs(now - a[i]));
				}
				
				//a[i] gets erased
				best[i][last] = min(best[i][last], best[i-1][last] + D);
		
				//a[i] stays as is if distance is at most M
				if (abs(a[i] - last) <= M)	{
					best[i][a[i]] = min(best[i][a[i]], best[i-1][last]);
				}

				//stuff gets inserted from last to a[i], increments of M
				if (M > 0)	{
					int inc = (abs(a[i] - last) + M - 1) / M;
					//assert(inc >= 1);
					if (inc >= 1)	{
						best[i][a[i]] = min(best[i][a[i]], best[i-1][last] + I * (inc - 1));
					}
				}
			}
		}
		
		int ret = 1000000;
		FOR (last, 0, 256)	{
			ret = min(ret, best[N][last]);
		}
		cout << "Case #" << nc << ": " << ret << endl;
	}
	
	
}
