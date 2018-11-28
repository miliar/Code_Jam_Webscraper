#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z)	for(int x = (y); x < (z); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int grid[110][110], h, w;

void read() {
	scanf("%d %d",&h,&w);
	fr(i,0,h) {
		fr(j,0,w) {
			scanf("%d",&grid[i][j]);
		}
	}
}

// North, West, East, South
int mx[]={-1,+0,+0,+1};
int my[]={+0,-1,+1,+0};
#define val(x,y) (0 <= x && x < h) && (0 <= y && y < w)
char base;
char mark[110][110];

char busca(int x, int y) {
	
	if(mark[x][y]) return mark[x][y];
	
	int eita = inf, dir = -1;
	int nx, ny;
	fr(i,0,4) {
		nx = x + mx[i];
		ny = y + my[i];
		if(val(nx,ny)) {
			if(grid[nx][ny] < grid[x][y] && grid[nx][ny] < eita) {
				eita = grid[nx][ny];
				dir = i;
			}
		}
	}
	
	if(eita != inf) return (mark[x][y] = busca(x+mx[dir],y+my[dir]));
	else return (mark[x][y] = base++);
}

int casos = 1;
void process() {
	memset(mark,0,sizeof(mark));
	base = 'a';
		
	printf("Case #%d:\n",casos++);
	fr(i,0,h) {
		fr(j,0,w) {
			if(j) printf(" ");
			printf("%c",busca(i,j));
		}
		printf("\n");
	}
}

int main() {

	//freopen("B-small-attempt3.in","r",stdin);
	//freopen("B-small-attempt3.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	while(t--) {
		read();
		process();
	}
	
	return 0;
	
}
