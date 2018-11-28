#include <iostream>
#include <cstdio>
using namespace std;

#define MAXD 100

int inp[MAXD][MAXD], H, W;

char res[MAXD][MAXD];

bool vis[MAXD][MAXD];

int da[] = {-1,0,0,1};
int db[] = {0,-1,1,0};

int savea[10000], saveb[10000];

void populate(int a, int b, int &num)
{
 int ind = 1;
 savea[0] = a;
 saveb[0] = b;
 vis[a][b] = true;
 
 while (true)
 {
  int mAlt = 1000000, besta = -1, bestb = -1;
  
  for (int i = 0; i < 4; i++)
  {
   int na = a + da[i], nb = b + db[i];
   if (na < 0 || nb < 0 || na >= H || nb >= W) continue;
  
   if (inp[na][nb] < inp[a][b] && inp[na][nb] < mAlt)
   {
    mAlt = inp[na][nb];
    besta = na;
    bestb = nb;
   }
  }
  
  if (mAlt == 1000000) break;
  
  a = besta;
  b = bestb;
  
  savea[ind] = a;
  saveb[ind] = b;
  ind++;
  
  if (vis[a][b])
  {
   for (int i = 0; i < ind; i++)
    res[savea[i]][saveb[i]] = res[a][b];
   return;
  }
  
  vis[a][b] = true;
 } 
 
 for (int i = 0; i < ind; i++)
  res[savea[i]][saveb[i]] = (char)('a' + num);
 
 num++;
}

void solve()
{
 memset(vis, 0, sizeof(vis));
 
 int curb = 0;
 for (int i = 0; i < H; i++)
  for (int j = 0; j < W; j++)
  {
   if (vis[i][j]) continue;
   populate(i, j, curb);
  }
}

int main()
{
 int T;
 scanf("%d", &T);
 
 for (int t = 1; t <= T; t++)
 {
  scanf("%d%d", &H, &W);
  for (int a = 0; a < H; a++)
   for (int b = 0; b < W; b++)
    scanf("%d", &inp[a][b]);
  
  solve();
    
  printf("Case #%d:\n", t);
  for (int a = 0; a < H; a++)
   for (int b = 0; b < W; b++)
    if (b == W - 1)
     printf("%c\n", res[a][b]);
    else
     printf("%c ", res[a][b]);
 }
 
 return 0;
}
