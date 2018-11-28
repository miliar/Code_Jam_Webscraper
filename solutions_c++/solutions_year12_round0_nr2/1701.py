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
	int n, s, p;
	cin >> n >> s >> p;
	int res = 0;
	FOR(i, n){
		int b;
		cin >> b;
		int a = (b + 2) / 3;
		int a1 = (b + 4) / 3;
		if (a >= p)
			res++;
		else if (s > 0 && a1 >= p && a1 - 2 >= 0){
			res++;
			s--;
		}
	}
	cout << res;
}

int main(){
	const string task = "B";
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
		printf("\n");
	}
	return 0;
}