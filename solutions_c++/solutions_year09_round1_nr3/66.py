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
const int MAX = 55;

LL CB[MAX][MAX];
bool seen[MAX];
double cache[MAX];
LL total;
int N, C;

double calc(int v)
{
	double &res = cache[v];
	if (seen[v]) return res;
	seen[v] = true;
	if (v == C) return res = 0.0;

	res = 1.0;
	int left, right;
	double per;
	double hs = 0.0;
	FR(left, 0, min(N, v))
	{
		right = N - left;
		if (right > C-v) continue;

		per = (double)CB[v][left] / (double)total * (double)CB[C-v][right];
		if (right == 0) hs += per; else res += per * calc(v+right);
	}

	res /= (1.0 - hs);

	return res;
}

int main()
{
	//freopen("sample.in", "r", stdin); //freopen("sample.out", "w", stdout);
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

	int tc, testcase, i, j;
	string str;
	char cc[1000];
	
	memset(CB, 0, sizeof(CB));
	CB[0][0] = 1;
	FR(i, 1, MAX-1)
	{
		CB[i][0] = 1;
		FR(j, 1, MAX-1) CB[i][j] = CB[i-1][j-1] + CB[i-1][j];
	}

	cin >> tc;

	RP(testcase, tc)
	{
		cin >> C >> N;
		total = CB[C][N];
		memset(seen, false, sizeof(seen));
		double ans = calc(0);
		printf("Case #%d: %.7lf\n", (testcase+1), ans);
	}

	return 0;
}
