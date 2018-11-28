#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

map<int, int> positions[6];
int cnt[6];
int masks[6][100000];
bool dang[6][100000];

bool used[6][6];

void dfs(int x, int y, int mask, int N){
	used[x][y] = true;
	FOR(nx,x-1,x+2)
		FOR(ny,y-1,y+2)
			if (nx >= 0 && ny >= 0 && nx < N && ny < N && (mask & (1<<(N*nx+ny))) > 0 && !used[nx][ny])
				dfs(nx,ny,mask,N);
}

bool check(int mask, int N){
	bool fl = false;
	REP(i,N)
		if (mask & (1<<i)) fl = true;
	if (!fl)
		return false;
	fl = false;
	REP(i,N)
		if (mask & (1<<(i*N))) fl = true;
	if (!fl)
		return false;
	FILL(used);
	REP(i,N)
		REP(j,N){
			if (mask & (1<<(i*N+j))){
				dfs(i, j, mask, N);
				REP(x,N)
					REP(y,N)
						if (mask & (1<<(x*N+y))) if (!used[x][y])
							return false;
				int badcnt = 0;
				REP(x,N)
					REP(y,N)
					if (mask & (1<<(x*N+y))){
						bool curf = false;
						REP(dir,4){
							int nx = x + dx[dir], ny = y + dy[dir];
							if (nx >= 0 && ny >= 0 && nx < N && ny < N){
								if (mask & (1<<(nx*N+ny)))
									curf = true;
							}
						}
						if (!curf)
							++badcnt;
					}
				if (badcnt && N > 1)
					dang[N][cnt[N]] = true;
				return true;
			}
	}
}

void genpos(int x, int y, int left, int mask, int N){
	if (x == N){
		if (left == 0 && check(mask, N)){
			positions[N][mask] = cnt[N];
			masks[N][cnt[N]] = mask;
			++cnt[N];
		}
		return;
	}
	if (left){
		if (y+1 == N)
			genpos(x+1, 0, left - 1, mask + (1<<(N*x+y)), N);
		else
			genpos(x, y+1, left - 1, mask + (1<<(N*x+y)), N);
	}
	if (y+1 == N)
		genpos(x+1, 0, left, mask, N);
	else
		genpos(x, y+1, left, mask, N);
}

struct posit{
	int num, x, y;
	posit(int num, int x, int y):num(num), x(x), y(y) {}
};

int n, m;
string s[12];
queue<posit> q;
int d[1000][12][12];
bool have[12][12];

bool isgood(int x, int y){
	return x >= 0 && y >= 0 && x < n && y < m && s[x][y] != '#';
}

posit gen(int box){
	int minx = 20, miny = 20;
	REP(i,n)
		REP(j,m)
			if (have[i][j]){
				minx = min(minx,i);
				miny = min(miny,j);
			}
	int mask = 0;
	REP(i,n)
		REP(j,m)
			if (have[i][j])
				mask += 1<<(box*(i-minx)+(j-miny));
	if (positions[box].find(mask) == positions[box].end())
		return posit(-1,-1,-1);
	return posit(positions[box][mask], minx, miny);
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	FILL(cnt); FILL(dang);
	FOR(i,1,6)
		genpos(0, 0, i, 0, i);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		memset(d,-1,sizeof(d));
		printf("Case #%d: ", it+1);
		scanf("%d%d", &n, &m);
		getline(cin, s[0]);
		REP(i,n)
			getline(cin, s[i]);
		int box = 0;
		int minx = 20, miny = 20;
		REP(i,n)
			REP(j,m)
				if (s[i][j] == 'o' || s[i][j] == 'w'){
					minx = min(minx, i);
					miny = min(miny, j);
					++box;
				}
		int ma = 0;
		REP(i,n)
			REP(j,m)
				if (s[i][j] == 'o' || s[i][j] == 'w'){
					ma += 1<<((i-minx)*box + (j-miny));
				}
		q.push(posit(positions[box][ma], minx, miny));
		d[positions[box][ma]][minx][miny] = 0;
		while (!q.empty()){
			posit cur = q.front();
			q.pop();
			int curd = d[cur.num][cur.x][cur.y];
			bool curdang = dang[box][cur.num];
			int curmask = masks[box][cur.num];
			FILL(have);
			REP(i,box){
				REP(j,box){
					if (curmask & (1<<(i*box + j))){
						have[i + cur.x][j + cur.y] = true;
					}
				}
			}
			REP(i,n){
				REP(j,m){
					if (have[i][j]){
						REP(dir,4){
							int nx = i + dx[dir], ny = j + dy[dir];
							int ox = i + dx[(dir+2)%4], oy = j + dy[(dir+2)%4];
							//cerr << have[nx][ny] << " " << have[ox][oy] << endl;
							if (isgood(nx, ny) && isgood(ox, oy) && !have[nx][ny] && !have[ox][oy]){
								swap(have[i][j], have[nx][ny]);
								posit npos = gen(box);
								if (npos.num == -1){
									swap(have[i][j], have[nx][ny]);
									continue;
								}
								if (curdang && dang[box][npos.num]){
									swap(have[i][j], have[nx][ny]);
									continue;
								}
								if (d[npos.num][npos.x][npos.y] == -1){
									d[npos.num][npos.x][npos.y] = curd + 1;
									q.push(npos);
								}
								swap(have[i][j], have[nx][ny]);
							}
						}
					}
				}
			}
		}
		minx = 20; miny = 20;
		REP(i,n)
			REP(j,m)
				if (s[i][j] == 'x' || s[i][j] == 'w'){
					minx = min(minx, i);
					miny = min(miny, j);
				}
		ma = 0;
		REP(i,n)
			REP(j,m)
				if (s[i][j] == 'x' || s[i][j] == 'w'){
					ma += 1<<((i-minx)*box + (j-miny));
				}
		cout << d[positions[box][ma]][minx][miny] << "\n";
	}
}
