#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

int N,K;

char v[64][64];
char p[64][64];

#define DIR 4

int dx[DIR] = {1,0,-1,1};
int dy[DIR] = {0,1,1,1};

void rotate()
{
	forn(i,N)
	forn(j,N)
		p[i][j] = v[N-1-j][i];
	forn(j,N)
	{
		int i = N-1;
		dforn(k,N)
		if (p[k][j] != '.') p[i--][j] = p[k][j];
		while (i >= 0) p[i--][j] = '.';
	}
}

bool inRange(int x,int y)
{
	return  0 <= x && x < N &&
			0 <= y && y < N;
}

bool check(char c)
{
	forn(i,N)
	forn(j,N)
	forn(d,DIR)
	{
		int x = i, y = j;
		int res = 0;
		while (inRange(x,y) && p[x][y] == c)
		{
			res++;
			x += dx[d];
			y += dy[d];
		}
		if (res >= K)
			return true;
	}
	return false;
}

int main()
{
	stdin = freopen("a.in","r",stdin);
	stdout = freopen("a.out","w",stdout);
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
		
		cin >> N >> K;
		forn(i,N)
		forn(j,N)
			cin >> v[i][j];
		rotate();
		bool red = check('R');
		bool blue = check('B');
		string res;
		if (red && blue)
			res = "Both";
		else if (red)
			res = "Red";
		else if (blue)
			res = "Blue";
		else
			res = "Neither";
		cout << "Case #" << caso + 1 << ": " << res << endl;
		//cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}

