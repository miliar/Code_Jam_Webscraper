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
	map<int,int> M;
	int n;
	scanf("%d",&n);
	VI a(n);
	FOR(i,0,n)
		scanf("%d",&a[i]);
	FOR(i,0,1<<n) {
		int s = 0;
		FOR(j,0,n) {
			if( i & (1<<j))
				s += a[j];
		}
		if(M.find(s)!=M.end()) {
			int mask = i;
			bool first = true;
			FOR(j,0,n) {
				if( (1<<j) & mask ) {
					if(!first)
						cout << " ";
					first = false;
					cout << a[j];
				}
			}
			cout << endl;
			first = true;
			mask = M[s];
			FOR(j,0,n) {
				if( (1<<j) & mask ) {
					if(!first)
						cout << " ";
					first = false;
					cout << a[j];
				}
			}
			cout << endl;
			return ;
			//
		}
		else
			M[s] = i;
	}
	cout << "Impossible\n";
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int A_TESTS;
	cin >> A_TESTS;
	FOR(SYS_TEST,0,A_TESTS) {

		printf("Case #%d:\n",SYS_TEST+1);

		solve();
	}
	return 0;
}