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
#define MAX 10001
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

int main() {
#ifndef ONLINE_JUDGE
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);
#endif
	int t, x, res, N, S, P;
	cin >> t;
	FOR (n , 0 , t) {
		res = 0;
		cin >> N >> S >> P;
		FOR (i , 0 , N) {
			cin >> x;
			if (x == 0){
				if (P == 0)
					res ++;
				continue;
			}
			int a = x / 3, b = x % 3;
//			cout << a << " " << b << endl;
			if (b == 1){
				if (a + b >= P)
					res ++;
			}
			if (b == 0){
				if (a >= P){
					res ++;
					continue;
				}
				if (a + 1 >= P && S)
					res ++, S--;
			}
			if (b == 2){
				if (a + 1 >= P){
					res ++;
					continue;
				}
				else if (a + 2 >= P && S){
					res ++, S--;
				}
			}
		}
		printf("Case #%d: %d\n", n + 1, res);
	}
	return 0;
}
