#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>

using namespace std;

const int INF = 1000000000;

typedef long long int64; 
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }



int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests_count;
	cin >> tests_count;

for (int test = 1; test <= tests_count; ++test) 
{
	fprintf(stderr, "Test: #%d\n", test);
	printf("Case #%d: ", test);


	int n, K, B, T_end;
	cin >> n >>  K >>  B >>  T_end;
	vector<int> x, v;
	x.resize(n);
	v.resize(n);
	for (int i = 0; i < n ; i++)
	{
		cin >> x[i];
	}
	for (int i = 0; i < n ; i++)
	{
		cin >> v[i];;
	}

	int res = 0, goods = 0;

	vector<bool> bad_duck (n);
	for (int i = n - 1; i >= 0 ; i--)
	{
		bad_duck[i] = x[i] + v[i] * T_end < B;
	}

	for (int i = n - 1; i >= 0 && goods < K ; i--)
	{
		if (!bad_duck[i]) {
			goods++;
			for (int j = i + 1; j < n ; j++)
			{
				if (bad_duck[j]) {
					res++;
				}
			}
		}
	}

	if (goods < K)
		printf("IMPOSSIBLE\n");
	else
	printf("%d\n", res);
}

}