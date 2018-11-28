#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 2e9
#define MAX 2000001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int vis[MAX];
int memo[MAX];
int dx[] = { };
int dy[] = { };

inline bool valid(int a, int b) {
	int t, c = 0, m = a, cnt = 0;
	while (m)
		cnt++, m /= 10;
	cnt--;
	m = a % 10, c = a / 10;
	while (true) {
		m *= (int) pow(10.0, cnt);
		m += c;
		if (m == b && a != b)
			return true;
		if (m == a)
			return false;
		t = c;
		c = m / 10;
		m = t % 10;
	}
	return false;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
#endif
	int t, m, a, cnt, b, res, c, tmp;
	cin >> t;
	FOR (n , 0 , t) {
		mem (vis , 0);
		res = 0;
		cin >> a >> b;
		FOR (i , a , b+1) {
			FOR (j , i , b+1) {
				if (valid(i, j)) {
					res++;
					//					cout << i << " " << j << endl;
				}
			}
		}
		printf("Case #%d: %d\n", n + 1, res);
	}
	return 0;
}
