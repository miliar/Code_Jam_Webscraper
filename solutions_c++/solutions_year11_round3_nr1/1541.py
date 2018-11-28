#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }
char nc() { char a; scanf("%c", &a); return a; }
/*
typedef map<char,int> mci;

mci tmap;
tmap['O'] = 0;
tmap['B'] = 1;
*/
typedef map<char, int> mci;

mci tmap;

int check(vector<vector<int > > &vext, int i, int j)
{
	if (vext[i][j] == 1 && vext[i+1][j] == 1 && vext[i+1][j+1]== 1
		&& vext[i][j+1] == 1) return 1;
	return 0;
}
int clear(vector<vector<int > > &vext, int i, int j, vector< vector<char> > &ovec)
{
	vext[i][j] = 0;
	ovec[i][j] = '/';
	ovec[i+1][j] = '\\';
	ovec[i][j+1] = '\\';
	ovec[i+1][j+1] = '/';
	vext[i+1][j] = 0;
	vext[i][j+1] = 0;
	vext[i+1][j+1] = 0;
	return 0;

}


typedef pair<int,int> pos;

class mxit
{
	int sx, sy;
	int steps;
	int maxsteps;
	public:
	int x, y;
	int circle;
	int dir;
	mxit(int maxx, int maxy) : sx(maxx), sy(maxy)
	{
		x = 0;
		y = 0;
		steps = 0;
		maxsteps = (sx)*(sy);
		circle = 0;
		dir = 0;
	}
	bool finished()
	{
		if (steps>= maxsteps) return true;
		return false;
	}
	int go()
	{
		if (dir == 0) 
		{
			x++;
			if (x >= sx-circle)
			{
				x--;
				dir++;
			}
		}
		if (dir == 1) 
		{
			y++;
			if (y >= sy-circle)
			{
				y--;
				dir++;
			}
		}
		if (dir == 2) 
		{
			x--;
			if (x < 0 + circle)
			{
				x++;
				dir++;
			}
		}
		if (dir == 3)
		{
			y--;
			if (y < 1 + circle)
			{
				y++;
				x++;
				dir=0;
				circle++;
			}
		}
		steps++;

	}

}
;
int main()
{
	tmap['.'] = 0;
	tmap['#'] = 1;
	tmap['/'] = 2;
	tmap['\\'] = 3;
	int cases;
	cases = ni();
	int i,j,k,l,m;
	fi(cases)
	{
		int r = ni();
		int c = ni();
		vector<vector<int> > mx;
		vector<vector<char> > cx;
		mx.resize(r);
		cx.resize(r);
		fj(r) {
			string s= ns();
			mx[j].resize(c);
			cx[j].resize(c);
			fk(c) {
				mx[j][k] = tmap[ s[ k ] ];
				cx[j][k] = s[ k ];
			}
		}
		mxit mit(r-1,c-1);
		while (!mit.finished())
		{
			
			if (check(mx, mit.x, mit.y) == 1)
			{
				clear(mx,mit.x, mit.y, cx);
			}
			mit.go();
		}
		printf("Case #%d:\n",i+1);
		bool check = true;
		fj(r)
		fk(c) {
			if ( cx[j][k] == '#' )
			{
				check = false;
				printf("Impossible\n");
				goto nextone;
			}
		}
		nextone:
		if (check) 
		fj(r){ 
			fk(c)
			{
				printf("%c",cx[j][k]);
			}
			printf("\n");
		}
		
	}				
}
