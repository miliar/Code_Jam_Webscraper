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

double Q[2];
double P[10][2];

double dot(double x1, double y1, double x2, double y2)	{
	return (x1 * x2 + y1 * y2);
}

double norm(double x, double y)	{
	return sqrt(x*x + y*y);
}

int N, M;

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> N >> M;
		FOR (i, 0, N)	{
			cin >> P[i][0] >> P[i][1];
		}
		cout << "Case #" << nc << ":";
		FOR (i, 0, M)	{
			cin >> Q[0] >> Q[1];
			double d = norm(P[1][0] - P[0][0], P[1][1] - P[0][1]);
			double dt0 = dot(Q[0] - P[0][0], Q[1] - P[0][1], (P[1][0] - P[0][0]) / d, (P[1][1] - P[0][1]) / d);
			double r0 = norm(P[0][0] - Q[0], P[0][1] - Q[1]);
			double r1 = norm(P[1][0] - Q[0], P[1][1] - Q[1]);
			//double h = sqrt(r0*r0 - dt0*dt0);
			
			double ang1 = acos(dt0 / r0);
			double ans = ang1 * r0 * r0 - 0.5 * r0 * r0 * sin(2. * ang1);

			double dt1 = dot(Q[0] - P[1][0], Q[1] - P[1][1], (P[0][0] - P[1][0]) / d, (P[0][1] - P[1][1]) / d);
			double ang2 = acos(dt1 / r1);
			ans += ang2 * r1 * r1 - 0.5 * r1 * r1 * sin(2. * ang2);
			
			printf(" %0.7lf", ans);
		}
		cout << endl;
	}
	
	
}
