#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for(int i=(a), _b=(b); i<_b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for(int i=(a), _b=(b); i>=_b; --i)
#define CL(a, v) memset(a, v, sizeof a)
#define INF 1000000000
#define INF_LL 1000000000000000000LL
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int h = 1111;
int n, c[h];

int main()
{
	freopen("c-large.in", "r", stdin); //-small-attempt
	freopen("c-large.out", "w", stdout); //-large
	int T, it=1;
for(scanf("%d", &T); it<=T; ++it)
{
	scanf("%d", &n);
	REP(i, n) scanf("%d", c+i);
	sort(c, c+n);
	int s = 0;
	REP(i, n) s ^= c[i];
	printf("Case #%d: ", it);
	if(s!=0) printf("NO\n");
	else
	{
		FOR(i, 1, n) s += c[i];
		printf("%d\n", s);
	}
}
	return 0;
}
