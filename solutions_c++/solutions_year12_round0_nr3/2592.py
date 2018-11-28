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
int n, a, b, t, r, ln;
inline void add(const int &m)
{
	int t=ln*(m%10)+m/10;
	while (t!=m)
	{
		if (t>=a && t<=b && m<t) r++;
		t=ln*(t%10)+t/10;
	}
}
int main()
{
	FIN;
	FOUT;
	scanf("%d", &t);
	for (int tst=1; tst<=t; tst++)
	{
		scanf("%d %d", &a, &b);
		r=0; ln=1; while (10*ln<=b) ln*=10;
		for (int i=a; i<=b; i++) add(i);
		printf("Case #%d: %d\n", tst, r);
	}
	return 0;
}
