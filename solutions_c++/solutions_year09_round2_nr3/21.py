#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////


int W;

int H = 2500, shH = 1000;

int dist[20][20][2500][2];

char tab[20][20];

queue<pair<pii, pii> > Q;

void wstaw(int x, int y, int h, int a, int d) {
    if (h<0 || h>=H) 	return;
    if (d>=dist[x][y][h][a]) return;
    dist[x][y][h][a] = d;
    Q.push(MP(MP(x, y), MP(h, a)));
}

inline bool cyfra(int x, int y) { return tab[x][y]>='0' && tab[x][y]<='9'; }
inline int val(int x, int y, int a) { int v = tab[x][y]-'0'; return a ? -v : v; } 

//a=0 --> +, a==1 --> -

int xd[4] = {-1,1,0,0};
int yd[4] = {0,0,-1,1};

int main() {
    int N,Qn;
    scanf("%d", &N);
    REP(t, N) {
        printf("Case #%d:\n", t+1);
        scanf("%d%d", &W, &Qn);
        REP(x, W) REP(y, W) scanf(" %c", &tab[x][y]);
        
        REP(x, W) REP(y, W) REP(h, H) REP(a, 2) dist[x][y][h][a] = INF;
        REP(x, W) REP(y, W) if (cyfra(x, y)) REP(a, 2) wstaw(x, y, shH+val(x, y, a), a, 1);
        
        while (!Q.empty()) {
            int x = Q.front().first.first;
            int y = Q.front().first.second;
            int h = Q.front().second.first;
            int a = Q.front().second.second;
            Q.pop();
            REP(d, 4) {
                int nx = x+xd[d];
                int ny = y+yd[d];
                if (nx<0 || ny<0 || nx>=W || ny>=W) continue;
                if (cyfra(x, y)) {
                    if ((tab[nx][ny]=='+' && a==0) || (tab[nx][ny]=='-' && a==1))
                        wstaw(nx, ny, h, 0, dist[x][y][h][a]+1);
                }
                else {
                    wstaw(nx, ny, h+val(nx, ny, 0), 0, dist[x][y][h][0]+1);
                    wstaw(nx, ny, h+val(nx, ny, 1), 1, dist[x][y][h][0]+1);
                }
            }
        }
        
        REP(test, Qn) {
            int q;
            scanf("%d", &q);
            int best = INF;
            set<pii> gdzie, tmp;
            REP(x, W) REP(y, W) {
                if (!cyfra(x, y))
                    continue;
                if (dist[x][y][shH+q][0]<best) {
                    best = dist[x][y][shH+q][0];
                    gdzie.clear();
                }
                if (dist[x][y][shH+q][0]==best)
                    gdzie.insert(MP(x, y));
            }
            int h = shH+q;
            int a = 0;
            for (;;) {
                char cmin = 127;
                FOREACH(it, gdzie)
                    cmin = min(cmin, tab[it->first][it->second]);
                printf("%c", cmin);
                tmp.clear();
                int nh;
                FOREACH(it, gdzie) {
                    int x = it->first;
                    int y = it->second;
                    if (tab[x][y]!=cmin)
                        continue;
                    nh = h-val(x, y, a);
                    REP(d, 4) {
                        int nx = x+xd[d];
                        int ny = y+yd[d];
                        if (nx<0 || ny<0 || nx>=W || ny>=W) continue;
                        if (dist[nx][ny][nh][0]+1>dist[x][y][h][a]) continue;
                        tmp.insert(MP(nx, ny));
                    }
                }
                h = nh;
                gdzie = tmp;
                if (gdzie.empty())
                    break;
                //////////////////////
                cmin = 127;
                FOREACH(it, gdzie)
                    cmin = min(cmin, tab[it->first][it->second]);
                printf("%c", cmin);
                a = (cmin=='-');
                tmp.clear();
                FOREACH(it, gdzie) {
                    int x = it->first;
                    int y = it->second;
                    if (tab[x][y]!=cmin)
                        continue;
                    REP(d, 4) {
                        int nx = x+xd[d];
                        int ny = y+yd[d];
                        if (nx<0 || ny<0 || nx>=W || ny>=W) continue;
                        if (dist[nx][ny][h][a]+1>dist[x][y][h][0]) continue;
                        tmp.insert(MP(nx, ny));
                    }
                }
                gdzie = tmp;
            }
            printf("\n");
        }
    }
    
}


