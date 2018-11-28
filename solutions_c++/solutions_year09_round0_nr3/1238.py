#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int inf = (int)1E+9;

typedef long long int64;
typedef pair<int,int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define last(a) (int)a.size() - 1
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

string p ="welcome to code jam";

int t[1000][50];
string s;

void solve(){
	memset(t,0,sizeof t);
	getline(cin,s);
	int n = s.length();
	int m = p.length();
	t[0][0] = 1;

	forn(i,n)
		forn(j,m+1){
			t[i+1][j] = (t[i+1][j] + t[i][j]) % 10000;
			if (j < m && s[i] == p[j])
				t[i+1][j+1] = (t[i+1][j+1] + t[i][j]) % 10000;
			}
	printf("%04d\n", t[n][m]);
}

int main(){
	freopen ("c.in", "rt", stdin);
	freopen ("c.out", "wt", stdout);
	int tst;
	scanf("%d\n",&tst);
	forn(i,tst){
		printf("Case #%d: ",i+1);
		solve();
	}	

	return 0;
}
