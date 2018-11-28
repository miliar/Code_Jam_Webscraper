#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
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
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
int N, M, K;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
#define MAX 111
int a[MAX][MAX];
int lab[MAX][MAX];
char ch[MAX][MAX];
inline bool isOk(int i, int j)  { return i>=0 && i<N && j>=0 && j<M; }
bool vis[MAX][MAX];

inline bool isBest(int y, int x, int i, int j)
{
	int bst = inf;
	pii bstII = mp(-1,-1);
	FOR(k,0,4)
	{
		int ny = y + dy[k];
		int nx = x + dx[k];
		if (isOk(ny,nx) && a[ny][nx] < a[y][x] && a[ny][nx] < bst)
		{
			bst = a[ny][nx];
			bstII = mp(ny,nx);
		}
	}
	return bstII == mp(i,j);
}
int dfs(int i, int j, int l)
{
	vis[i][j] = true;
	lab[i][j] = l;
	int r = 1;
	FOR(k,0,4)
	{
		int nx = j+dx[k];
		int ny = i+dy[k];
		if (!isOk(ny,nx)) continue;
		if (vis[ny][nx]) continue;

		if (isBest(ny,nx,i,j))
		{
			r += dfs(ny, nx, l);
		}
	}
	return r;
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d: ", Case+1);
		fprintf(stderr, "Case #%d: ", Case+1);

		priority_queue<pair<int, pii> > q;
		scanf("%d%d", &N, &M);
		FOR(i,0,N)
			FOR(j,0,M)
		{
			scanf("%d", &a[i][j]);
			q.push(mp(-a[i][j], mp(i,j)));
		}

		int curLab = 0;
		fill(vis,0);
		fill(lab,-1);
		fill(ch,'0');

		int cnt=0;
		while (!q.empty())
		{
			int h = q.top().X;
			int ii = q.top().Y.X;
			int jj = q.top().Y.Y;
			q.pop();
			if (vis[ii][jj]) continue;
			cnt += dfs(ii,jj,curLab);
			++curLab;
		}
		if (cnt != N*M) throw -1;

		char curLabCh = 'a';
		FOR(i,0,N)
			FOR(j,0,M)
		{
			if (ch[i][j] == '0')
			{
				int cur = lab[i][j];
				FOR(ii,0,N)
					FOR(jj,0,M)
				{
					if (lab[ii][jj] == cur)
					{
						ch[ii][jj] = curLabCh;
					}
				}
				++curLabCh;
			}
		}

		printf("\n");
		fprintf(stderr, "\n");
		FOR(i,0,N)
		{
			FOR(j,0,M)
			{
				printf("%c ", ch[i][j]);
				fprintf(stderr, "%c ", ch[i][j]);
			}
			printf("\n");
			fprintf(stderr, "\n");
		}
		fflush(stderr);
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
