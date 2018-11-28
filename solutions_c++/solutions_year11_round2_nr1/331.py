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

char a[110][110];
double f[3][110];
double nn[110];
double g[110];

void solve(int test){
	int n;
	scanf("%d", &n);
	REP(i, n){
		scanf("%s", a[i]);
	}
	double coef[] = {0.25, 0.5, 0.25};
	REP(i, n){
		f[0][i] = 0.0;
		nn[i] = 0;
		REP(j, n){
			nn[i] += a[i][j] != '.';
			f[0][i] += a[i][j] == '1';
		}
		g[i] = (f[0][i] / nn[i]) * coef[0];
	}

	REP(i, n){
		f[1][i] = 0.0;
		REP(j, n){
			if(a[i][j] == '1'){
				f[1][i] += f[0][j] / (nn[j] - 1);
			}
			if(a[i][j] == '0'){
				f[1][i] += (f[0][j] - 1) / (nn[j] - 1);
			}
		}
		f[1][i] /= nn[i];
		g[i] += f[1][i] * coef[1];
	}

	REP(i, n){
		f[2][i] = 0.0;
		REP(j, n){
			if(a[i][j] != '.'){
				f[2][i] += f[1][j];
			}
		}
		f[2][i] /= nn[i];
		g[i] += f[2][i] * coef[2];
	}

	REP(i, n){
		printf("%.7lf\n", g[i]);
	}
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int n;
	cin>>n;
	for(int test = 1; test <= n; ++test){
		printf("Case #%d:\n", test);
//		printf("Case #%d: ", test);
		solve(test);
	}
	return 0;
}
