#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define fprintf(...)
typedef long double ld;

int dr[] = { 0, 1, 0, -1 },
    dc[] = { 1, 0, -1, 0 };

int cas=0;
int R,C;
char grid[16][16];
int par[5];
int find(int i) {
  if (i != par[i]) return par[i] = find(par[i]);
  return i;
}
void join(int i, int j) {
  i = find(i); j = find(j);
  if (i==j) return;

  par[i] = j;
}
int nbox;
struct State {
  pair<int,int> pos[5];

  State() {
    FOR(i,5) pos[i] = MP(99,99);
  }
  void normize() {
    sort(&pos[0],&pos[5]);
  }
  bool safe() {
    FOR(i,nbox) par[i] = i;

    FOR(i,nbox) FR(j,i+1,nbox) {
      int r1 = pos[i].A, c1 = pos[i].B, r2 = pos[j].A, c2 = pos[j].B;
      if (abs(r1-r2)+abs(c1-c2)==1) join(i,j);
    }

    FOR(i,nbox) if (find(i) != find(0)) return 0;
    return 1;
  }
};
bool thebox[16][16];
bool haswall(int r, int c) {
  if (r<0||r>=R||c<0||c>=C) return 1;
  return grid[r][c] == '#';
}
bool hasbox(int r, int c) {
  if (r<0||r>=R||c<0||c>=C) return 0;
  return thebox[r][c];
}
bool hasempty(int r, int c) {
  return !haswall(r,c) && !hasbox(r,c);
}
int ninit,ngoal;
set<State> mark;
State init;
State goal;
bool operator<(const State &s, const State &t) {
  FOR(i,nbox) {
    if (s.pos[i] != t.pos[i]) return s.pos[i] < t.pos[i];
  }
  return 0;
}
void dump() {
  FOR(r,R) {
    FOR(c,C) {
      char ch = grid[r][c];
      if (ch=='o') ch='.';
      if (ch=='w') ch='x';
      if (hasbox(r,c)) {
	if (ch=='x') ch = 'w';
	else ch = 'o';
      }
      fprintf(stderr, "%c",ch);
    }
    fprintf(stderr,"\n");
  }
  fprintf(stderr,"\n");
}
void doit() {
  CLR(thebox,0);
  scanf("%d%d",&R,&C);
  
  FOR(r,R) {
    scanf(" %[^\n]",grid[r]);
  }

  init = State(); goal = State();
  ninit=ngoal=0;
  FOR(r,R) FOR(c,C) {
    if (grid[r][c] == 'x' || grid[r][c] == 'w') {
      goal.pos[ngoal++] = MP(r,c);
    }
    if (grid[r][c] == 'o' || grid[r][c] == 'w') {
      init.pos[ninit++] = MP(r,c);
    }
  }
  init.normize();
  goal.normize();
  assert(ninit == ngoal);
  nbox = ninit;

  mark.clear();

  int t = 0;
  deque<State> q,q2;
  q.PB(init);
  mark.insert(init);
  while (q.size()) {
    fprintf(stderr,"t = %d\n",t);
    while (q.size()) {
      State now = q.front(); q.pop_front();
      
      bool weredone = 1;
      FOR(i,nbox) if (now.pos[i] != goal.pos[i]) weredone = 0;
      if (weredone) goto done;

      FOR(i,nbox) {
	int r = now.pos[i].A, c = now.pos[i].B;
	thebox[r][c] = 1;
      }
      /*
      dump();
      int zzzzz=0;
      FOR(r,R) FOR(c,C) zzzzz+=hasbox(r,c);
      assert(zzzzz==nbox);*/

      FOR(i,nbox) {
	int r = now.pos[i].A, c = now.pos[i].B;
	fprintf(stderr, "  trying box at (%d, %d)\n",r,c);

	FOR(k,4) {
	  int k2 = (k+2)%4;
	  if (hasempty(r+dr[k],c+dc[k]) && hasempty(r+dr[k2],c+dc[k2])) {
	    State next = now;

	    next.pos[i] = MP(r+dr[k],c+dc[k]);
	    next.normize();

	    if ((now.safe() || next.safe()) && !mark.count(next)) {
	      fprintf(stderr, "  pushed q2\n");
	      mark.insert(next);
	      q2.PB(next);
	    }
	  }
	}
      }

      FOR(i,nbox) {
	int r = now.pos[i].A, c = now.pos[i].B;
	thebox[r][c] = 0;
      }
    }
    swap(q,q2);
    ++t;
  }

  t=-1;
  done:;
  printf("Case #%d: %d\n",++cas,t);
}

int zzzz;
int main() {
  scanf("%d ",&zzzz);
  FOR(i,zzzz) doit();
}
