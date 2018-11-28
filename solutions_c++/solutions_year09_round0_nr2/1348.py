#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

int h,w;
vector<int> g[10010];
int c[10010];
int t[111][111];

int px[4] = {0,1,0,-1}, py[4] = {1,0,-1,0};

pair<int, pair<int,int> > get(int x, int y)
{
	if(x<0||y<0||x>=h||y>=w) return mp(1111111, mp(x,y));
	return mp(t[x][y], mp(x,y));
}

void go(int u, int col)
{
	c[u] = col;
	fort(i,g[u]) if(c[*i] == -1) go(*i, col);
}

void test()
{
	scanf("%d%d", &h, &w);
	fore(i,h) fore(j,w)
	{
		c[i*w+j] = -1;
		g[i*w+j].clear();
	}
	fore(i,h) fore(j,w) scanf("%d", &t[i][j]);
	fore(i,h) fore(j,w)
	{
		pair<int, pair<int,int> > k[4];
		fore(q,4) k[q] = get(i+px[q], j+py[q]);
		sort(k,k+4);
		if(k[0].x < t[i][j])
		{
			g[i*w+j].pb(k[0].y.x*w+k[0].y.y);
			g[k[0].y.x*w+k[0].y.y].pb(i*w+j);
		}
	}
	int q = 0;
	fore(i,h) fore(j,w) if(c[i*w+j] == -1) go(i*w+j,q++);
	fore(i,h)
	{
		fore(j,w) printf("%c ", 'a'+c[i*w+j]);
		printf("\n");
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d:\n", tt);
		test();
	}
}
