#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iterator>
#include <numeric>
#include <complex>
using namespace std;

#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define REPD(i,n) for (int i = n-1; i >= 0; --i)
#define FOR(i,p,k) for (int i = p; i <= (int)(k); ++i)
#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> ostream& operator<<(ostream& os, const vector<T>& v) { REP(i,v.size()) os<<'['<<v[i]<<']'; return os; }
#define DEBUG(x) cerr<<#x":"<<(x)<<endl;

int a[1001][1001];
int b[1001][1001];
int size = 100;

int main() {
	int T; cin>>T;
	for (int cnum = 1; cnum <= T; cnum++) {
		memset(a,0,sizeof(a));
		int r; cin>>r;
		REP(i,r) {
			int x, y, xx, yy; cin>>x>>y>>xx>>yy;
			FOR(xi,x,xx) FOR(yi,y,yy) a[xi][yi] = 1;
		}
		int cnt = 0;
		bool flag = true;
		while (flag) {
			//REP(i,6) { REP(j,6) cout<<a[j][i]<<" "; cout<<endl; } cout<<endl;
			++cnt;
			flag = false;
			memset(b,0,sizeof(b));
			FOR(i,1,size) FOR(j,1,size) {
				if (a[i][j]+a[i-1][j]+a[i][j-1] >= 2) {
					b[i][j] = 1;
					flag = true;
				}
			}
			memcpy(a,b,sizeof(a));
		}
		cout<<"Case #"<<cnum<<": "<<cnt<<endl;
	}
	return 0;
}