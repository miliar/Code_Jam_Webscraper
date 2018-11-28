#define _HAS_CPP0X 0
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


void Go(){
	int a, b;
	cin >> a >> b;
	LL res = 0;
	LL len = 0;
	LL aa = a;
	LL p10 = 1;
	while (aa){
		len++;
		p10 *= 10;
		aa /= 10;
	}
	LL pairs[16];
	int pairs_sz = 0;
	for (LL m = a; m <= b; m++){
		LL n = m;
		pairs_sz = 0;
		for (int i = 1; i < len; i++){
			bool ok = 1;
			if (n % 10 == 0)
				ok = 0;
			n = n / 10 + p10 / 10 * (n % 10);
			ok = ok && n != m && a <= n && n < m;
			if (ok){
				FOR(j, pairs_sz)
					if (pairs[j] == n){
						ok = 0;
						break;
					}
			}
			if (ok){
				res++;
				pairs[pairs_sz++] = n;
			}
		}
		if (m + 1 == p10){
			p10 *= 10;
			len++;
		}
	}
	cout << res;
}

int main(){
	const string task = "C";
	const string folder = "gcj/2012/qual";
	const int attempt = -1;
	const bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		if (attempt < 0)
			ss << folder << '/' << task << "-large";
		else
			ss << folder << '/' << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		Go();
		cerr << '!';
		printf("\n");
	}
	return 0;
}