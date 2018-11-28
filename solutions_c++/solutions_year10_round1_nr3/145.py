#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <ctime>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;

#define Filename "c"
#define sqr(a) (a)*(a)
#define abs(a) ((a) < 0 ? -(a) : (a))
#define nextline for (int CcC = getchar();CcC != '\n' && CcC != EOF;CcC = getchar());

typedef long long lng;
typedef long double ldb;

const int INF = (1 << 30)-1;
const double EPS = 1e-9;

int A1, A2, B1, B2;

void Load()
{
	cin >> A1 >> A2 >> B1 >> B2;
}

int win (int a, int b, int wh)
{
	if (a == 0 || b == 0) return wh;
	if (a == 1 && b > 1) return wh;
	if (b == 1 && a > 1) return wh;
	int pr = a / b;
	for (int i = pr;i >= 1;i--)
		if (win (a - i * b, b, !wh) == wh) return wh;
	pr = b / a;
	for (int i = pr;i >= 1;i--)
		if (win (a, b - i * a, !wh) == wh) return wh;
	return 1 - wh;
}

int main()
{
	freopen(Filename".in", "r", stdin);
	freopen(Filename".out", "w", stdout);
	int T;
	cin >> T;
	for (int step = 1;step <= T;step++)
	{
		Load();
		int ans = 0;
		printf("Case #%d: ", step);
		for (int A = A1;A <= A2;A++)
			for (int B = B1;B <= B2;B++)
			{
				//cerr << A << " " << B << endl;
				if (win (A, B, 0) == 0) ans++;
			}
		printf("%d\n", ans);
	}
	return 0;
}
