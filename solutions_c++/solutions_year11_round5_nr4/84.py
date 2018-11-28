#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

char buff[1234];

bool isok(long long num)
{
	long long a = sqrt(double(num));
	return a * a == num || (a - 1) * (a - 1) == num || (a + 1) * (a + 1) == num;
}

char* run()
{
	scanf("%s", buff);
	int len = strlen(buff);
	vector<int> v;
	long long val = 0;
	for (int i = 0; buff[i]; ++i) {
		if (buff[i] == '?') {
			v.push_back(i);
		}
		val <<= 1;
		if (buff[i] == '1') ++val;
	}
	int nn = sz(v);
	for (int i = 0; i < (1 << nn); ++i) {
		long long vv = val;
		for (int j = 0; j < nn; ++j) {
			if (i & (1LL << j)) {
				buff[v[j]] = '1';
				vv += (1LL << (len - 1 - v[j]));
			}
			else {
				buff[v[j]] = '0';
			}
		}
		if (isok(vv)) {
			return buff; 
		}
	}
	return buff;
}

int main()
{
	freopen("D0.in", "r", stdin);
	freopen("D0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %s\n", i, run());
	}
	return 0;
}