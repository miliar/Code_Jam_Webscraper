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
char m[]="yhesocvxduiglbkrztnwjpfmaq";
char s[1001], r[1001];
int n;
int main()
{
	FIN;
	FOUT;
	scanf("%d\n", &n);
	for (int i=0; i<n; i++)
	{
		gets(s);
		CL(r);
		for (int j=0; s[j]; j++) r[j]=s[j]==' ' ? ' ' : m[s[j]-'a'];
		printf("Case #%d: %s\n", i+1, r);
	}
	return 0;
}
