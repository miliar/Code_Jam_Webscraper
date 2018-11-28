#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

int mapa[100][100];
char res[100][100];

int r, c;
char cur;

#define OK(x, y) ((x)>=0 && (x) < r && (y) >=0 && (y) < c)
void go(int x, int y)
{
  vector<pair<int, int> > kol;
  kol.push_back(make_pair(x, y));

  while(res[kol.back().first][kol.back().second] == '\0')
  {
    x = kol.back().first;
    y = kol.back().second;
    int old = kol.size();
    int kx = x, ky = y;

    if(OK(x-1, y) && mapa[x-1][y] < mapa[kx][ky])
    {
      kx = x-1;
      ky = y;
    }
    if(OK(x, y-1) && mapa[x][y-1] < mapa[kx][ky])
    {
      kx = x;
      ky = y-1;
    }
    if(OK(x, y+1) && mapa[x][y+1] < mapa[kx][ky])
    {
      kx = x;
      ky = y+1;
    }
    if(OK(x+1, y) && mapa[x+1][y] < mapa[kx][ky])
    {
      kx = x+1;
      ky = y;
    }

    if(kx == x && ky == y)
      res[x][y] = cur++;
    else
      kol.push_back(make_pair(kx, ky));
  }

  for(int i=0;i<kol.size();++i)
    res[kol[i].first][kol[i].second] = res[kol.back().first][kol.back().second];
}

int cas = 1;

void fun()
{
  cur = 'a';
  scanf("%d%d", &r, &c);
  for(int i=0;i<r;++i)
    for(int k=0;k<c;++k)
    {
      res[i][k] = '\0';
      scanf("%d", &mapa[i][k]);
    }

  for(int i=0;i<r;++i)
    for(int k=0;k<c;++k)
      if(res[i][k] == '\0')
        go(i, k);

  printf("Case #%d:\n", cas++);
  for(int i=0;i<r;++i)
  {
    for(int k=0;k<c;++k)
      printf("%c%s", res[i][k], k != c-1 ? " " : "");
    printf("\n");
  }
}

int main()
{
  int n;
  scanf("%d", &n);
  while(n--)
    fun();

  return 0;
}

