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

double dist(double x1, double y1, double x2, double y2)	{
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

double x[10], y[10], r[10];
int N;

int main(void)	{
	int C;
	cin >> C;
	
	FOR (nc, 1, C+1)	{
		cin >> N;
		FOR (i, 0, N)	cin >> x[i] >> y[i] >> r[i];
	
		double ans = 10e9;
		if (N == 1)	{
			ans = r[0];
		}
		else if (N == 2)	{
			ans = max(r[0], r[1]);
		}
		else if (N == 3)	{
			ans = min(ans, max((dist(x[0], y[0], x[1], y[1]) + r[0] + r[1]) / 2.0, r[2]));
			ans = min(ans, max((dist(x[0], y[0], x[2], y[2]) + r[0] + r[2]) / 2.0, r[1]));
			ans = min(ans, max((dist(x[1], y[1], x[2], y[2]) + r[1] + r[2]) / 2.0, r[0]));
		}
		cout << "Case #" << nc << ": ";
		printf("%0.7lf\n", ans);
	}
	
	
}
