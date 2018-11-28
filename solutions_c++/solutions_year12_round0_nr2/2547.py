#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <ctime>
#include <queue>
#include <cmath>
#include <deque>
#include <list>
#include <sstream>
#include <bitset>
#include <complex>
#pragma comment(linker, "/STACK:16777216")
#pragma warning(default :4)
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define eps 1e-9
#define INF 1000000001
#define oo 1000000001
#define MOD 1000000007
#define cint const int &
#define cll const ll &
#define cull const ull &
#define FOR(i, x) for (int i = 0; i < (int)(x); ++i)
#define CL(x) memset(x, 0, sizeof(x))
#define SVAL(x, y) memset(x, y, sizeof(x))
#define FIN freopen("in.txt", "r", stdin);
#define FOUT freopen("out.txt", "w", stdout);
#define y1 Y1
using namespace std;
typedef vector<int> VINT;
typedef pair<int, int> PII;
typedef complex<double> Cn;
int T, n, s, p, t[1001];
vector<int> nx;
int tr(int t)
{
	if (t<2) return t;
	return 2+(t-2)/3;
}
int hs(int t)
{
	return t/3+((t%3)>0);
}
int main()
{
	FIN;
	FOUT;
	scanf("%d", &T);
	for (int tst=1; tst<=T; tst++)
	{
		scanf("%d %d %d", &n, &s, &p); int r=0;
		for (int i=0; i<n; i++) scanf("%d", &t[i]); nx.clear();
		for (int i=0; i<n; i++)
			if (hs(t[i])>=p) r++; else nx.push_back(t[i]);
		for (int i=0; s && i<nx.size(); i++)
			if (tr(nx[i])>=p) r++, s--;
		printf("Case #%d: %d\n", tst, r);
	}
	return 0;
}
