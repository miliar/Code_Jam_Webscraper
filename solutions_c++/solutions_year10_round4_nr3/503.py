#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 
#include <iomanip>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define MAX(a,b) (((a) > (b)) ? (a) : (b))	
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define SQR(a) ((a)*(a))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;

ll gcd(ll a, ll b){return a == 0 ? b : gcd(b%a, a);}


string filename = "C-small-attempt0";



bool mem[2][500][500];
int cur = 0;

int di[] = {-1, 0};
int dj[] = {0, -1};
int minx, maxx, miny, maxy;

struct Rect{
	int x1, x2, y1, y2;
	bool cont(int x, int y){
		return x1 <= x && x <= x2 && y1 <= y && y <= y2;
	}
};

vector<Rect> rects;

void go(){
	int next = (cur ^ 1);
	memset(mem[next], false, sizeof(mem[next]));
	int nminx = 1000, nmaxx = 0, nminy = 1000, nmaxy = 0;
	FOR(i, minx, maxx + 2)FOR(j, miny, maxy + 2){
		int cntn = 0;
		REP(k, 2){
			int ni = i + di[k], nj = j + dj[k];
			if (ni >= 0 && ni <= maxx && nj >=0 && nj <= maxy){
				if (mem[cur][ni][nj])
					cntn++;
			}
		}
		if(mem[cur][i][j]){
			if (cntn  == 0)
				mem[next][i][j] = 0;
			else
				mem[next][i][j] = 1;
		}else{
			if (cntn == 2)
				mem[next][i][j] = 1;
			else
				mem[next][i][j] = 0;
		}
		if (mem[next][i][j]){
			nmaxx = MAX(i, nmaxx);
			nmaxy = MAX(j, nmaxy);
			nminx = MIN(i, nminx);
			nminy = MIN(j, nminy);
		}
	}
	maxx = nmaxx;
	maxy = nmaxy;
	miny = nminy;
	minx = nminx;
	cur = next;
}

int calc(){
	int ret = 0;
	FOR(i, minx, maxx + 2)FOR(j, miny, maxy + 2){
		if (mem[cur][i][j]){
			ret++;
		}
	}
	return ret;
}

int main(){
	string str_fin = filename + ".in";
	string str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);
	
	int T;
	cin>>T;
	REP(test, T){
		int r;
		cin>>r;
		rects.clear();
		memset(mem, false, sizeof(mem));
		minx = 100; maxx = 0; miny = 100; maxy = 0;
		REP(i, r){
			int x1, x2, y1, y2;
			cin>>x1>>y1>>x2>>y2;
			FOR(i, x1, x2+1)FOR(j, y1, y2+1)
				mem[0][i][j] = true;
			Rect rr;rr.x1 = x1; rr.x2 = x2; rr.y1 = y1; rr.y2 = y2;
			rects.pb(rr);
			minx = MIN(minx, x1);
			maxx = MAX(maxx, x2);
			miny = MIN(miny, y1);
			maxy = MAX(maxy, y2);
		}
		
		cur = 0;
		int res = 0;
		for(;;){
			if (calc() == 0)
				break;
			++res;
			go();
		}

		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}


	return 0;
}