#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define Maze(x,y) maze[(W)*(y)+(x)]
#define LRMaze(x,y) maze[(W)*(y)+(W)-(x)-1]
#define UDMaze(x,y) maze[(W)*((H)-(y)-1)+(x)]
#define LRUDMaze(x,y) maze[(W)*((H)-(y)-1)+(W)-(x)-1]
#define FullMaze(x,y) full_maze[(FW)*(y)+(x)]

// Gloval variable
int T, H, W, D;
int FH, FW, FXx, FXy, Xx, Xy;
char *maze;
char *full_maze;
char *line;

//------------------------------------------------------------------------------
// GetGCM()
//------------------------------------------------------------------------------
int GetGCM(int a, int b) {
  if (a<0)
    a*=-1;
  if (b<0)
    b*=-1;

  // a < b
  if (b > a) {
    int tmp;
    tmp = a;
    a = b;
    b = tmp;
  }

  if (a==0)
    return b;
  if (b==0)
    return a;
  int r;
  while((r = b % a) != 0) {
    b = a;
    a = r;
  }
  return a;
}

//------------------------------------------------------------------------------
// SetupFullMaze()
//------------------------------------------------------------------------------
void SetupFullMaze() {
  // copy maze
  for (int y=0; y!=FH; ++y) {
    for (int x=0; x!=FW; ++x) {
      if (((x / W) % 2) == 0 && ((y / H) % 2) == 0) {
        FullMaze(x, y) = Maze(x%W, y%H);
      } else if (((x / W) % 2) != 0 && ((y / H) % 2) == 0) {
        FullMaze(x, y) = LRMaze(x%W, y%H);
      } else if (((x / W) % 2) == 0 && ((y / H) % 2) != 0) {
        FullMaze(x, y) = UDMaze(x%W, y%H);
      } else {
        FullMaze(x, y) = LRUDMaze(x%W, y%H);
      }
    }
  }

  // Center
  FullMaze(FXx, FXy) = 'E';
}

//------------------------------------------------------------------------------
// Solve()
//------------------------------------------------------------------------------
int Solve() {
  // Check distance
  for (int y=0; y!=FH; ++y) {
    for (int x=0; x!=FW; ++x) {
      if (FullMaze(x, y) == 'X') {
        if ((FXx - x)*(FXx - x) + (FXy - y)*(FXy - y) > D * D) {
          FullMaze(x, y) = '.';
        }
      }
    }
  }

  // Collide
  for (int y=0; y!=FH; ++y) {
    for (int x=0; x!=FW; ++x) {
      if (FullMaze(x, y) == 'X') {
        int dx = FXx - x;
        int dy = FXy - y;
        int gcm = GetGCM(dx, dy);
        //        printf("GCM(%d,%d)=%d\n", dx,dy,gcm);
        if (gcm != 0) {
          dx /= gcm;
          dy /= gcm;
          int i=1;
          while (FullMaze(x+i*dx, y+i*dy) != 'E') {
            if (FullMaze(x+i*dx, y+i*dy) == 'X' || FullMaze(x+dx, y+dy) == 'D') {
              FullMaze(x, y) = 'D';
            }
            ++i;
          }
        }
      }
    }
  }

  // Count
  int count = 0;
  for (int y=0; y!=FH; ++y) {
    for (int x=0; x!=FW; ++x) {
      if (FullMaze(x, y) == 'X') {
        count++;
      }
    }
  }
  return count;
}

//------------------------------------------------------------------------------
// DrawMaze()
//------------------------------------------------------------------------------
void DrawMaze() {
  printf("# Maze\n");
  printf("H=%d, W=%d, D=%d X=(%d,%d)\n", H, W, D, Xx, Xy);
  for (int y=0; y!=H; ++y) {
    for (int x=0; x!=W; ++x) {
      printf("%c", Maze(x, y));
    }
    printf("\n");
  }
}

//------------------------------------------------------------------------------
// DrawFullMaze()
//------------------------------------------------------------------------------
void DrawFullMaze() {
  printf("# FullMaze\n");
  printf("FH=%d, FW=%d, D=%d FX=(%d,%d)\n", FH, FW, D, FXx, FXy);
  for (int y=0; y!=FH; ++y) {
    for (int x=0; x!=FW; ++x) {
      printf("%c", FullMaze(x, y));
    }
    printf("\n");
  }
}

//------------------------------------------------------------------------------
// main()
//------------------------------------------------------------------------------
int main() {
  // Loop
  scanf("%d", &T);
  for (int i = 1; i != T+1; ++i) {
    scanf("%d", &H);
    scanf("%d", &W);
    scanf("%d", &D);
    H-=2;
    W-=2;

    FH = H;
    FXy = 0;
    while (FH < 2*D+H) {
      FH+= 4*H;
      FXy += 2*H;
    }
    FW = W;
    FXx = 0;
    while (FW< 2*D+W) {
      FW+= 4*W;
      FXx += 2*W;
    }
    maze = (char *)malloc(H*W);
    full_maze = (char *)malloc(FH*FW);
    line = (char *)malloc(W+2+1);

    scanf("%s", line);
    for (int y = 0; y != H; ++y) {
      scanf("%s", line);
      for (int x = 0; x != W; ++x) {
        Maze(x, y) = line[x+1];
        if (line[x+1] == 'X') {
          Xx = x;
          Xy = y;
        }
      }
    }
    scanf("%s", line);
    FXx += Xx;
    FXy += Xy;

    // Setup full maze
    SetupFullMaze();

    // Draw mazes
    //    puts("---------------------------------------");
    //    DrawMaze();
    //    DrawFullMaze();

    // Solve
    printf("Case #%d: %d\n", i, Solve());
    //    DrawFullMaze();

    free(maze);
    free(full_maze);
    free(line);
  }

  return 0;
}
