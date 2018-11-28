#include <cstdio>
#include <algorithm>
using namespace std;

int tasks, t, h, w, licz, now, cells[100][100], b, basin[100][100];
char label[30];
struct pole
{
  int x, y, alt;
  pole(){};
  pole(int a, int b, int c) {x=a; y=b; alt=c;}
} tab[10000], best[4];

bool operator< (const pole& a, const pole &b)
{
  if(a.alt==b.alt)
  {
    if(a.y==b.y) return a.x<b.x;
    return a.y<b.y;
  }
  return a.alt<b.alt;
}

int main()
{
  scanf("%d", &tasks);
  for(int t=1; t<=tasks; ++t)
  {
    licz=now=0;
    scanf("%d%d", &h, &w);
    for(int i=0; i<h; ++i)
      for(int j=0; j<w; ++j)
      {
        scanf("%d", &cells[j][i]);
	tab[licz++]=pole(j, i, cells[j][i]);
      }
    sort(tab, tab+licz);
    for(int l=0; l<licz; ++l)
    {
      b=0;
      for(int i=tab[l].x-1; i<=tab[l].x+1; ++i)
        for(int j=tab[l].y-1; j<=tab[l].y+1; ++j)
	  if((i==tab[l].x || j==tab[l].y) && i>=0 && i<w && j>=0 && j<h)
	      best[b++]=pole(i, j, cells[i][j]);
      sort(best, best+b);
      if(b==0 || tab[l].alt<=best[0].alt)
        basin[tab[l].x][tab[l].y]=now++;
      else basin[tab[l].x][tab[l].y]=basin[best[0].x][best[0].y];
    }
    now='a';
    for(int i=0; i<30; ++i) label[i]=0;
    for(int i=0; i<h; ++i)
      for(int j=0; j<w; ++j)
        label[basin[j][i]]+=(label[basin[j][i]]==0)?(now++):0;
    printf("Case #%d:\n", t);
    for(int i=0; i<h; ++i)
    {
      for(int j=0; j<w; ++j) printf("%c ", label[basin[j][i]]);
      printf("\n");
    }
  }
  return 0;
}
