#include <vector>
#include <list>
#include <map>
#include <set>
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
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const int MAX = 105;

int n;
double X[MAX], Y[MAX], R[MAX];
double ans;

double distance(double x1, double y1, double x2, double y2)
{
	return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) );
}

void process()
{
	if (n == 1)
	{
		ans = R[0];
		return;
	}

	if (n == 2)
	{
		ans = max(R[0], R[1]);
		return;
	}
	double res;
	ans = 1e30;

	res = (distance(X[0], Y[0], X[1], Y[1]) + R[0] + R[1]) * 0.5;
	res = max(res, R[2]);
	ans = min(ans, res);

	res = (distance(X[1], Y[1], X[2], Y[2]) + R[1] + R[2]) * 0.5;
	res = max(res, R[0]);
	ans = min(ans, res);

	res = (distance(X[2], Y[2], X[0], Y[0]) + R[2] + R[0]) * 0.5;
	res = max(res, R[1]);
	ans = min(ans, res);
}

int main()
{
	//freopen("sample.in", "r", stdin); //freopen("sample.out", "w", stdout);
	freopen("D-small-attempt3.in", "r", stdin); freopen("D-small-attempt3.out", "w", stdout);
	//freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

	int tc, testcase, i, j;
	cin >> tc;

	RP(testcase, tc)
	{
		cin >> n;
		RP(i, n)
		{
			cin >> X[i] >> Y[i] >> R[i];
		}
		process();
		printf("Case #%d: %.6lf\n", (testcase+1), ans);
	}

	return 0;
}
