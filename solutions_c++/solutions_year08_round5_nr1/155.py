#include <algorithm>
#include <cstdio>
#include <string>

using namespace std;

#define forn(i,n) for (int i = 0, limit = (int)(n); i < limit; i++)

int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

#define maxr 6010

char c[maxr][maxr], c1[maxr][maxr], c2[maxr][maxr], c3[maxr][maxr], c4[maxr][maxr];

int main()
{
  int tests;
  scanf("%d", &tests);
  forn (test, tests)
  {
    int n;
    scanf("%d", &n);
    string s = "";
    forn (i, n)
    {
      char tmp[100];
      int ttt;
      scanf(" %s%d", tmp, &ttt);
      forn (j, ttt)
        s += tmp;
    }
    int minx = 0, miny = 0, curx = 0, cury = 0;
    int d = 0, cnt = 0;
    forn (i, s.length())
      if (s[i] == 'R')
        cnt++;
      else if (s[i] == 'L')
        cnt--;
    if (cnt < 0)
      forn (i, s.length())
        if (s[i] == 'L' || s[i] == 'R')
          s[i] = 'L' + 'R' - s[i];
    forn (i, s.length())
    {
      if (s[i] == 'F')
      {
        curx += dx[d], cury += dy[d];
//         fprintf(stderr, "%d,%d\n", curx, cury);
        minx = min(minx, curx);
        miny = min(miny, cury);
      }
      else if (s[i] == 'R')
        d = (d + 1) & 3;
      else if (s[i] == 'L')
        d = (d + 3) & 3;
    }
    minx -= 2, miny -= 2;
    memset(c, 0, sizeof(c));
    memset(c1, 0, sizeof(c1));
    memset(c2, 0, sizeof(c2));
    memset(c3, 0, sizeof(c3));
    memset(c4, 0, sizeof(c4));
    curx = -minx, cury = -miny;
    d = 0;
    forn (i, s.length())
    {
      if (s[i] == 'F')
      {
        if (dy[d] == 0)
        {
          if (dx[d] == 1)
            c[curx][cury]++;
          else if (dx[d] == -1)
            c[curx - 1][cury - 1]++;
//           fprintf(stderr, "%d,%d(%d,%d) <-\n", curx, cury, (curx + dx[d] - 1) / 2, cury + (dx[d] - 1) / 2);
//           fprintf(stderr, "  -< %d\n", c[curx + (dx[d] - 1) / 2][cury + (dx[d] - 1) / 2]);
        }
        curx += dx[d], cury += dy[d];
      }
      else if (s[i] == 'R')
        d = (d + 1) & 3;
      else if (s[i] == 'L')
        d = (d + 3) & 3;
    }
    forn (i, maxr)
    {
      int cnt = 0;
      forn (j, maxr)
        if (c[i][j] == 0)
          c[i][j] = cnt & 1;
        else
          cnt += c[i][j];
    }
    forn (i, maxr)
    {
      int cnt1 = 0, cnt2 = 0;
      forn (j, maxr)
      {
        cnt1 += c[i][j];
        cnt2 += c[i][maxr - 1 - j];
        if (cnt1 > 0)
          c1[i][j] = 1;
        if (cnt2 > 0)
          c2[i][maxr - 1 - j] = 1;
      }
    }
    forn (i, maxr)
    {
      int cnt1 = 0, cnt2 = 0;
      forn (j, maxr)
      {
        cnt1 += c[j][i];
        cnt2 += c[maxr - 1 - j][i];
        if (cnt1 > 0)
          c3[j][i] = 1;
        if (cnt2 > 0)
          c4[maxr - 1 - j][i] = 1;
      }
    }
//     forn (i, 20)
//       forn (j, 20)
//         fprintf(stderr, "%d%s", (((c1[i][j] && c2[i][j]) || (c3[i][j] && c4[i][j])) && !c[i][j]) ? 2 : !!c[i][j], j == 19 ? "\n" : "");
    int ans = 0;
    forn (i, maxr)
      forn (j, maxr)
        if (((c1[i][j] && c2[i][j]) || (c3[i][j] && c4[i][j])) && !c[i][j])
          ans++;
    printf("Case #%d: %d\n", test + 1, ans);
    fprintf(stderr, "Case #%d complete!\n", test);
  }
  return 0;
}
