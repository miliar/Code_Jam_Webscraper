#include <string>      
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

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
#define y1 botva

const int nmax = 110;

int n,res;
int x1[nmax], y1[nmax],x2[nmax],y2[nmax];
int b[250][250];
int a[250][250];

void solve(){
	memset(a,0,sizeof a);
	cin >> n;
	forn(i,n)
		scanf("%d %d %d %d", &x1[i], &y1[i], &x2[i], &y2[i]);
	int res = 0;
	forn(i,n)
		for (int j = x1[i]; j <= x2[i]; j++)
			for (int k = y1[i]; k <= y2[i]; k++)
				a[j][k] = 1;
	while(1){
	memset(b,0,sizeof b);
		int cnt = 0;
		forn(i,nmax)
			forn(j,nmax)
				if (a[i][j] == 1){
					cnt ++;
					if (a[i-1][j] == 1 || a[i][j-1] == 1)
						b[i][j] = 1;
					if (a[i+1][j-1] == 1)
						b[i+1][j] = 1;
				}
		if (cnt == 0) break;
		res ++;
		forn(i,nmax)
			forn(j,nmax)
				a[i][j] = b[i][j];
	}
				
	cout << res << endl;
}

int main(){
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		printf("Case #%d: ", i+1);
		solve();
	}

        return 0;
}
