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
typedef	pair<double,PII>        EL;
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
    VI d(n);
    vector<PII> r(n);
    FOR(i,0,n) {
        scanf("%d%d",&r[i].X,&r[i].Y);
    }
    int D;
    scanf("%d",&D);
    sort(ALL(r));
    VI mx(n,0);
    mx[0] = r[0].X;
    FOR(i,0,n) {
        FOR(j,i+1,n) {
            if( r[i].X+mx[i] >= r[j].X ) {
                mx[j] = max( mx[j], min(r[j].X-r[i].X,r[j].Y) );
            }
        }
    }
    FOR(i,0,n)
        if( mx[i]+r[i].X >= D ) {
            cout << "YES\n";
            return;
        }
    cout << "NO\n";
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