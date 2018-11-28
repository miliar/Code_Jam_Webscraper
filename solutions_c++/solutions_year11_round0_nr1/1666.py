#define TSK "c"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cassert>

using namespace std;

#define ll long long
#define db double
#define rep(i,n) for(int (i) = 0;  (i) < (n); ++ (i))
#define forn(i,a,n) for(int (i) = (a);  (i) < (n); ++ (i))
#define tr(i,a) for(__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define PI pair<int,int>
#define fi first
#define se second
#define VPI vector<PI >
#define VVPI vector<VPI >
#define VI vector<int>
#define VII vector<VI >
#define VB vector<bool> 
#define VD vector<db>
#define VS vector<string>
#define INF 1000000000
#define deb(x) cerr <<"[line: " << __LINE__ << "] " #x " = " << x << endl
#define NONE 
int main(){
	int T;
	cin >> T;
	string s;
	rep(qwe,T){
		int n, t;
		char ch;
		cin >> n;
		vector<int> nm(n);
		vector<vector<int> > x(2);
		rep(i,n){
			cin >> ch >> t;
			ch = (ch == 'O') ? 0 : 1;
			nm[i] = ch;
			x[ch].pb(t - 1);
		}
		x[0].pb(1000);
		x[1].pb(1000);
		int pos[2] = {0, 0};
		int u[2] = {0, 0};
		int it = 0;
		while (u[0] + u[1] != n){
			++it;
			int c = nm[u[0] + u[1]];
			if (pos[c] == x[c][u[c]])
				u[c]++;
			else if (pos[c] < x[c][u[c]])
				pos[c]++;
			else pos[c]--;
			c ^= 1;
			if (pos[c] < x[c][u[c]])
				pos[c]++;
			else if (pos[c] > x[c][u[c]])
				pos[c]--;
		}
		printf("Case #%d: %d\n", qwe + 1, it);
	}
	return 0;
}