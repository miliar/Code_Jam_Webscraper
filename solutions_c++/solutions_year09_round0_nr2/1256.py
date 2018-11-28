#include <stdio.h>
#include <cstring>

int dx[]={0, -1, 1, 0};
int dy[]={-1, 0, 0, 1};

int a[105][105], h, w;
char mark[105][105], cur;

int get(int i, int j)
{
  if (i>=0 && i<h && j>=0 && j<w) return a[i][j];
  return 10000000;
}

int dfs(int i, int j)
{
  if (mark[i][j]) return mark[i][j];
  int cmin=a[i][j], bd=-1;
  for (int d=0; d<4; d++)
    if (get(i+dy[d], j+dx[d])<cmin) cmin=get(i+dy[d], j+dx[d]), bd=d;
  if (bd!=-1)
    return mark[i][j]=dfs(i+dy[bd], j+dx[bd]);
  return mark[i][j]=cur++;
}

int main(void)
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);

  int tn, nt;
  scanf("%d", &nt);
  for (tn=0; tn<nt; tn++)
  {
    int i, j;
    memset(mark, 0, sizeof(mark));
    scanf("%d %d", &h, &w);
    for (i=0; i<h; i++)
      for (j=0; j<w; j++)
        scanf("%d", &a[i][j]);
 
    cur='a';
    for (i=0; i<h; i++)
      for (j=0; j<w; j++)
        if (!mark[i][j]) dfs(i, j);

    printf("Case #%d:\n", tn+1);
    for (i=0; i<h; i++)
      for (j=0; j<w; j++)
        printf("%c%c", mark[i][j], " \n"[j==w-1]);
  }

  return 0;
}