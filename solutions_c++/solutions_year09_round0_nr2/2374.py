#include<iostream>
#include<cstring>

using namespace std;

int ways[2][4]={{-1,0,0,1},{0,-1,1,0}};
int n, m;

int kind[1010][1010];
int br = 1;

int G[1010][1010];
int used[100000];

int go(int x,int y)
{
    if(kind[x][y])return kind[x][y];
    int i, tmp = G[x][y];
    int nextx, nexty = -1;
    nextx = -1;

    for(i = 0; i < 4; ++i)
    {
     int p, q;
     p = x + ways[0][i];
     q = y + ways[1][i];

     if(p>=0 && p < n)
     if(q>=0 && q < m)
     if(G[p][q] < tmp) {tmp = G[p][q]; nextx = p; nexty = q;}
    }

    if(nextx!=-1)kind[x][y] = go(nextx,nexty);// printf("ot tuk dodi %d %d natam otidi %d %d\n",x,y,nextx,nexty);
    else kind[x][y] = br++;

return kind[x][y];
}
void input()
{
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i)
     for(int j = 0; j < m; ++j)scanf("%d", &G[i][j]);
}
void solve()
{
   input();
   memset(kind, 0, sizeof(kind));
   memset(used, 0, sizeof(used));

   int i, j;
   int ul = 1;

   for(i = 0; i < n; ++i)
    for(j = 0; j < m; ++j)
    {
     int u = go(i,j); //printf("za %d %d imam kind %d\n",i,j,u);
     if(!used[u])used[u] = ul++;

     if(j!=m-1)printf("%c ",'a' + used[u] - 1);
     else printf("%c\n",'a' + used[u] - 1);
    }
}
int main()
{
   int t, i = 1; scanf("%d", &t);
   for(;t;t--)
   {
    printf("Case #%d:\n", i);
    solve();
    i++;
   }
return 0;
}
