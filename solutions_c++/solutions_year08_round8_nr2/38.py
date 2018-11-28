#include<iostream> 
#include<sstream> 
#include<cstdlib> 
#include<cmath> 
#include<vector> 
#include<string> 
#include<algorithm>
#include<map>
using namespace std; 
typedef vector<int>VI;typedef vector<VI>VVI; 
typedef vector<string>VS; 
typedef pair<int,int>PII; 
#define FOR(i,n) for((i)=0;(i)<(n);(i)++) 
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--) 
#define BE(a) ((a).begin()),((a).end()) 
#define SI(a) ((a).size()) 
#define PB push_back 
#define MP make_pair 
#define FORIT(i,a) for((i)=(a).begin();(i)!=(a).end();(i)++) 
#define CLR(a,v) memset((a),(v),sizeof(a)) 

vector<vector<PII>> a;
map<string,int> names;
int n, m;

int solve(int X, int Y, int Z) {
	int ret, last, x, y, z, cur;
	ret = 0;
	last = 0;
	x = y = z = 0;
	while (last < 10000 && (x < SI(a[X]) || y < SI(a[Y]) || z < SI(a[Z]))) {
		cur = last;
		while (x < SI(a[X]) && a[X][x].first <= last + 1) {
			cur = max(cur, a[X][x].second);
			x++;
		}
		while (y < SI(a[Y]) && a[Y][y].first <= last + 1) {
			cur = max(cur, a[Y][y].second);
			y++;
		}
		while (z < SI(a[Z]) && a[Z][z].first <= last + 1) {
			cur = max(cur, a[Z][z].second);
			z++;
		}
		if (cur <= last) break;
		last = cur;
		ret++;
	}
	if (last < 10000) return 1000000;
	else return ret;
}

int main() {
	int ans, cases, casen, i, j, x, y, k;
	string s;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n;
		m = 0;
		names.clear();
		a.clear();
		FOR (k,n) {
			cin >> s >> x >> y;
			if (!names.count(s)) {
				names[s] = m++;
				a.PB(vector<PII>(0));
			}
			a[names[s]].PB(MP(x, y));
		}
		FOR (i,m) sort(BE(a[i]));
		ans = 1000000;
		FOR (i,m) FOR (j,i+1) FOR (k,j+1) {
			ans = min(ans, solve(i, j, k));
		}
		cout << "Case #" << casen << ": ";
		if (ans < 1000000) cout << ans;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
