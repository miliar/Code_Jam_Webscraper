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

void solve() {
	int n;
	cin >> n;
	VI a(n);
	int sum = 0;
	FOR(i,0,n) {
		cin >> a[i];
		sum += a[i];
	}
	double need = 0;
	VD res(n);
	FOR(i,0,n) {
		need = 0.0;
		double l = 0.0, r = 1.0;

		FOR(j,0,74) {
			need = (l+r)*0.5;
			double  rest = 1.0 - need;
			double my = a[i] + need*sum;
			FOR(k,0,n) if(i!=k && my>a[k]) {
				double t = (my-a[k])/(1.0*sum);
				rest -= t;
			}
			if(rest>0.0)
				l = need;
			else
				r = need;
		}
		res[i] = need*100.0;
	}
	FOR(i,0,n)
		printf("%.6f%c",res[i],i==n-1?'\n':' ');
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int A_TESTS;
	cin >> A_TESTS;
	FOR(SYS_TEST,0,A_TESTS) {

		printf("Case #%d: ",SYS_TEST+1);

		solve();
	}
	return 0;
}