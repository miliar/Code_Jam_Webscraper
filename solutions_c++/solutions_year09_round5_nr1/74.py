#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

#define MAX 16

#define POW2(a) ((1) << (a))
#define BIT(a, b) (((a) >> (b)) & (1))

const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, 1, 0, -1 };

void input(void);
void solve(void);

void relax(vector <pair <int, int> > vp, int d);

int bfs(void);
int connected(vector <pair <int, int> > &vp);
int dfs(int x, int &set, vector <pair <int, int> > &vp);

void print_it(vector <pair <int, int> > &vp);

int n, m;
char tmp[MAX][MAX];
char grid[MAX][MAX];
vector <pair <int, int> > start;
vector <pair <int, int> > finish;
queue <vector <pair <int, int> > > que;
map <vector <pair <int, int> >, int> dist;
int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  scanf("%d %d", &n, &m);
  for(int i = 0; i < n; i++) scanf(" %s", &tmp[i][0]);
  
  start.clear();
  finish.clear();
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++) {
      if(tmp[i][j] == 'o' || tmp[i][j] == 'w') start.push_back(make_pair(i, j));
      if(tmp[i][j] == 'x' || tmp[i][j] == 'w') finish.push_back(make_pair(i, j));
    }
    
  sort(start.begin(), start.end());
  sort(finish.begin(), finish.end());
}

void solve(void)
{
  printf("Case #%d: %d\n", case_cnt++, bfs());
}

int bfs(void)
{
  dist.clear();
  while(!que.empty()) que.pop();
  relax(start, 0);
  
  while(!que.empty()) {
    vector <pair <int, int> > cur = que.front(); que.pop();
    //print_it(cur);
    if(cur == finish) return dist[cur];
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) {
        if(tmp[i][j] == '#') grid[i][j] = '#';
        else grid[i][j] = '.';
      }
    }
    for(int i = 0; i < cur.size(); i++) grid[cur[i].first][cur[i].second] = '#';
    /*
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) printf("%c", grid[i][j]);
      printf("\n");
    }
    */
    
    for(int d = 0; d < 4; d++) {
      for(int i = 0; i < cur.size(); i++) {
        int x1 = cur[i].first  + dx[d];
        int y1 = cur[i].second + dy[d];
        int x2 = cur[i].first  - dx[d];
        int y2 = cur[i].second - dy[d];
        if(x1 < 0 || x1 >= n || y1 < 0 || y1 >= m) continue;
        if(x2 < 0 || x2 >= n || y2 < 0 || y2 >= m) continue;
        if(grid[x1][y1] != '.') continue;
        if(grid[x2][y2] != '.') continue;
        vector <pair <int, int> > tmp = cur;
        tmp[i] = make_pair(x1, y1);
        sort(tmp.begin(), tmp.end());
        if(!connected(tmp) && !connected(cur)) continue;
        relax(tmp, dist[cur] + 1);
      }
    }
  }
  
  return -1;
}

void relax(vector <pair <int, int> > vp, int d)
{
  if(!dist.count(vp)) {
    dist[vp] = d;
    que.push(vp);
  }
}

int connected(vector <pair <int, int> > &vp)
{
  int set = 0;
  if(dfs(0, set, vp) == vp.size()) return 1;
  else return 0;
}

int dfs(int x, int &set, vector <pair <int, int> > &vp)
{
  set |= POW2(x);
  
  int res = 1;
  for(int i = 0; i < vp.size(); i++) {
    if(BIT(set, i)) continue;
    if(abs(vp[x].first  - vp[i].first) +  abs(vp[x].second - vp[i].second) == 1) {
      res += dfs(i, set, vp);
    }
  }
  
  return res;
}
  
void print_it(vector <pair <int, int> > &vp)
{
  printf("\n");
  printf("connected = %d\n", connected(vp));
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      if(tmp[i][j] == '#') printf("#");
      else if(find(vp.begin(), vp.end(), make_pair(i, j)) != vp.end()) printf("X");
      else printf(".");
    }
    printf("\n");
  }
}
