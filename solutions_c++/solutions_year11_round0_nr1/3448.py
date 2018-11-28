#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) (a.begin(),a.end())
#define rall(a) (a.rbegin(),a.rend())
#define INF (int)1e9
#define EPS (double)1e-9

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef pair< int, ii > pi;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

int main() {
	int T = GI;
	REP(t, T) {
		int N = GI;

		int i, k;
		char c;
		int ltime[2] = {0, 0};
		int lpos[2] = {1, 1};		

		REP(j,N) {
			cin >> c >> k;
			if (c == 'O') i = 0;
			else i = 1;

			ltime[i] = max(ltime[i]+abs(lpos[i]-k), ltime[1-i]) + 1;
			lpos[i] = k;
		}

		cout << "Case #" << t+1 << ": " << max(ltime[0], ltime[1]) << endl;
	}	
	return 0;
}
