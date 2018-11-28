#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define MAX 2010

int N, M;
int U[MAX], V[MAX];

vector<int> sus[MAX];
int visited[MAX][MAX];
vector<vector<int> > rooms;

int next(int a, int b) {
  int susid = (a - b + N) % N;
  vector<int>::iterator it = lower_bound(sus[b].begin(), sus[b].end(), susid);
  --it;
  return (b + *it) % N;
}

void visit(int a, int b) {
  if(a == (b+1)%N) return;
  if(visited[a][b]) return;
  visited[a][b] = 1;
  //printf("visited %d %d\n", a+1, b+1);
  int roomid = rooms.size();
  rooms.resize(rooms.size() + 1);
  rooms[roomid].push_back(a);
  rooms[roomid].push_back(b);
  int origa = a;   // Origa FTW
  while(1) {
    int nextb = next(a, b);
    a = b; b = nextb;
    visited[a][b] = 1;
    if(b == origa) break;
    //printf("visited %d %d\n", a+1, b+1);
    rooms[roomid].push_back(b);
  }
//  printf("room %d:", roomid); for(int i = 0; i < rooms[roomid].size(); i++) printf(" %d", rooms[roomid][i]+1); printf("\n");
}

int res[MAX];
bool isok(int F) {
  bool roomhave[MAX];
  for(int i = 0; i < rooms.size(); i++) {
    for(int j = 0; j < F; j++) roomhave[j] = 0;
    for(int j = 0; j < rooms[i].size(); j++) roomhave[res[rooms[i][j]]] = 1;
    for(int j = 0; j < F; j++) if(roomhave[j] == 0) return false;
  }
  return true;
}
bool skusrec(int F, int nn) {
  if(nn == N) {
    return isok(F);
  }
  for(int i = 0; i < F; i++) {
    res[nn] = i;
    if(skusrec(F, nn+1)) return true;
  }
  return false;
}
bool skus(int F) {
  return skusrec(F, 0);
}

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    for(int i = 0; i < MAX; i++) {
      sus[i].clear();
      rooms.clear();
      U[i] = V[i] = 0;
      for(int j = 0; j < MAX; j++) visited[i][j] = 0;
    }

    scanf("%d%d", &N, &M);
    for(int i = 0; i < M; i++) scanf("%d", &U[i]);
    for(int i = 0; i < M; i++) scanf("%d", &V[i]);
    for(int i = 0; i < M; i++) {
      U[i]--;
      V[i]--;
      sus[U[i]].push_back((V[i]-U[i]+N+N)%N);
      sus[V[i]].push_back((U[i]-V[i]+N+N)%N);
    }
    for(int i = 0; i < N; i++) {
      sus[i].push_back(1);
      sus[i].push_back(N-1);
      sort(sus[i].begin(), sus[i].end());
      //printf("sus %d:", i+1); for(int j = 0; j < sus[i].size(); j++) printf(" %d", sus[i][j]); printf("\n");
    }
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < sus[i].size(); j++)
        visit(i, (i+sus[i][j])%N);
    }
    int low = 1, high = N;
    // <=low does work, >high doesn't work
    while(low != high) {
      int mid = (low+high+1)/2;
      if(skus(mid))
        low = mid;
      else
        high = mid-1;
    }
    skus(low);
    printf("Case #%d: %d\n", t, low);
    for(int i = 0; i < N; i++) printf("%d%c", res[i]+1, i == N-1 ? '\n' : ' ');
  }
  return 0;
}

