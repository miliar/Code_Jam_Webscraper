//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<complex>
#include<set>
#include<algorithm>

using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

const double PI = acos(-1.0);

bool ok(VS &a, char z) {
	FOR(i,0,4) {
		int r = 0;
		FOR(j,0,4) {
			if(a[i][j]==z || a[i][j]=='T')
				r++;
		}
		if(r==4)
			return true;
	}
	FOR(j,0,4) {
		int r = 0;
		FOR(i,0,4) {
			if(a[i][j] == z || a[i][j] =='T')
				r++;
		}
		if(r==4)
			return true;
	}

	int r = 0;
	FOR(i,0,4)
		if(a[i][i]==z || a[i][i]=='T') r++;
	if(r==4)
		return true;

	r = 0;
	FOR(i,0,4)
		if(a[3-i][i]==z || a[3-i][i]=='T') r++;

	if(r==4)
		return true;

	return false;
}

void Solve() {
	VS a(4);
	FOR(i,0,4) {
		cin >> a[i];
	}
	if(ok(a,'X') ) {
		printf("X won");
		return ;
	}

	if(ok(a,'O') ) {
		printf("O won");
		return ;
	}

	FOR(i,0,4) {
		FOR(j,0,4) {
			if(a[i][j]=='.') {
				printf("Game has not completed");
				return ;
			}
		}
	}
	printf("Draw");
}

int main() {
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		printf("Case #%d: ",CUR_TEST);
		Solve();
		printf("\n");
	}
	return 0;
}