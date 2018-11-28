#include<cstdio>
#include<cstring>
#include<list>
using namespace std;

bool fav[2000][2000];
int tu[2000];
int fm[2000];
bool sch[2000];
int n, m;
int c;
int zn;

void init()
{
  zn = 0;
  memset(sch, 0, sizeof(sch));
  memset(fav, 0, sizeof(fav));
  memset(fm, 255, sizeof(fm));
  scanf(" %d", &n);
  scanf(" %d", &m);
  for (int i = 0; i < m; ++i) {
    scanf(" %d", tu+i);
    int t = tu[i];
    for (int j = 0; j < t; ++j) {
      int x, y;
      scanf(" %d %d", &x, &y);
      if (y == 0) {
	fav[i][x-1] = true;
      } else {
	--tu[i];
	fm[i] = x-1;
      }
    }
    if (tu[i] == 0) {
      ++zn;
    }
  }
}

void reduce(int v)
{
  for (int i = 0; i < m; ++i) {
    if (fav[i][v]) {
      --tu[i];
      fav[i][v] = false;
      if (tu[i] == 0) {
	++zn;
      }
    }
  }
}

bool proc()
{
  while (zn != 0) {
    int t;
    for (int i= 0; i < m; ++i) {
      if (tu[i] == 0) {
	t = i;
	break;
      }
    }
    if (fm[t] == -1) {
      return false;
    } else {
      tu[t] = -1;
      --zn;
      if (!sch[fm[t]]) {
	sch[fm[t]] = true;
	reduce(fm[t]);
      }
    }
  }
  return true;
}

void outp()
{
  for (int i = 0; i < n; ++i) {
    if (i != 0) {printf(" ");}
    if (sch[i]) {
      printf("1");
    } else {
      printf("0");
    }
  }
  printf("\n");
}

int main()
{
  scanf(" %d", &c);
  for (int i = 0; i < c; ++i) {
    init();
    printf("Case #%d: ", i+1);
    if (proc()) {
      outp();
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
}
