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
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

const int px[] = {1,0,-1,0};
const int py[] = {0,1,0,-1};
const int nmax = 15;

map<int64, int> h;


int n,m;
char a[nmax][nmax];
int res;

int64 hash(vector<pii> now){
	sort(all(now));
	forn(i,now.size()){
		now[i].fs ++;
		now[i].sc ++;
	}
	int64 res = 1;
	forn(i,now.size()){
		res = (res * (int64)now[i].fs*5) + 771ll;
		res = (res * (int64)now[i].sc*7) + 997ll;
	}
	return res;
}

bool check(int x, int y, vector<pii> &now){
	if (x < 0 || y < 0) return 0;
	if (x >= n || y >= m) return 0;
	if (a[x][y] == '#') return 0;
	forn(e,now.size())
		if (mp(x,y) == now[e])
			return 0;
	return 1;
}

bool stable(vector<pii> now){
	vector<bool> go(now.size(), 0);
	queue<pii> q;
	q.push(now[0]);
	go[0] = 1;
	while (!q.empty()){
		pii e = q.front();
		q.pop();
		forn(j,now.size())
			if (!go[j])
			forn(k,4){
				int nx = e.fs + px[k];
				int ny = e.sc + py[k];
				if (mp(nx,ny) == now[j]){
					go[j] = 1;
					q.push(now[j]);
				}
			}
	}
	forn(i,now.size())
		if (!go[i]) return 0;
	return 1;

}
				


void solve(){
	h.clear();
	res = -1;
	queue<vector<pii> > q;
	vector<pii> now, end;
	forn(i,n)
		forn(j,m){
			if (a[i][j] == 'x' || a[i][j] == 'w')
				end.pb(mp(i,j));
			if (a[i][j] == 'o' || a[i][j] == 'w')
				now.pb(mp(i,j));
				
		}
	sort(all(now));
	q.push(now);
	h[hash(now)] = 1;
	int64 last = hash(end);
//	cout << last << endl;
//	
//	forn(i,now.size())
//		cout << end[i].fs << " " << end[i].sc << endl;
//	cout << endl;

//	cerr << now.size() << endl;
	while(!q.empty()){

		if (h[last] != 0)
			break;
		now = q.front();
		q.pop();
		int cost = h[hash(now)];
//		forn(i,now.size())
//			cout << now[i].fs << " " << now[i].sc << endl;
//		cout <<cost << " " << hash(now) << endl << endl;
		bool st = stable(now);
		forn(i,now.size())
			forn(j,4)
				if (check(now[i].fs - px[j], now[i].sc - py[j], now) && check(now[i].fs + px[j], now[i].sc + py[j], now)){
				now[i].fs += px[j];
				now[i].sc += py[j];
				bool how = stable(now);
				int64 f = hash(now);
				if ((st || how) && (h[f] == 0)){
//		forn(i,now.size())
//			cout << now[i].fs << " " << now[i].sc << endl;
//		cout << f << endl;
					h[f] = cost + 1;
					q.push(now);
				}
				now[i].fs -= px[j];
				now[i].sc -= py[j];
			}
	}
	while(!q.empty())
		q.pop();
	if (h[last] == 0)
		res = -1;
	else	
		res = h[last] - 1;

}
					

	

void read(){
	cin >> n >> m;
	forn(i,n)
		forn(j,m)
			cin >> a[i][j];
}

int main(){
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		read();
		solve();
		printf("Case #%d: %d\n", i+1, res);
	}

}
