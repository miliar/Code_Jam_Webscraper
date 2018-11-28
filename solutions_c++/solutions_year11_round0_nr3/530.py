#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
//#include <ext/hash_map>

using namespace std;
//using namespace __gnu_cxx;

#define FOR(i, a, n) for(int i=(a); i<(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define sz(X) int((X).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define all(X) (X).begin(), (X).end()

typedef long long lint;
typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef vector<int> VI;

template<class T> ostream &operator<<(ostream &os, vector<T> vec)
{
	os<<'{';
	REP(i, sz(vec)){
		os<<vec[i];
		if (i+1!=sz(vec)) os<<',';
	}
	os<<'}';
	return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, pair<T1, T2> par)
{
	os<<'('<<par.X<<','<<par.Y<<')';
	return os;
}

void solve(int test){
	int n;
	scanf("%d", &n);
	int sumV = 0;
	int xorV = 0;
	int minV = 1000 * 1000 * 1000;
	REP(i, n){
		int x;
		scanf("%d", &x);
		xorV ^= x;
		sumV += x;
		minV = min(minV, x);
	}
	if(xorV){
		printf("NO\n");
		return;
	}
	int ans = sumV - minV;
	printf("%d\n", ans);
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int n;
	cin>>n;
	for(int test = 1; test <= n; ++test){
		printf("Case #%d: ", test);
		solve(test);
	}
	return 0;
}
