// problem1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024*1024];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	gets(buf);
	long double ld = 3 + 2.23606797749978969;
	string aaa[30] = {

	"005",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"335",
"047",

"943",
"471",
"055",
"447",
"463",
"991",
"095",
"607",
"263",
"151",

"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"
	};

	For(test, 1, atoi(buf)) {
		
		long double s = 1;

		int n = 0;
		scanf("%d",&n);

		


		long double d;
		printf("Case #%d: %s\n", test, aaa[n-1].c_str());
	}

	exit(0);
}
