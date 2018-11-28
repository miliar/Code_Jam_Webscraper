// =====================================================================================
//   [ Filename    ]  main.cpp
//   [ Description ]  Watersheds
//   [ Created     ]  09/03/09 11:32:11 CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

class Data
{
   public:
      void read()
      {
         cin >> h >> w;
         allt.resize(h);
         isSink.resize(h);
         mark.resize(h);
         for (int i = 0; i < h; ++i) {
            allt[i].resize(w);
            isSink[i].resize(w);
            mark[i].resize(w);
            for (int j = 0; j < w; ++j)
               cin >> allt[i][j];
         }
         markSink();
      }
      void markSink()
      {
         char m = 'a';
         int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
         for (int i = 0; i < h; ++i)
            for (int j = 0; j < w; ++j) {
               bool iss = true;
               for (int d = 0; d < 4; ++d) {
                  int x = i + dir[d][0];
                  int y = j + dir[d][1];
                  if (!legal(x, y))
                     continue;
                  if (allt[x][y] < allt[i][j]) {
                     iss = false;
                     break;
                  }
               }
               isSink[i][j] = iss;
               if (iss)
                  mark[i][j] = m++;
            }
      }
      bool legal(int x, int y) {
         return (x >= 0 && x < h && y >= 0 && y < w);
      }

      class Point
      {
         public:
            Point(int _x = 0, int _y = 0):x(_x), y(_y) { }
            int x, y;
            bool operator == (const Point& rhs) {
               return (rhs.x == x && rhs.y == y);
            }
      };

      void flood() {
         for (int i = 0; i < h; ++i)
            for (int j = 0; j < w; ++j)
               if (isSink[i][j])
                  floodSub(i, j);
      }

      void floodSub(int x, int y) {
         queue<Point> q;
         q.push(Point(x, y));
         const char m = mark[x][y];
         const int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
         while (!q.empty()) {
            Point pos = q.front();
            q.pop();
            for (int d = 0; d < 4; ++d) {
               int nx = pos.x + dir[d][0];
               int ny = pos.y + dir[d][1];
               if (!legal(nx, ny))
                  continue;
               if (flowTo(nx, ny) == pos) {
                  mark[nx][ny] = m;
                  q.push(Point(nx, ny));
               }
            }
         }
      }

      Point flowTo(int x, int y) {
         const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
         int min = allt[x][y];
         Point which(~0u, ~0u);
         for (int d = 0; d < 4; ++d) {
            int nx = x + dir[d][0];
            int ny = y + dir[d][1];
            if (!legal(nx, ny))
               continue;
            if (allt[nx][ny] < min) {
               min = allt[nx][ny];
               which = Point(nx, ny);
            }
         }
         return which;
      }
      void output() {
         for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j)
               cout << mark[i][j] << " ";
            cout << endl;
         }
      }
      void remark() {
         char mm = 'a';
         map<char,char> cm;
         vector<vector<char> > ret;
         ret.resize(h, vector<char>(w));
         for (int i = 0; i < h; ++i)
            for (int j = 0; j < w; ++j) {
               char org = mark[i][j];
               if (cm.find(org) == cm.end())
                  cm[org] = mm++;
               ret[i][j] = cm[org];
            }
         mark = ret;
      }
      int w, h;
      vector<vector<int> > allt;
      vector<vector<bool> > isSink;
      vector<vector<char> > mark;
};

void run(int caseNo)
{
   Data data;
   data.read();
   data.flood();
   cout << "Case #" << caseNo << ":" << endl;
   data.remark();
   data.output();
}

int main()
{
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t)
      run(t);
   return 0;
}
