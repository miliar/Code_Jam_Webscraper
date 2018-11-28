
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

const int MAXH = 1000000000;
int next[2100];
int h[2100];
bool calc(int id1, int id2){
	if(id1 + 1 >= id2)return true;
	vi order;
	int id = id1 + 1;
	while(id < id2){
		order.pb(id);
		id = next[id];
	}
	if(id > id2){
//	cout << id1 << " "<< id2 << " " << id << endl;
		return false;
	}
	int to = id2;
	ll dx,dx0, dy,dy0;
	dx = dx0 = id2 - id1; dy0 = dy = h[id2] - h[id1];
	FORD(i,0,sz(order)){
		int n = order[i];
		int ddx = to - n;
		ll nh = h[to] - (ddx * dy + dx - 1) / dx;
		h[n] = nh;
		ll ndx = ddx;
		ll ndy = h[to] - h[n];
		while(ndy * dx < ndx * dy || ndy * dx0 <= ndx * dy0){
			--h[n];
			ndy = h[to] - h[n];
		}
		if(!calc(n,to))return false;
		to = n;
		dx = ndx;
		dy = ndy;
	}
	return true;
}
int main() {
	int tc, N;
	cin >> tc;
	FOR(tcc,1,tc+1){
		cin >> N;
		FOR(i,0,N-1)cin >> next[i];
		FOR(i,0,N-1)--next[i];
		h[0] = MAXH;
		int cur = 0;
		bool suc = 1;
		while(cur != N-1 && suc){
			h[next[cur]] = MAXH;
			suc &= calc(cur, next[cur]);
			cur = next[cur];
		}
		cout << "Case #" << tcc <<":";
		if(suc){
			int mh = MAXH;
			FOR(i,0,N)mh = min(h[i], mh);
			FOR(i,0,N)h[i] -= mh;
			FOR(i,0,N)cout <<" " << h[i];
			cout << endl;
		} else {
			cout << " Impossible\n";
		}
	}
	return 0;
}
