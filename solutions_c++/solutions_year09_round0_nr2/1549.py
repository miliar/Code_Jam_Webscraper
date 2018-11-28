#include<stdio.h>
#include<memory.h>
int t,h,w;
int basin = 0;//broj sinkova
FILE *f, *g;
int a[101][101];
int m[101][101];//1 n, 2 w, 3 e, 4 s, 0 sink, matrica kretanja
char color[101][101];
bool visited[101][101];
bool moze(int i1, int j1)
{
if(i1>=1&&j1>=1)
if(i1<=h&&j1<=w)
return true;
return false;
}

char dfs(int i1, int j1)
{
if(!visited[i1][j1])
{
if(m[i1][j1]==1) color[i1][j1] = dfs(i1-1,j1); else if(m[i1][j1]==2) color[i1][j1] = dfs(i1,j1-1);
else if(m[i1][j1]==3) color[i1][j1] = dfs(i1,j1+1); else if(m[i1][j1]==4) color[i1][j1] = dfs(i1+1,j1);
visited[i1][j1] = 1; return color[i1][j1];
}
return color[i1][j1];
}

void fix()
{
bool appear[27];//da li smo do sada dosli do tog
char map[270];
memset(appear,0,sizeof(appear));
int br = 0;
for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
if(!appear[color[i][j]-'a'+1]) { appear[color[i][j]-'a'+1] = true; br++; map[color[i][j]] = 'a'+br-1; }
for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
color[i][j] = map[color[i][j]];
}

int main()
{
f = fopen("B-small.in","r");
g = fopen("rex.txt","w");
fscanf(f,"%d",&t);
for(int l = 1; l <= t; l++)
{
    basin = 0;
fscanf(f,"%d %d",&h,&w);
for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
fscanf(f,"%d",&a[i][j]);
//ucitana, ajmo sada na m
for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
{
int min = a[i][j]; m[i][j] = 0;
if(moze(i-1,j)&&a[i-1][j]<min) { m[i][j] = 1; min = a[i-1][j]; }
if(moze(i,j-1)&&a[i][j-1]<min) { m[i][j] = 2; min = a[i][j-1]; }
if(moze(i,j+1)&&a[i][j+1]<min) { m[i][j] = 3; min = a[i][j+1]; }
if(moze(i+1,j)&&a[i+1][j]<min) { m[i][j] = 4; min = a[i+1][j]; }
}
//napravljena matrica kretanja
memset(color,0,sizeof(color));
memset(visited, 0, sizeof(visited));

for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
{
if(m[i][j]==0) { basin++; color[i][j] = 'a'+basin-1; visited[i][j] = 1; }
}

//sinkovi obojeni

for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
{
char c = dfs(i,j);
color[i][j] = c;
}
//sada smo obojili celu, samo treba sortirati boje, pa ispisati

fix();//lexikografija

fprintf(g,"Case #%d: \n",l);
for(int i = 1; i <= h; i++)
for(int j = 1; j <= w; j++)
{
if(j!=w) fprintf(g,"%c ",color[i][j]);
else fprintf(g,"%c\n",color[i][j]);
}

}
}
