//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<double>          VD;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef	pair<double,PII>        EL;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

int n,m,h;
VVI c;
VVI r;

const double MX = 2.0*10000.0*10000.0*10000.0;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

bool ok(int i, int j) {
	return (i>=0 && j>=0 && i<n && j<m);
}

double mint(PII a, PII b, double time) {
	//-1 if cannot, else min time
	if( r[a.X][a.Y]+50 > c[b.X][b.Y] )
		return -1.0;
	if( r[b.X][b.Y]+50 > c[b.X][b.Y] )
		return -1.0;
	if( c[a.X][a.Y]-50 < r[b.X][b.Y] )
		return -1.0;
	double level = h - 10.0*time;
	level = max(0.0,level-r[a.X][a.Y]*1.0);
	if(level+r[a.X][a.Y] + 50>c[b.X][b.Y]) {
		//way1  - чекаємо, доки знизиться до прийнятної різніці, отже
		double ac_level = c[b.X][b.Y] - 50;
		double ap_time = (r[a.X][a.Y] + level - ac_level)/10.0;
		double nw_level = level - (r[a.X][a.Y] + level - ac_level);
		if(nw_level < 20) {
			double res = 10 + ap_time;
			return res;
		}
		else {
			double res = 1.0 + ap_time;
			return res;
		}
	}
	else {
		if(level < 20) {
			double res = 10;
			return res;
		}
		else {
			double res = 1.0;
			return res;
		}
	}
	return -1;
}

bool prec(PII a, PII b) {
	//-1 if cannot, else min time
	if( r[a.X][a.Y]+50 > c[b.X][b.Y] )
		return false;
	if( r[b.X][b.Y]+50 > c[b.X][b.Y] )
		return false;
	if( c[a.X][a.Y]-50 < r[b.X][b.Y] )
		return false;
	double level = h;
	if(max(h,r[a.X][a.Y]) + 50>c[b.X][b.Y]) {
		return false;
	}
	else {
		return true;
	}
}

void solve() {

	cin >> h >> n >> m;
	//n = m = 100; h = 10000;
	c.resize(n);
	FOR(i,0,n) {
		c[i].resize(m);
		FOR(j,0,m) {
			//c[i][j] = 10000;
			scanf("%d",&c[i][j]);
		}
	}
	r.resize(n);
	FOR(i,0,n) {
		r[i].resize(m);
		FOR(j,0,m) {
			//r[i][j] = 0;
			scanf("%d",&r[i][j]); 
		}
	}
	vector< vector<double> > D(n,VD(m,MX));
	set< pair<double, PII> > q;

	queue<PII> p;
	p.push(MP(0,0));
	while(!p.empty()) {
		PII z = p.front();
		p.pop();
		int x = z.X;
		int y = z.Y;
		FOR(i,0,4) {
		if ( ok(x+dx[i],y+dy[i]) ) {
			bool dt = prec(z,MP(x+dx[i],y+dy[i]));
			if( dt ) {
				if(D[x+dx[i]][y+dy[i]]!=0) {
					p.push( MP(x+dx[i],y+dy[i]) );
					D[x+dx[i]][y+dy[i]] = 0;
					q.insert( MP( 0.0,MP(x+dx[i],y+dy[i]) ) );
				}
			}
		}
		
		}
	}

	q.insert( MP(0.0, MP(0,0)) );
	D[0][0] = 0;
	while(!q.empty()) {
		EL t = *q.begin();
		int x = t.second.X;
		int y = t.second.Y;
		q.erase(t);
		double time = t.first;
		FOR(i,0,4) {
			if ( ok(x+dx[i],y+dy[i]) ) {
				double dt = mint(t.second,MP(x+dx[i],y+dy[i]),t.first);
				if(dt<-0.5)
					continue;
				if( D[x+dx[i]][y+dy[i]] > dt+D[x][y] ) {
					D[x+dx[i]][y+dy[i]] = dt + D[x][y];
					q.insert( MP( dt+D[x][y],MP(x+dx[i],y+dy[i]) ) );
				}
			}
		}
	}
	printf("%.6f\n",D[n-1][m-1]);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int A_TESTS;
	cin >> A_TESTS;
	//A_TESTS = 1;
	FOR(SYS_TEST,0,A_TESTS) {

		printf("Case #%d: ",SYS_TEST+1);

		solve();
	}
	return 0;
}