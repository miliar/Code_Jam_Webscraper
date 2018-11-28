#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int t, h, w;
int G[100][100], P[100][100];
int ind;


int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int go(int a, int b) {
	if (P[a][b] != -1) {
		return P[a][b];
	} 
	
	int la = -1, lb = -1, lv = inf;
	REP(k, 4) {
		int na = a + dx[k], nb = b + dy[k];
		if (na >= 0 && na < h && nb >= 0 && nb < w) {
			if (G[na][nb] < G[a][b] && G[na][nb] < lv) {
				la = na, lb = nb, lv = G[na][nb];
			}
		}
	}
	if (la != -1) {
		return P[a][b] = go(la, lb);
	} else {
		return P[a][b] = ind++;
	}
}

int main() {

	cin>>t;
	REP(_t, t) {
		cout << "Case #" << _t + 1 << ":" << endl;
		cin>>h>>w;
		REP(i, h) REP(j, w) cin>>G[i][j];
		memset(P, -1, sizeof(P));
		ind = 0;
		REP(i, h) REP(j, w) {
			go(i, j);
			
		}
		REP(i, h) {
			REP(j, w) {
				if (j) cout << ' ';
				cout << char('a' + P[i][j]);
			}
			cout << endl;
		}
	}
	return 0;
}