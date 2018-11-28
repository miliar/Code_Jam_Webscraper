#include <stdio.h>
#include <string.h>
#include <math.h>

#define min(a,b) ((a)<(b)?(a):(b))

int R,C, sx, sy, ex, ey;
bool v[17][17];
int dist[17][17];
int closestWall[17][17];
char maze[17][17];

void fillFrom(int i, int j, int d)
{
  if (i < 0 || j < 0 || i >= R || j >= C) return;
  if (closestWall[i][j] == -1 || closestWall[i][j] > d)
  {
    closestWall[i][j] = d;
    fillFrom(i+1, j, d+1);
    fillFrom(i-1, j, d+1);
    fillFrom(i, j+1, d+1);
    fillFrom(i, j-1, d+1);
  }
}

void fillDist()
{
  int i,j;
  for (i=0;i<R;i++)
    for (j=0;j<C;j++)
      if (maze[i][j] == '#')
        fillFrom(i,j,-1);
}
int getWallDist(int x, int y)
{
  if (closestWall[x][y] != -1)
    return closestWall[x][y];

  if (maze[x][y] == '#') return -1;

  int a = getWallDist(x-1,y);
  int b = getWallDist(x+1,y);
  int c = getWallDist(x,y-1);
  int d = getWallDist(x,y+1);

  if (a<0 || b<0 || c<0 || d<0)
    closestWall[x][y] = 0;
  else
  {
    a = min(a,b);
    c = min(c,d);
    a = min(a,c);
    closestWall[x][y] = a;
  }

  return closestWall[x][y];
}

void update(int x, int y, int d)
{
  if (maze[x][y] == '#') return;
  if (dist[x][y] == -1) dist[x][y] = d;
  else dist[x][y] = min(dist[x][y], d);
  return;
}

void dijkstra()
{
  int i,j,x,y,a;
  R += 2;
  C += 2;

  fillDist();

  //printf("sx %d sy %d ex %d ey %d\n", sx, sy, ex, ey);
  while(true)
  {
    a = -1;
    for (i=0;i<R;i++)
      for (j=0;j<C;j++)
        if (!v[i][j] && dist[i][j] >= 0)
          if (a == -1 || dist[i][j] < a)
          {
            a = dist[i][j];
            x=i;
            y=j;
          }

    if (a == -1) return; // no more points to visit that are reachable
    v[x][y] = true;
    //printf("visiting %d %d %d\n", x, y, a);

    if (x == ex && y == ey) return; // found exit

    update(x-1,y,a+1);
    update(x+1,y,a+1);
    update(x,y-1,a+1);
    update(x,y+1,a+1);


    for (i=1; maze[x+i][y] != '#'; i++);
    update(x+i-1,y,a+1+getWallDist(x,y));
    for (i=1; maze[x-i][y] != '#'; i++);
    update(x-i+1,y,a+1+getWallDist(x,y));
    for (i=1; maze[x][y+i] != '#'; i++);
    update(x,y+i-1,a+1+getWallDist(x,y));
    for (i=1; maze[x][y-i] != '#'; i++);
    update(x,y-i+1,a+1+getWallDist(x,y));
  }
}

int main()
{
  int cs, N, i, j;

  scanf("%d", &N);

  for (cs=1; cs<=N; cs++)
  {
    scanf("%d %d", &R, &C);
    memset(closestWall, -1, sizeof(closestWall));
    memset(dist, -1, sizeof(dist));
    memset(v, 0, sizeof(v));
    for (i=0;i<R+2;i++)
      for (j=0; j<C+2; j++)
        maze[i][j] = '#';

    for (i=1;i<=R;i++)
    {
      scanf("%s", maze[i]+1);
      maze[i][strlen(maze[i])] = '#';
    }

    bool pmaze = false;
    for (i=0;i<R+2; i++)
    {
      for (j=0;j<C+2; j++)
      {
        if (maze[i][j] == 'O')
        {
          sx=i;
          sy=j;
        }
        else if (maze[i][j] == 'X')
        {
          ex=i;
          ey=j;
        }

        if (pmaze)
          printf("%c", maze[i][j]);
      }
      if (pmaze)
        printf("\n");
    }
    
    dist[sx][sy] = 0;
    dijkstra();


    if (dist[ex][ey] == -1)
      printf("Case #%d: THE CAKE IS A LIE\n", cs);
    else
      printf("Case #%d: %d\n", cs, dist[ex][ey]);
  }

  return 0;
}
