/*
 * 2012-04-14  Martin  <Martin@Martin-desktop>

 * 
 */
#include <climits>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <exception>
#include <stdexcept>
#include <memory>
#include <locale>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include <string>
#include <complex>
#include <valarray>

using namespace std;

template <class T> inline T checkmin(T &a, T b)
{
	return (a < b) ? a : a = b;
}

template <class T> inline T checkmax(T &a, T b)
{
	return (a > b) ? a : a = b;
}

template <class T> T GCD(T a, T b)
{
	if (a < 0)
		return GCD(- a, b);
	if (b < 0)
		return GCD(a, - b);
	return (a == 0) ? b : GCD(b % a, a);
}

template <class T> T LCM(T a, T b)
{
	if (a < 0)
		return LCM(- a, b);
	if (b < 0)
		return LCM(a, - b);
	return (a == 0 || b == 0) ? 0 : a / GCD(a, b) * b;
}

template <class T> T ExtGCD(T a, T b, T &x, T &y)
{
	if (a < 0)
	{
		T c = ExtGCD(- a, b, x, y);
		x = - x;
		return c;
	}
	if (b < 0)
	{
		T c = ExtGCD(a, - b, x, y);
		y = - y;
		return c;
	}
	if (a == 0)
	{
		x = 0, y = 1;
		return b;
	}
	else
	{
		T c = ExtGCD(b % a, a, y, x);
		x -= b / a * y;
		return c;
	}
}

template <class T> inline T sqr(T X)
{
	return X * X;
}

#define tr(i, x) for (typeof(x.begin()) i = x.begin(); i != x.end(); ++ i)
#define rep(i, n) for (int i = 0; i < n; ++ i)
#define pii pair <int, int>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define ll long long

namespace Poor
{
	const int MaxiN = 105;
	
	int N, S, P;
	int T[MaxiN];
	int Opt[MaxiN][MaxiN];
	
	int Solve()
	{
		scanf("%d%d%d", &N, &S, &P);
		for (int i = 1; i <= N; ++ i)
			scanf("%d", T + i);
		memset(Opt, 0, sizeof(Opt));
		for (int i = 1; i <= N; ++ i)
			for (int j = 0; j <= S; ++ j)
			{
				int h = T[i] / 3 + (T[i] % 3 > 0);
				Opt[i][j] = Opt[i - 1][j] + (h >= P);
				if (j > 0 && T[i] > 1)
					checkmax(Opt[i][j], Opt[i - 1][j - 1] + (h + (T[i] % 3 != 1) >= P));
			}
		return Opt[N][S];
	}
	
	void Run()
	{
		int TestCase;
		scanf("%d", &TestCase);
		for (int i = 1; i <= TestCase; ++ i)
			printf("Case #%d: %d\n", i, Solve());
	}
}

int main()
{
	Poor::Run();
	return 0;
}
