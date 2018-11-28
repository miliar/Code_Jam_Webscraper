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

int nn[220 * 2];
int x[220 * 2];

void solve(int test){
	int n;
	double d;
	scanf("%d%lf", &n, &d);
	int m = 0;
	REP(i, n){
		int nn1, x1;
		scanf("%d%d", &x1, &nn1);
		nn[m] = 1;
		x[m] = x1;
		++m;
		if(nn1 > 1){
			nn[m] = nn1 - 1;
			x[m] = x1;
			++m;
		}
	}
	double t = -1e7, h = 0;

	REP(i, m){
		if(x[i] + h < t){
			h = (h + t - x[i]) / 2;
			t = x[i] + h;
		}else if(h + t < x[i]){
			t = x[i] - h;
		}
		if(i != m - 1){
			t += d * nn[i + 1];
		}
	}
	printf("%.7lf\n", h);
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int n;
	cin>>n;
	for(int test = 1; test <= n; ++test){
//		printf("Case #%d:\n", test);
		printf("Case #%d: ", test);
		solve(test);
	}
	return 0;
}
