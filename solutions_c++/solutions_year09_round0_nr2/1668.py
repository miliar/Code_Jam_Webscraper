#include<stdio.h>
#include<queue>

#define X (x+dx[k])
#define Y (y+dy[k])

#define MAXN 128

using namespace std;

int ar[MAXN][MAXN] = {};
int vis[MAXN][MAXN] = {};
char ch[MAXN][MAXN] = {};
int N,M;

int dx[6] = {-1,0,0,1};
int dy[6] = {0,-1,1,0};

int ok (int x,int y) {
    if (x < 0 || y < 0 || x >= N || y >= M) return 0;
    if (vis[x][y] != 0) return 0;
    return 1;
}
int ok1 (int x,int y) {
    if (x < 0 || y < 0 || x >= N || y >= M) return 0;
    return 1;
}


pair<int,int> sink (int x,int y) {
              int minn = INT_MAX;
              int minx = -1;
              int miny = -1;
              
              for (int k=0; k<4; k++) {
                  if (ok1(X,Y) && minn > ar[X][Y] && ar[X][Y] < ar[x][y]) {
                     minn = ar[X][Y];
                     minx = X;
                     miny = Y;
                  }
              }
              return make_pair(minx,miny);
}

int run (int x,int y, int mark) {
    queue<pair<int,int> > q;
    q.push(make_pair(x,y));
    vis[x][y] = mark;

    while (!q.empty()) {
          pair<int,int> p = q.front();
          q.pop();
          x = p.first;
          y = p.second;
          for (int k=0; k<4; k++) {
              if (ok(X,Y) && sink(X,Y) == p) {
                 vis[X][Y] = mark;
                 q.push(make_pair(X,Y));
              }
          }
    }
    return 0;
}


pair<int,int> find () {
              int minn = INT_MAX;
              int minx = -1;
              int miny = -1;
              for (int i=0; i<N; i++) {
                  for (int j=0; j<M; j++) {
                      if (vis[i][j] != 0) continue;
                      if (ar[i][j] < minn) {
                         minn = ar[i][j];
                         minx = i;
                         miny = j;
                      }
                  }
              }
              return make_pair(minx,miny);
}


int mark (int w, char l) {
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (vis[i][j] == w) ch[i][j] = l;
        }
    }
    return 0;
}

int solve () {
    
    int t = 1;
    while (1) {
          pair<int,int> p = find();
          if (p.first == -1) break;
          run(p.first,p.second,t++);
    }
    char l = 'a';
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (ch[i][j] == 0) {
               mark(vis[i][j], l++);
            }
        }
    }
    return 0;
}



int main () {
    freopen("bbbb.in","r",stdin);
    freopen("bbbb.out","w",stdout);


    int T;
    scanf("%d\n",&T);

    for (int t=1; t<=T; t++) {
    memset(ar,0,sizeof(ar));
    memset(vis,0,sizeof(vis));
    memset(ch,0,sizeof(ch));
    
        scanf("%d%d\n",&N,&M);
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++) {
                scanf("%d",&ar[i][j]);
            }
        solve();
        printf("Case #%d:\n", t);
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (j==0) printf("%c",ch[i][j]);
                else printf(" %c",ch[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
