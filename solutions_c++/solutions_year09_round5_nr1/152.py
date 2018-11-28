#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORD(i,n) for (int i=n-1; i>=0; --i)
#define FORALL(s,x) for (typeof(s.begin()) x=s.begin(); x!=s.end(); ++x) 
#define PRINT(s) {FORALL(s,v) cout << *v << " "; cout << endl;}
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define int64 long long

#define MAX 15

int m, n;
char board[MAX][MAX];

pii box[2];

void input() {
	scanf("%d%d", &m, &n);
	FOR(i,m) scanf("%s", board[i]);
}

const int di[]={1,-1,0,0};
const int dj[]={0,0,1,-1};

int opposite(int d) {
	if (d<=1) return 1-d;
	else return 5-d;
}

pii next(pii a, int d) {
	return mp(a.first+di[d], a.second+dj[d]);
}

char getCell(pii a) {
	if (0<=a.first && a.first < m &&
		0<=a.second && a.second < n)
		return board[a.first][a.second];
	else
		return 'o'; //outside
}

int dist[MAX][MAX][MAX][MAX];

struct Stat{
	pii a, b;
	Stat(pii a, pii b):a(a),b(b){}
	Stat() {}
	void setDist(int d) {
		dist[a.first][a.second][b.first][b.second]=d;
	}
	
	int getDist() {
		return dist[a.first][a.second][b.first][b.second];
	}

	bool feasible() {
		return (a.first==b.first && abs(a.second - b.second) == 1)
			|| (a.second==b.second && abs(a.first - b.first) == 1);
	}
	
	bool isGoal() {
		return getCell(a)=='x' && getCell(b)=='x';
	}
	
	void print() {
		cout << "Config: (" << a.first+1 << " " << a.second+1 <<") (" << b.first+1 << " " << b.second+1 <<") " << feasible() << " " << getDist() << endl;
	}
};

bool canMove(pii a, Stat s, int d) {
	pii p1=next(a,opposite(d));
	pii p2=next(a,d);
	char c1=getCell(p1);
	char c2=getCell(p2);	
	return p1!=s.a && p1!=s.b && p2!=s.a && p2!=s.b && c1=='.' && (c2=='.' || c2=='x');
}


bool canMove(pii a, int d) {
	pii p1=next(a,opposite(d));
	pii p2=next(a,d);
	char c1=getCell(p1);
	char c2=getCell(p2);	
	return (c1=='.' || c1=='x') && (c2=='.' || c2=='x');
}

bool correctMove(Stat u, Stat v) {
	if (u.feasible()) return (v.a!=v.b);
	return v.feasible();
}

int result;

void solve2() {
	queue<Stat> q;
	Stat start(box[0], box[1]);	
	q.push(start);	
	
	memset(dist, -1, sizeof(dist));	
	start.setDist(0);	
	
	while (!q.empty()) {
		Stat u=q.front();
//		u.print();
		q.pop();
		if (u.isGoal()) {
			result=u.getDist();
			break;
		}
		
		FOR(d,4) {
			Stat v;
			v=u;
			if (canMove(v.a, u, d)) {
				v.a=next(v.a, d);
				//v.print();
				if (correctMove(u,v) && v.getDist()==-1) {
					v.setDist(u.getDist()+1);
					q.push(v);
				}
			}
			
			v=u;
			if (canMove(v.b, u, d)) {
				v.b=next(v.b, d);
				//v.print();
				if (correctMove(u, v) && v.getDist()==-1) {
					v.setDist(u.getDist()+1);
					q.push(v);
				}
			}
		}
	}	
}

int dist1[MAX][MAX];

void solve1() {
	queue<pii> q;	
	q.push(box[0]);	
	
	memset(dist1, -1, sizeof(dist1));	
	dist1[box[0].first][box[0].second]=0;
	
	while (!q.empty()) {
		pii u=q.front();
//		cout << u.first << " " << u.second << endl;
		if (getCell(u)=='x') {
			result=dist1[u.first][u.second];
			break;
		}
		q.pop();
		
		FOR(d,4) {
			pii v=u;			
			if (canMove(v, d)) {
				v=next(v, d);
				if (dist1[v.first][v.second]==-1) {
					dist1[v.first][v.second]=dist1[u.first][u.second]+1;
					q.push(v);
				}
			}
		}
	}		
}

void solve() {
	int k=0;
	result=-1;
	FOR(i,m) FOR(j,n)
		if (board[i][j]=='o') {
			if (k==2) {
				assert(false);
				return;
			}
			board[i][j]='.';
			box[k]=mp(i,j);
			++k;
		} else if (board[i][j]=='w') {
			if (k==2) {
				assert(false);				
				return;
			}
			board[i][j]='x';
			box[k]=mp(i,j);
			++k;
		}
	
	if (k==2) solve2();
	else solve1();
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nTest;
	scanf("%d", &nTest);
	for (int test=1; test<=nTest; ++test) {
		input();
		solve();
		printf("Case #%d: %d\n", test, result);
	}
	return 0;
}
