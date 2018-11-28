#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

#define MAX_H 100
#define MAX_W 100

#define INFTY  20000

typedef pair<int,int> int_pair;

vector<int_pair> children[MAX_H][MAX_W];
int_pair parent[MAX_H][MAX_W];

int h,w;
int e[MAX_H][MAX_W];

int group[MAX_W][MAX_W];

void read_input()
{
  scanf("%d %d",&h, &w);
  for(int i=0; i<h; i++)
    for(int j=0; j<w; j++)
      scanf("%d", &e[i][j]);
}

void clear_children()
{
  for(int i=0; i<h; i++)
    for(int j=0; j<w; j++)
      children[i][j].clear();
}

void find_parent(int r, int c, int& pr, int& pc)
{
  pr = pc = -1;
  int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

  int min_at = INFTY;
  for(int d=0; d<4; d++) {
    int nr = r + dir[d][0];
    int nc = c + dir[d][1];
    if((nr >= 0) && (nr < h) && 
       (nc >= 0) && (nc < w) && 
       ((e[nr][nc] < e[r][c]) && (e[nr][nc] < min_at))) {
      min_at = e[nr][nc];
      pr = nr;
      pc = nc;
    }
  }
}

void build_children_map()
{
  clear_children();
  for(int r=0; r<h; r++) {
    for(int c=0; c<w; c++) {
      int pr, pc;
      find_parent(r,c,pr,pc);
      //printf("(%2d,%2d) ",pr,pc);
      if(pr!=-1) {
	children[pr][pc].push_back(int_pair(r,c));
	parent[r][c] = int_pair(pr,pc);
      } else {
	parent[r][c] = int_pair(-1,-1);
      }
    }
    //printf("\n");
  }
}

void init_group()
{
  for(int r=0; r<h; r++)
    for(int c=0; c<w; c++)
      group[r][c] = -1;
}

void dfs(int r, int c, int g)
{
  group[r][c] = g;
  for(vector<int_pair>::iterator i = children[r][c].begin();
      i != children[r][c].end(); i++)
    dfs(i->first, i->second, g);
}

void build_group()
{
  int g = 0;
  for(int r=0; r<h; r++)
    for(int c=0; c<w; c++)
      if(group[r][c]==-1) {
	// find root
	int pr = r;
	int pc = c;
	while(parent[pr][pc].first!=-1) {
	  int npr = parent[pr][pc].first;
	  int npc = parent[pr][pc].second;
	  pr = npr;
	  pc = npc;
	}
	dfs(pr,pc,g);
	g++;
      }
  if(g>26)
    fprintf(stderr,"BAD!\n");
}

void print_group()
{
  for(int r=0; r<h; r++) {
    for(int c=0; c<w; c++)
      printf("%c ", group[r][c]+'a');
    printf("\n");
  }
}

main()
{
  int T;

  scanf("%d",&T);
  for(int t=0; t<T; t++) {
    read_input();
    build_children_map();
    init_group();
    build_group();
    printf("Case #%d:\n",t+1);
    print_group();
    //printf("----------------\n");
  }
}
