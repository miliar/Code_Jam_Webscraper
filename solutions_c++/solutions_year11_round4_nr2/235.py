//#pragma comment(linker, "/stack:1000000")

#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-4
#define Pi 3.14159265358979
#define FILL(a,v) memset(a,v,sizeof(a))

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PII;

#define SZ 600

int f[SZ][SZ];

struct BIT
{
	Long tree[SZ];

	BIT()
	{
		FILL(tree, 0);
	}

	Long read(int idx)
	{
		Long sum = 0;
		while (idx > 0){
			sum += tree[idx];
			idx -= (idx & -idx);
		}
		return sum;
	}
	void update(int idx ,int val)
	{
		while (idx < SZ){
			tree[idx] += val;
			idx += (idx & -idx);
		}
	}
	Long read(int l, int r)
	{
		return read(r)-read(l-1);
	}


};

struct bit2d
{
	BIT t[SZ];
	Long a[SZ][SZ];

	void update(int x , int y , int val)
	{
		while (x <= SZ){
			t[x].update(y,val);
			// this function should update array tree[x] 
			x += (x & -x); 
		}
	}

	Long read(int x, int y)
	{
		Long sum = 0;
		while (x > 0){
			sum += t[x].read(y);
			x -= (x & -x);
		}
		return sum;
	}

	void prepare()
	{
		REP(i,SZ)
			REP(j,SZ)
				a[i][j] = read(i,j);
	}

	Long read(int x1, int y1, int x2, int y2)
	{
		return (a[x2][y2] - a[x1-1][y2] - a[x2][y1-1] + a[x1-1][y1-1]);
	}
	void clear()
	{
		FILL(t,0);
	}
};

bit2d sx,sy,sm;

#define DEQ(a,b) (abs(a-b)<EPS)

bool chk(int x, int y, int k)
{
	++x;
	++y;
	int x1 = x + k-1;
	int y1 = y + k-1;
	Long resx = sx.read(x,y,x1,y1);	
	Long resy = sy.read(x,y,x1,y1);
	double resm = sm.read(x,y,x1,y1);

	--x;	--y;	--x1;	--y1;

	resx -= (f[x][y]*x + f[x][y1]*x + f[x1][y] * x1 + f[x1][y1]*x1);
	resy -= (f[x][y]*y + f[x][y1]*y1 + f[x1][y] * y + f[x1][y1]*y1);
	resm -= (f[x][y] + f[x][y1] + f[x1][y] + f[x1][y1]);


	double dx = resx/resm;
	double dy = resy/resm;

	double tx = x+(k-1)*0.5;
	double ty = y+(k-1)*0.5;
	return (DEQ(dx,tx)&&DEQ(dy,ty));
}

int r,c;
void sol(int T)
{
	sx.clear();
	sy.clear();
	sm.clear();
	int d;
	cin>>r>>c>>d;
	string s;
	REP(i,r)
	{
		cin>>s;
		REP(j,c)
		{
			f[i][j] = (d+(s[j] - '0'));
			sx.update(i+1,j+1, f[i][j]*i);
			sy.update(i+1,j+1, f[i][j]*j);
			sm.update(i+1,j+1, f[i][j]  );
		}
	}
	cout<<"Case #"<<T<<": ";
	sx.prepare();
	sy.prepare();
	sm.prepare();
	for(int i = max(r,c); i>=3; --i)
		RREP(x,r-i+1)
			RREP(y,c-i+1)
				if(chk(x,y,i))
				{
					cout<<i<<endl;
					return;
				}
	cout<<"IMPOSSIBLE"<<endl;
}

int main(int argc, char** argv)
{
	int T;
	cin>>T;
	REP(i,T)
		sol(i+1);
	return 0;
}