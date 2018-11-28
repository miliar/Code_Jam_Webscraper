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
	For(test, 1, atoi(buf)) {
		
		long long s = 0;
		vector<long long > v1;
		vector<long long > v2;
		int n1 = 0;
		scanf("%d",&n1);
		for(int k1 = 0;k1<n1;k1++)
		{
			long long  m;
			scanf("%lld",&m);
			v1.push_back(m);
		}
		for(int k2 = 0;k2<n1;k2++)
		{
			long long  m;
			scanf("%lld",&m);
			v2.push_back(m);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		reverse(v2.begin(),v2.end());

		for(int i = 0;i<n1;i++)
		{
			s += v1[i] * v2[i];
		}
		printf("Case #%d: %lld\n", test, s);
	}

	exit(0);
}
