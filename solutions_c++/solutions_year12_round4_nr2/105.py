#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 1000;
int N, X, Y, x[MAX], y[MAX], r[MAX], order[MAX];

bool comp(int i, int j) { return r[i] > r[j]; }

inline bool isok(int i, int j)
{
	return x[i]+r[i] <= x[j]-r[j] || x[i]-r[i] >= x[j]+r[j] ||
		y[i]+r[i] <= y[j]-r[j] || y[i]-r[i] >= y[j]+r[j];
}

bool go()
{
	vector<pair<int, int> > points;
	points.push_back(make_pair(-r[order[0]], -r[order[0]]));
	REP(i, N)
	{
		int index = order[i];
		bool found = false;
		REP(j, points.size())
		{
			x[index] = max(0, points[j].first + r[index]);
			y[index] = max(0, points[j].second + r[index]);
			if (x[index] > X || y[index] > Y) continue;

			bool ok = true;
			REP(k, i)
				if (!isok(index, order[k]))
				{
					ok = false;
					break;
				}
			if (ok)
			{
				found = true;
				if (x[index]+r[index] <= X) points.push_back(make_pair(x[index]+r[index], y[index]-r[index]));
				if (y[index]+r[index] <= Y) points.push_back(make_pair(x[index]-r[index], y[index]+r[index]));
				if (x[index]+r[index] <= X && y[index]+r[index] <= Y)
					points.push_back(make_pair(x[index]+r[index], y[index]+r[index]));
				swap(points[j], points.back());
				points.pop_back();
				break;
			}
		}
		if (!found) return false;
	}
	return true;
}

void Solve(int tc)
{
	scanf("%d%d%d", &N, &X, &Y);
	REP(i, N) scanf("%d", &r[i]);
	REP(i, N) order[i] = i;
	sort(order, order+N, comp);
	while (!go()) random_shuffle(order, order+N);
	printf("Case #%d: ", tc);
	REP(i, N) printf("%d %d ", x[i], y[i]);
	printf("\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}