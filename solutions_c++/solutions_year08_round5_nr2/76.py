#include <iostream>
#include <queue>
using namespace std;

vector<string> map;
int X, Y;
vector<pair<int, pair<int, int> > > get_portals(int x, int y)
{
  vector<pair<int, pair<int, int> > > ret;
  int xx;
  for (xx = x+1; xx < X; xx++) {
    if (map[y][xx] == '#') break;
  }
  ret.push_back(make_pair(xx-x, make_pair(xx-1, y)));
  for (xx = x-1; xx >= 0; xx--) {
    if (map[y][xx] == '#') break;
  }
  ret.push_back(make_pair(x-xx, make_pair(xx+1, y)));

  int yy;
  for (yy = y+1; yy < Y; yy++) {
    if (map[yy][x] == '#') break;
  }
  ret.push_back(make_pair(yy-y, make_pair(x, yy-1)));
  for (yy = y-1; yy >= 0; yy--) {
    if (map[yy][x] == '#') break;
  }
  ret.push_back(make_pair(y-yy, make_pair(x, yy+1)));

  return ret;
}

int main() {
  int cases;
  cin >> cases;
  for (int caseno=1; caseno<=cases; caseno++) {
    cin >> Y >> X;
    map = vector<string>();
    for (int i=0; i<Y; i++) {
      string s;
      cin >> s;
      map.push_back(s);
    }

    const int INF = 1000000;
    int best[20][20];
    int sx, sy, ex, ey;
    for (int y=0; y<Y; y++) {
      for (int x=0; x<X; x++) {
        best[y][x] = INF;
        if (map[y][x] == 'O') sx = x, sy = y;
        if (map[y][x] == 'X') ex = x, ey = y;
      }
    }

    int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};

    queue<pair<int, int> > q;
    q.push(make_pair(sx, sy));
    best[sy][sx] = 0;
    while (!q.empty()) {
      pair<int, int> u = q.front(); q.pop();
      int x = u.first, y = u.second;
      int c = best[y][x];
      for (int dir=0; dir<4; dir++) {
        int nx = x + dx[dir], ny = y + dy[dir];
        if (nx < 0 || nx >= X || ny < 0 || ny >= Y) continue;
        if (map[ny][nx] == '#') continue;
        if (best[ny][nx] > c+1) {
          best[ny][nx] = c+1;
          q.push(make_pair(nx, ny));
        }
      }
      vector<pair<int, pair<int, int> > > portals = get_portals(x, y);
      sort(portals.begin(), portals.end());
      for (int i=0; i<portals.size(); i++) {
        int c2 = i > 0 ? portals[0].first : portals[1].first;
        int nx = portals[i].second.first, ny = portals[i].second.second;
        if (best[ny][nx] > c + c2) {
          best[ny][nx] = c + c2;
          q.push(make_pair(nx, ny));
        }
      }
    }

    int res = best[ey][ex];
    if (res < INF) {
      cout << "Case #" << caseno << ": " << res << endl;
    } else {
      cout << "Case #" << caseno << ": THE CAKE IS A LIE" << endl;
    }
  }
}
