//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
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
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<double>          VD;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
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
int n,k;
VD p;

void solve2() {
	double ans = 1 + n + 1;
	double prob = 1.0;
	vector<double> R(k);
	FOR(i,0,k) {
		//i - first mistake
		double tmp = prob * (1.0-p[i]);

		R[i] = (prob *= p[i]);
	}

	//backspaces done
	FOR(i,0,k) {
		double tans = R[k-i-1]*(2*i+n-k+1) + (1-R[k-i-1])*(2*i+n-k+1+n+1);
		ans = min(tans, ans);
	}
	ans = min(ans, k+n+1.0);

	printf("%.6f\n",ans);
}

void solve() {

	vector< vector<int> > turns(k+3);
	//enter - 0
	//finish - 1
	vector<double> R(1<<k);
	FOR(mask,0,1<<k) {
		double pr = 1;
		double last = -1;
		FOR(i,0,k) {
			if(mask & (1<<i) ) {
				if(last==-1)
					last = i;
				pr = pr*(1.0-p[i]);
			}
			else
				pr = pr*p[i];
		}
		R[mask] = pr;
		//enter
		turns[0].PB(2+n);
		//complete
		turns[1].PB( (!mask)?n-k+1:n-k+1+n+1 );
		//backspace X times
		FOR(i,0,k) {
			if(i<=last || last==-1) {
				turns[i+2].PB( 2*(k-i) + (n-k) + 1 );
			}
			else
				turns[i+2].PB( 2*(k-i) + (n-k) + 1 + n + 1 );
		}
	}
	double res = INF;
	FOR(i,0,k+2) {
		double tres = 0.0;
		FOR(j,0,1<<k) {
			tres += turns[i][j]*R[j];
		}
		res = min(res,tres);
	}
	printf("%.6f ",res);
}

int main()
{
	freopen("AL.in","r",stdin);
	freopen("out.txt","w",stdout);
	int A_TESTS;
	cin >> A_TESTS;
	FOR(SYS_TEST,0,A_TESTS) {
		cin >> k >> n;

		p.clear();
		p.resize(k);
		FOR(i,0,k)
			cin >> p[i];
		printf("Case #%d: ",SYS_TEST+1);

		//solve();
		solve2();
	}
	return 0;
}