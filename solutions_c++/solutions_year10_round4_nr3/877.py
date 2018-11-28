#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "set"
#include "map"
#include "iostream"
#include "sstream"
#include "queue"
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define MP				make_pair
#define CCQ(que)			while(!que.empty()) que.pop();
#define CC(m,what)			memset(m,what,sizeof(m))
#define FS(i,a)				for( int i = 0 ; a[i] ; i ++ )
#define FF(i,a)				for( int i = 0 ; i < a ; i ++ )
#define FOR(i,a,b)			for( int i = a ; i < b ; i ++ )
#define PP(n,m,a)			puts("---");FF(i,n){FF(j,m)cout << a[i][j] << ' ';puts("");}
const double Pi = acos(-1.0);
void read(char *a)		{	freopen(a,"r",stdin);	}
void write(char *a)		{	freopen(a,"w",stdout);	}
template<class T> inline void checkmin(T &a,T b)	{if(a < 0 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)	{if(a < b)	a = b;}
template<class T> inline int fix(T x,const int p)	{if((x%=p) >= 0) return x;return x + p;}
int dx[] = {-1,0,1,0,1,1,-1,-1};//up Right down Left
int dy[] = {0,1,0,-1,1,-1,1,-1};
//-----------------------------------------------------------------

struct H{
	int x1,x2,y1,y2;
}hh[1001];
vector <int> edge[1001];
int X1,X2,Y1,Y2;
int hash[1001];


bool Insert(int a,int x,int y) {
	if(hh[a].x1 <= x && x <= hh[a].x2 && hh[a].y1 <= y && y <= hh[a].y2) return true;
	return false;
}
bool yes(int a,int b) {
	if(hh[a].x1 == hh[b].x1 && hh[a].x2 == hh[b].x2 && hh[a].y1 == hh[b].y1 && hh[a].y2 == hh[b].y2) {
		return true;
	}
	hh[a].x1 --;
	hh[a].y1 --;
	hh[a].x2 ++;
	hh[a].y2 ++;
	if(Insert(a,hh[b].x1,hh[b].y1)) goto loop;
	if(Insert(a,hh[b].x1,hh[b].y2)) goto loop;
	if(Insert(a,hh[b].x2,hh[b].y1)) goto loop;
	if(Insert(a,hh[b].x2,hh[b].y2)) goto loop;
	hh[a].x1 ++;
	hh[a].y1 ++;
	hh[a].x2 --;
	hh[a].y2 --;
	return false;
loop:
	hh[a].x1 ++;
	hh[a].y1 ++;
	hh[a].x2 --;
	hh[a].y2 --;
	return true;
}


int cnt;
void dfs(int u) {
	if(hash[u] != -1) return ;
	hash[u] = cnt;
	checkmin(X1 , hh[u].x1);
	checkmin(Y1 , hh[u].y1);
	checkmax(X2 , hh[u].x2);
	checkmax(Y2 , hh[u].y2);
	for (int i = 0 ; i < edge[u].size() ; i ++) {
		dfs(edge[u][i]);
	}
}
bool maze[111][111];
void solved(int n) {
	memset(maze,false,sizeof(maze));
	int cnt = 0;
	for (int i = 0 ; i < n ; i ++) {
		for (int x = hh[i].x1 ; x <= hh[i].x2 ; x ++) {
			for (int y = hh[i].y1 ; y <= hh[i].y2 ; y ++) {
				if(maze[x][y] == false) {
					maze[x][y] = true;
					cnt ++;
				}
			}
		}
	}
	int ret = 0;
	while(cnt) {
		ret ++;
		for (int i = 100 ; i >= 1 ; i --) {
			for (int j = 100 ; j >= 1 ; j --) {
				if(maze[i-1][j] && maze[i][j-1] && !maze[i][j]) {
					maze[i][j] = true;
					cnt ++;
				}
			}
		}
		for (int i = 100 ; i >= 1 ; i --) {
			for (int j = 100 ; j >= 1 ; j --) {
				if(!maze[i-1][j] && !maze[i][j-1] && maze[i][j]) {
					maze[i][j] = false;
					cnt --;
				}
			}
		}
	}
	printf("%d\n",ret);
}
int main() {
	read("C-small-attempt1.in");
	write("C-small-attempt1.out");
	int T;
	scanf("%d",&T);
	int cas = 1;
	while(T --) {
		int n;
		scanf("%d",&n);
		for (int i = 0 ; i < n ; i ++) {
			scanf("%d%d%d%d",&hh[i].x1,&hh[i].y1,&hh[i].x2,&hh[i].y2);
		}

		printf("Case #%d: ",cas++);
		solved(n);
		continue;


		for (int i = 0 ; i < n ; i ++) {
			edge[i].clear();
			for (int j = 0; j < n ; j ++) {
				if(yes(i,j) || yes(j,i)) {
					edge[i].push_back(j);
				}
			}
		}
		CC(hash,-1);
		int ret = 0;
		cnt = 0;
		for (int i = 0 ; i < n ; i ++) {
			if(hash[i] != -1) continue;
			X1 = hh[i].x1;
			X2 = hh[i].x2;
			Y1 = hh[i].y1;
			Y2 = hh[i].y2;
			dfs(i);
			for (int j = 0 ; j < n ; j ++) {
				if(hash[j] == cnt) {
					checkmax(ret , X2 - hh[j].x1 + Y2 - hh[j].y2 + 1);
				}
			}
		}
		printf("Case #%d: %d\n",cas++,ret);
	}
	return 0;
}