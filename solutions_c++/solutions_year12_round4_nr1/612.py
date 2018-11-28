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
#define pb push_back
using namespace std;
typedef vector<int> VINT;
typedef pair<int, int> PII;
typedef complex<double> Cn;
int tst;
int D, d[10010], l[10010], b[10010], n, rd;
bool can()
{
	CL(b); rd=0;
	b[0]=d[0];
	for (int i=0; i<n; i++)
	{
		int &r=b[i];
		if (!b[i]) continue;
		if (d[i]+b[i]>=D) return 1;
		for (int j=i+1; j<n && d[j]<=d[i]+r; j++)
		{
			//if ((d[j]-d[i])*1LL*(d[j]-d[i])+l[j]*1LL*l[j]<r*1LL*r) continue;
			b[j]=max(b[j], min(l[j], d[j]-d[i]));
		}
	}
	return 0;
}
int main()
{
	FIN;
	FOUT;
	//FOUT;
	//freopen("p5.in", "r", stdin);
	//freopen("p5.out", "w", stdout);
	scanf("%d", &tst);
	FOR(TST, tst)
	{
		scanf("%d", &n);
		FOR(i, n) scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &D);
		printf("Case #%d: ", TST+1);
		printf("%s\n", can() ? "YES" : "NO");
	}
    return 0;
}
