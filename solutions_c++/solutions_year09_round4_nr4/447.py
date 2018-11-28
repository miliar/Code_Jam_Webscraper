#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()
#define FILL(a, i) memset((a), (i), sizeof(a))
#define MAX(a, b) (((a)>(b))?(a):(b))
#define MIN(a, b) (((a)<(b))?(a):(b))
#define SQ(x) ((x)*(x))

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pii pair<int, int>
#define pis pair<int, string>
#define psi pair<string, int>

#define INF 999999999
#define PI 3.141592654

typedef struct { int x, y, r; } circ;

int main(void)
{
	int T, n;
	cin >> T;
	circ a[10];
	for(int caso=1; caso<=T; caso++) {
		cin >> n;
		REP(i, n) {
			cin >> a[i].x >> a[i].y >> a[i].r;
		}
		
		cout << "Case #" << caso << ": ";
		
		if(n==1) cout << a[0].r;
		else if(n==2) cout << MAX(a[0].r, a[1].r);
		else {
			double res=999999999.0;
			res = MIN(res, MAX(a[0].r, (a[1].r+a[2].r+sqrt((double)(SQ(a[1].x-a[2].x) + SQ(a[1].y-a[2].y))))/2.0));
			res = MIN(res, MAX(a[1].r, (a[0].r+a[2].r+sqrt((double)(SQ(a[0].x-a[2].x) + SQ(a[0].y-a[2].y))))/2.0));
			res = MIN(res, MAX(a[2].r, (a[1].r+a[0].r+sqrt((double)(SQ(a[1].x-a[0].x) + SQ(a[1].y-a[0].y))))/2.0));
			cout << res;
		}
		cout << endl;
	}

	return 0;
}
