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

int g[26][26];
int o[26][26];
char buf[110];

void solve(int test){
	memset(g, -1, sizeof g);
	memset(o, 0, sizeof o);
	int n;
	scanf("%d", &n);
	REP(i, n){
		scanf("%s", buf);
		g[buf[0] - 'A'][buf[1] - 'A'] = buf[2] - 'A';
		g[buf[1] - 'A'][buf[0] - 'A'] = buf[2] - 'A';
	}
	scanf("%d", &n);
	REP(i, n){
		scanf("%s", buf);
		o[buf[0] - 'A'][buf[1] - 'A'] = 1;
		o[buf[1] - 'A'][buf[0] - 'A'] = 1;
	}
	scanf("%d", &n);
	scanf("%s", buf);
	int len = 0;
	REP(i, n){
		buf[i] -= 'A';
		int c;
		while(len && (c = g[buf[i]][buf[i-1]]) >= 0){
			--len;
			buf[i] = c;
		}
		bool clear = false;
		REP(j, len) if(o[buf[j]][buf[i]]) clear = true;
		if(clear){
			len = 0;
		}else{
			buf[len++] = buf[i];
		}
	}
	printf("[");
	REP(i, len){
		printf(", %c" + !i * 2, buf[i] + 'A');
	}
	printf("]\n");
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
