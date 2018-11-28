#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

typedef pair<short,short> P;

struct U {
	P parent;
	char corners;
	char sides;
	bool add;
};
const int MN = 3010;
U board[2*MN][2*MN];

P par(int x, int y) {
	U& u = board[y][x];
	P& p = u.parent;
	if (x==p.first && y==p.second) return p;
	return p = par(p.first, p.second);
}
void join(int x1, int y1, int x2, int y2) {
	P p = par(x2,y2);
	P q = par(x1,y1);
	x1 = q.first, y1 = q.second;
	board[y1][x1].parent = p;
	int x=p.first, y = p.second;
	board[y][x].corners |= board[y1][x1].corners;
	board[y][x].sides |= board[y1][x1].sides;
//	cout<<"joining "<<x1<<' '<<y1<<" - "<<x2<<' '<<y2<<" : "<<(int)board[y][x].corners<<' '<<(int)board[y][x].sides<<'\n';
}
U& getp(int x, int y) {
	P p = par(x,y);
	return board[p.second][p.first];
}

const int dx[] = {1,0,-1,-1,0,1};
const int dy[] = {1,1,0,-1,-1,0};
int S,M;

bool out(int x, int y) {
	if (x<1 || y<1) return 1;
	if (x>=2*S || y>=2*S) return 1;
	if (x>S && y<=x-S) return 1;
	if (y>S && x<=y-S) return 1;
	return 0;
}

char corner(int x, int y) {
	if (x==1 && y==1) return 1;
	if (x==1 && y==S) return 2;
	if (x==S && y==2*S-1) return 4;
	if (x==2*S-1 && y==2*S-1) return 8;
	if (x==2*S-1 && y==S) return 16;
	if (x==S && y==1) return 32;
	return 0;
}
char side(int x, int y) {
	if (corner(x,y)) return 0;
	if (x==1) return 1;
	if (y==x+S-1) return 2;
	if (y==2*S-1) return 4;
	if (x==2*S-1) return 8;
	if (x==y+S-1) return 16;
	if (y==1) return 32;
	return 0;
}

bool testB(vector<P> ps, P p) {
	vector<int> v(6);
	for(int i=0; i<6; ++i) {
		v[i] = ps[i]==p;
	}
	v.erase(unique(v.begin(),v.end()),v.end());
	return v.size()>=4;
}

vector<string> res;
void insert(int x, int y) {
	U& u = board[y][x];
	u.corners = corner(x,y);
	u.sides = side(x,y);
	u.add = 1;
//	cout<<"k "<<x<<' '<<y<<" : "<<(int)u.corners<<' '<<(int)u.sides<<'\n';

	vector<P> ps(6);
	for(int i=0; i<6; ++i) {
		int xx = x+dx[i], yy = y+dy[i];
		if (out(xx,yy)) continue;
		U& uu = board[yy][xx];
		if (!uu.add) continue;
		ps[i] = par(xx,yy);
	}
	bool bridge = 0;
	for(int i=0; i<6; ++i) if (ps[i].first) bridge |= testB(ps, ps[i]);

	for(int i=0; i<6; ++i) {
		int xx = x+dx[i], yy = y+dy[i];
		if (out(xx,yy)) continue;
		U& uu = board[yy][xx];
		if (!uu.add) continue;
		join(x,y,xx,yy);
	}
	U& uu = getp(x,y);
	if (__builtin_popcount(uu.corners)>=2) res.push_back("bridge");
	if (__builtin_popcount(uu.sides)>=3) res.push_back("fork");
	if (bridge) res.push_back("ring");
}

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>S>>M;
		for(int i=0; i<2*S; ++i) for(int j=0; j<2*S; ++j) board[i][j].parent = P(j,i), board[i][j].add=0;


		res.clear();
		bool done=0;
		cout<<"Case #"<<a<<": ";
		for(int i=1; i<=M; ++i) {
			int x,y;cin>>x>>y;
			if (done) continue;

			insert(x,y);

			if (!res.empty()) {
				cout<<res[0];
				for(size_t j=1; j<res.size(); ++j) cout<<'-'<<res[j];
				cout<<" in move "<<i<<'\n';
				done=1;
			}
		}
		if (!done)cout<<"none\n";
	}
}
