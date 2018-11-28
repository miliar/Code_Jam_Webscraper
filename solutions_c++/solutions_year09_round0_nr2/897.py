#include <stdio.h>
#include <memory.h>
int h, w, map[105][105], rk[20005], fa[20005], no = 1, at[20005];
int nx[4] = {-1, 0, 0, 1};
int ny[4] = {0, -1, 1, 0};
bool vis[20005]; 
void initSet()
{
int i, j;
for(i=1; i<=h; ++i)
{
for(j=1; j<=w; ++j)
{
rk[i*w+j] = 1;
fa[i*w+j] = i*w + j;
}
}
}

int findSet( int x )
{
if( x != fa[x] )
{
fa[x] = findSet(fa[x]);
}
return fa[x];
}

void unionSet( int x, int y )
{
x = findSet(x);
y = findSet(y);
if( x == y ) return;
if( rk[x] < rk[y] ) fa[x] = y;
else fa[y] = x;
if( rk[x] == rk[y] ) rk[x]++;
}

bool overpass( int x, int y )
{
if( x<=0 || x>h || y<=0 || y>w ) return true;
return false;
}

void Merge()
{
int i, j, k;
for(i=1; i<=h; ++i)
{
for(j=1; j<=w; ++j)
{
int Min = map[i][j], dir = -1;
for(k=0; k<4; ++k)
{
int tx = i + nx[k];
int ty = j + ny[k];
if( overpass(tx, ty) ) continue;
if( map[tx][ty] < Min )
{
Min = map[tx][ty];
dir = k;
}
}
int tx = i + nx[dir];
int ty = j + ny[dir];
if( dir != -1 ) unionSet(i*w+j, tx*w+ty);
}
}
}

void Output()
{
memset(vis, 0, sizeof(vis));
int i, j, now = 0;
for(i=1; i<=h; ++i)
{
for(j=1; j<=w; ++j)
{
int f = findSet(i*w+j);
if( !vis[f] )
{
vis[f] = true;
at[f] = now++;
}
if( j != 1 ) putchar(' ');
printf("%c", at[f] + 'a');
}
putchar('\n');
}
}

int main()
{
freopen("B-large.in", "r", stdin);
freopen("out22.txt", "w", stdout);
int t;
scanf("%d", &t);
while( t-- )
{
scanf("%d %d", &h, &w);
int i, j;
for(i=1; i<=h; ++i)
{
for(j=1; j<=w; ++j)
{
scanf("%d", &map[i][j]);
}
}
initSet();
Merge();
printf("Case #%d:\n", no++);
Output();
}
return 0;
}
