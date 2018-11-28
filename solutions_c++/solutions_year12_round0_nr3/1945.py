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
	int A, B;
	
	int Solve()
	{
		scanf("%d%d", &A, &B);
		int res = 0;
		for (int i = A; i <= B; ++ i)
		{
			int dgt = 1;
			for (; dgt <= i; dgt *= 10);
			vector <int> List;
			for (int base = 10; base <= i; base *= 10)
			{
				int a = i % base, b = i / base;
				int x = a * (dgt / base) + b;
				if (i < x && x <= B)
					List.pb(x);
			}
			sort(List.begin(), List.end());
			res += unique(List.begin(), List.end()) - List.begin();
		}
		return res;
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
