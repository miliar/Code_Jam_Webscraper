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
int h[11], n, nx[11];
bool gr(int p1, int q1, int p2, int q2)
{
	return q2*1LL*p1<=p2*1LL*q1;
}
bool gd()
{
	for (int i=0; i+1<n; i++)
	{
		int a=h[i+1]-h[i], b=1, ps=i+1;
		for (int j=i+2; j<n; j++)
		{
			int p=h[j]-h[i], q=j-i;
			if (gr(a, b, p, q))
			{
				a=p; b=q; ps=j;
			}
		}
		ps++;
		if (ps!=nx[i]) return 0;
	}
	return 1;
}
bool can()
{
	for (int i=0; i+1<n; i++)
		for (int j=i+1; j+1<n; j++)
		{
			if (j<nx[i]-1 && nx[j]>nx[i]) return 0;
		}
	for (int i=1; i<1000000; i++)
	{
		for (int j=0; j<n; j++) h[j]=rand();
		do
		{
			if (gd()) return 1;
		}
		while (next_permutation(h, h+n));
	}
	//h[0]=1;
	//for (int i=1; i<n; i++) h[i]=2*i+h[i-1]; // !
	//do
	//{
	//	if (gd()) return 1;
	//}
	//while (next_permutation(h, h+n));
	return 0;
}
int main()
{
	FIN;
	FOUT;
	//freopen("p5.in", "r", stdin);
	//freopen("p5.out", "w", stdout);
	scanf("%d", &tst);
	FOR(TST, tst)
	{
		cerr << TST << endl;
		scanf("%d", &n);
		FOR(i, n-1) scanf("%d", &nx[i]);
		printf("Case #%d: ", TST+1);
		if (!can()) puts("Impossible");
		else
		{
			for (int i=0; i<n; i++) printf("%d%c", h[i], i==n-1 ? '\n' : ' ');
		}
	}
    return 0;
}
