/* @JUDGE_ID: tinysun  10252  C++  "Common Permutation"  */

#define _CRT_SECURE_NO_WARNINGS

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

//typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

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

char buf[1024];

int main() {

#ifndef  ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	gets(buf);
	int ncase = atoi(buf);
	For(nc,1,ncase) {
		int  P, K, L;
		scanf("%d%d%d", &P, &K, &L);
		gets(buf);
		int  alpha[1001];
		Rep(i,L) {
			scanf("%d",&alpha[i]);
		}
		gets(buf);
		sort(alpha, alpha+L, greater<int>());
		int sum = 0;
		Rep(i,L)
			sum += (i/K+1)*alpha[i];
		printf("Case #%d: %d\n", nc, sum);
	}
}
