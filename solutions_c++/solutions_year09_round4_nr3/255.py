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

int n,k;
int a[200][200];
bool used[200];
int next[200];
int res;
bool g[200][200];
bool inp[200];
int p[200];

int find_next(int i){
	int res = i + 1;
        while(1){
		bool done = 1;
		forn(j,k)
			if (a[i][j] >= a[res][j])
				done = 0;
		if (used[res]) done = 0;
		if (!done) res++;
		if (res >= n || done) break;
		}
	return res;
}

bool can(int i,int j){
	bool done = 1;
	forn(l,k)
		if (a[i][l] <= a[j][l])
			done = 0;
	return done;
}

bool go(int v){
	used[v] = 1;
	forn(i,n)
		if (g[v][i]){
		if (p[i] == -1 || (!used[p[i]] && go(p[i]))){
			inp[v] = 1;
			p[i] = v;
			return 1;
		}
	}
	return 0;
}
		

int main(){
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int tst;
	cin >> tst;
	forn(qwe,tst){
		cin >> n >> k;
		forn(i,n)
			forn(j,k)
				cin >> a[i][j];
		res = 0;
		memset(used,0,sizeof used);
		forn(i,n)
			forn(j,n)
				if (can(i,j)){
					g[i][j] = 1;
//					cerr << i << " " << j << endl;
				}else
				g[i][j] = 0;
		int match = 0;
		memset(inp, 0, sizeof inp);
		memset(p,255,sizeof p);
		forn(i,n)
			if (!inp[i]){
				memset(used,0,sizeof used);
				if (go(i))
					match++;
			}
//		cerr << match << endl;
		res = n - match;		       
		printf("Case #%d: %d\n", qwe+1, res);
	}
			

}
