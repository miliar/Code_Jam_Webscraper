#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>
 
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

int main() {
	int test; scanf("%d",&test); REP(tt,test) {
		int m,n;
		scanf("%d%d",&m,&n);
		vector<string> V;
		string str;
		REP(i,m) cin >> str, V.pb(str);
		bool changed = true;
		while(changed) {
			changed = false;
			REP(i,m-1) REP(j,n-1) if(V[i][j] == '#') {
				if(V[i+1][j] != '#' || V[i+1][j+1] != '#') continue;
				if(V[i][j+1] != '#') continue;
				changed = true;
				V[i][j] = '/';
				V[i+1][j] = '\\';
				V[i][j+1] = '\\';
				V[i+1][j+1] = '/';
			}

			out:;
		}
		bool ok = true;
		REP(i,m) REP(j,n) if(V[i][j] == '#') ok = false;
		printf("Case #%d:\n",tt+1);
		if(ok) REP(i,m) cout << V[i] << endl;
		else cout << "Impossible" << endl;
	}
}

