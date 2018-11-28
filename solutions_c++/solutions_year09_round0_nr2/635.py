#include <cstdio>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int mw = 103;
const int m = mw * mw;

int w, h, nt, a[mw][mw], si[m], pa[m];
char res[m];
const int di[] = { -1,  0, 0, 1 };
const int dj[] = {  0, -1, 1, 0 };

void join( int i, int j )
{
  if (si[i] > si[j]) swap(i, j);
  pa[i] = j;
  if (si[i] == si[j]) si[j]++;
}

int get( int i )
{
  return (i == pa[i]) ? i : (pa[i] = get(pa[i]));
}

int main()
{
  scanf("%d", &nt);
  forn (t, nt)
  {
    scanf("%d%d", &h, &w);
    forn (i, h)
      forn (j, w)
      {
        scanf("%d", &a[i][j]);
        int pos = i * w + j;
        si[pos] = 0, pa[pos] = pos;
        res[pos] = 0;
      }
    forn (i, h)
      forn (j, w)
      {
        int be = -1, bev = a[i][j], pos = i * w + j;
        forn (k, 4)
        {
          int ii = i + di[k], jj = j + dj[k];
          if (ii < 0 || ii >= h || jj < 0 || jj >= w ||
              a[ii][jj] >= a[i][j])
            continue;
          if (a[ii][jj] < bev)
            bev = a[ii][jj], be = ii * w + jj;
        }
        if (be != -1)
          join(get(pos), get(be));
      }
    char cur = 'a';
    forn (i, h * w)
      if (res[get(i)] == 0)
        res[get(i)] = cur++;
    printf("Case #%d:\n", t + 1);
    forn (i, h)
      forn (j, w)
        printf("%c%c", res[get(i * w + j)], " \n"[j == w - 1]);
  }
  return 0;
}
