#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <string.h>
#include <cassert>

#ifdef _DEBUG
#define typeof(X) std::identity<decltype(X)>::type //C++0x (for vs2010)
#else
#define typeof(X) __typeof__(X) // for gcc
#endif

#define sz(a)  int((a).size())
#define FOREACH(it, c) for (typeof((c).begin()) it=(c).begin(); it != (c).end(); ++it)
#define FOR(i,count) for (int i = 0; i < (count); i++)
#define V_CIN(v) do{for(int i = 0; i < sz(v); i++) cin >> (v)[i];}while(0)
#define all(c) (c).begin(),(c).end()

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
const int MODULO = 1000000007;
const int INF = 100000000; //1e8

typedef pair<int,int> Pii;

int N;
vector<int> m[1000];

bool table[1000];

bool solve()
{
	cin >> N;
	FOR(i,1000) m[i].clear();

	FOR(i,N){
		int x; cin >> x;
		FOR(j,x){
			int y; cin >> y; y--;
			m[i].push_back(y);
		}
	}


	FOR(i,N){
		queue<int> q; q.push(i);
		fill(table,table+1000,false);
		while(!q.empty()){
			int id = q.front(); q.pop();
			table[id] = true;
			FOREACH(it,m[id]){
				if(table[*it]) return true;
				table[*it] = true;
				q.push(*it);
			}
		}
	}

	return false;
}

int main(){
	int t;
	cin >> t;
	FOR(i,t){
		bool b = solve();
		printf("Case #%d: %s\n",i+1,((b) ?"Yes" : "No"));
	}
	return 0;
}