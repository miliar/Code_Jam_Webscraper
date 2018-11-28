#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define FORD(i,a,b) for (int i = (int)(a)-1; i >= (int)(b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,a) FORD(i,a,0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-12;
const int INF = 1000000000;

int tc, n;
string s[100];

double wp (int v, int p){
	int win = 0;
	int tot = 0;
	REP(i,n) if (s[v][i]!='.' && i!=p){
		++tot;
		if (s[v][i]=='1') ++win;
	};
	return (double)win/(double)tot;
};

double owp (int v){
	int q = 0;
	double sm = 0;
	REP(i,n) if (s[v][i]!='.'){
		++q;
		sm += wp (i, v);
	};
	return sm/q;
};

double rpi(int v){
	double res = 0.25*wp(v, -1);
	int q = 0;
	double sm = 0;
	int w = 0;
	double sm2 = 0;
	REP(i,n) if (s[v][i]!='.'){
		++q;
		sm += wp (i, v);
		++w;
		sm2 += owp (i);
	};
	res += 0.5*sm/q + 0.25*sm2/w;
	return res;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n;
		REP(i,n) cin >> s[i];
		printf ("Case #%d:\n", ic+1);
		REP(i,n) printf ("%.10lf\n", rpi(i));
	};
	return 0;
};