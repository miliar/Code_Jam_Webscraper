#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define FOR(i,a,b) for(__typeof(b) i=(a);i!=(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define EACH(i,a) FOR(i,a.begin(),a.end())
#define PB push_back
#define iss istringstream
#define SZ(a) (int)a.size()
#define CLEAR(a) memset(a,0,sizeof(a))
#define ll long long

bool vis[2000005];

ll ans;
int T;
ll x, y;
inline void process(int n) {
	ostringstream out;
	out << n;
	string s = out.str();
	int L = s.size();
	int mult = 1;
	for(int i = 1; i < L ; i++) {mult *= 10;}
	set< int > st;
	
	for(int i = 0 ; i < L + 5 ; i++) {
		n = (n / 10) + mult * (n % 10);
		if (x <= n && y >= n) {st.insert(n);}
	}
	EACH(it, st) {
		vis[(*it)] = true;
	}
	int S = SZ(st);
	ans += (((S - 1) * S) / 2);
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		//int x, y;
		cin >> x >> y;
		memset(vis, 0, sizeof(vis));
		ans = 0;
		for(int i = x ; i <= y ; i++) {
			if (!vis[i]) {
				process(i);
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}



	return 0;
}
