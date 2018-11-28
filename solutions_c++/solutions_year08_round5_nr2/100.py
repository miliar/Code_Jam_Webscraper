#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <numeric>
using namespace std;
typedef long long LL;

struct vert
{
	int y;
	int x;
	int by, bx, yy, yx; // connected
	vert(int y, int x, int by, int bx, int yy, int yx): y(y),x(x),by(by),bx(bx),yy(yy),yx(yx) {}
	bool operator<(const vert& v) const {
		if( y!=v.y ) return y<v.y;
		if( x!=v.x ) return x<v.x;
		if( by!=v.by ) return by<v.by;
		if( bx!=v.bx ) return bx<v.bx;
		if( yy!=v.yy ) return yy<v.yy;
		if( yx!=v.yx ) return yx<v.yx;
		return false;
	}
};


int dy[]={-1,0,1,0};
int dx[]={0,-1,0,1};
void shot(vector<string>& M, int& y, int& x, int d)
{
	for(int i=1 ;; ++i)
		if( M[y+dy[d]*i][x+dx[d]*i]=='#' )
		{
			y += dy[d]*(i-1);
			x += dx[d]*(i-1);
			return;
		}
}

int bfs(vector<string>& M, int sy, int sx, int gy, int gx)
{
	set<vert> visited;

	vector<vert> cand;
	int yy=sy, xx=sx;
	shot(M, yy, xx, 0);
	cand.push_back( vert(sy,sx,yy,xx,yy,xx) );

	for(int stp=0; !cand.empty(); ++stp)
	{
		vector<vert> cand2;
//cout << "---" << stp << "---" << endl;
		for(int i=0; i!=cand.size(); ++i)
		{
			vert v = cand[i];
			if( v.y==gy && v.x==gx )
				return stp;
			if( visited.count(v) )
				continue;
			visited.insert(v);
//cout << v.y << " " << v.x << endl;

			for(int bd=-1; bd<4; ++bd)
				for(int yd=-1; yd<4; ++yd)
				{
					vert vv = v;
					if( bd>=0 ) {
						int yy=vv.y, xx=vv.x;
						shot(M, yy, xx, bd);
						vv.by=yy;
						vv.bx=xx;
					}
					if( yd>=0 ) {
						int yy=vv.y, xx=vv.x;
						shot(M, yy, xx, yd);
						vv.yy=yy;
						vv.yx=xx;
					}

					// move
					if( vv.y==vv.by && vv.x==vv.bx ) {
						vert v2 = vv;
						v2.y = vv.yy;
						v2.x = vv.yx;
						if( !visited.count(v2) ) cand2.push_back(v2);
					}
					else if( vv.y==vv.yy && vv.x==vv.yx ) {
						vert v2 = vv;
						v2.y = vv.by;
						v2.x = vv.bx;
						if( !visited.count(v2) ) cand2.push_back(v2);
					}
					for(int d=0; d<4; ++d)
					{
						vert v2 = vv;
						v2.y = vv.y+dy[d];
						v2.x = vv.x+dx[d];
						if( M[v2.y][v2.x]!='#' ) {
							if( !visited.count(v2) ) cand2.push_back(v2);
						}
					}
				}
		}

		cand2.swap(cand);
	}

	return -1;
}

void solve( vector<string>& M )
{
	int sy, sx, gy, gx;
	for(int y=0; y!=M.size(); ++y)
		for(int x=0; x!=M[y].size(); ++x)
			if( M[y][x]=='O' )
			{
				sy = y;
				sx = x;
				M[y][x] = '.';
			}
			else if( M[y][x] == 'X' )
			{
				gy = y;
				gx = x;
				M[y][x] = '.';
			}

	int n = bfs(M, sy, sx, gy, gx);
	if( n < 0 )
		cout << "THE CAKE IS A LIE";
	else
		cout << n;
}



int main()
{
	int NUM_CASE; cin >> NUM_CASE;
	for(int caseID=1; caseID<=NUM_CASE; ++caseID)
	{
		int R, C;
		cin >> R >> C;
		vector<string> maze;
		string wall(C+2, '#');
		maze.push_back(wall);
		for(int y=0; y!=R; ++y) {
			string m;
			cin >> m;
			maze.push_back("#"+m+"#");
		}
		maze.push_back(wall);

		cout << "Case #" << caseID << ": ";
		solve(maze);
		cout << endl;
	}
}
