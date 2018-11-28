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


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int testt;
	cin >> testt;
	FOR(test,0,testt) {
		int n;
		int s,p;
		cin >> n;
		cin >> s >> p;
		int can_only = 0, can = 0;
		int score = max(p,3*p-2);
		int mn_score = max(p,3*p-4);
		FOR(i,0,n) {
			int t;
			cin >> t;
			if( t<mn_score )
				continue;
			if( t>=score )
				can++;
			else
				can_only++;
		}
		int ans = can + min(s,can_only);
		printf("Case #%d: %d\n",test+1,ans);
	}
	return 0;
}