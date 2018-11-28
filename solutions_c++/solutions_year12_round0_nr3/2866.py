#include <climits>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)
#define FOR(i,n)    for(int i=0;i<(n);++i)

#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back

bool recycled(string n, string m) {
	//cout << "\tREC: " << n << " " << m << endl;
	int cnt = 0;
	bool leading;
	string tmp;
	int l = n.length();
	FOR(i, l) {
		tmp = m.substr(l - i, l);
		tmp += m.substr(0, l - i);
		//cout << "i: " << i << " NM: " << tmp << endl;
		if(tmp[0] == '0') continue;
		if(tmp == n) return true;
	}
	return false;
}

int main() {
	freopen("d.in",  "r", stdin);
	freopen("d.out", "w", stdout);

	int a, b;
	int cnt;
	char BUFF[64];
	string N, M;
	int tt;
	cin>>tt;
	REP(t,tt) {
		printf("Case #%d: ", t);
		cin>>a>>b;
		cnt = 0;
		FORE(n, a, b + 1) {
			FORE(m, a + 1, b + 1) {
				if(n >= m) continue;
				//cout << "n = " << n << " m = " << m << endl;
				sprintf(BUFF, "%d", n);
				N = BUFF;
				sprintf(BUFF, "%d", m);
				M = BUFF;
				if(recycled(N, M)) ++cnt;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}
