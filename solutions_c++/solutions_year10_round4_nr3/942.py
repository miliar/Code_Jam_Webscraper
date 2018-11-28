
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

typedef struct Rec{
  int x1;
  int x2;
  int y1;
  int y2;
}Rec;

/*
typedef struct Poly {
  vector<int> lx;
  vector<int> ly;
  int rx;
  int ry;
}Poly;


static void merge(Poly& p, Rec& r)
{
  for (int i = 0; i < p.lx.size(); i++) {
    if (r.x1 < p.lx[i]) {

    }
  }

}





static void checkMax(int& dst, int src) {
  if (dst < src) dst = src;
}

static int inter(Rec* recs, int i, int j)
{
  


  return 0;
}

static int merge(Rec* recs, int* index, int i, int j)
{
  if (inter(recs, i, j) > 0) {
    index[j] = index[i];
  }
}


*/

static int cmp(const void* a, const void* b)
{
  Rec* ra = (Rec*) a;
  Rec* rb = (Rec*) b;
  if (ra->x1 == rb->x1) {
    return ra->y1 - rb->y1;
  } else {
    return ra->x1 - rb->x1;
  }
}

static int solve(int r, Rec* rects)
{
  int count = 0;
  bool visit[101][101];
  memset(visit, false, sizeof(visit));
  for (int i = 0; i < r; i++) {
    for (int j = rects[i].x1; j <= rects[i].x2; j++) {
      for (int k = rects[i].y1; k <= rects[i].y2; k++) {
        if (!visit[j][k]) {
          visit[j][k] = true;
          count++;
        } 
      }
    }
  }
  int time = 0;
 
  bool visit1[101][101];

  memcpy(visit1, visit, sizeof(visit));
  while (count > 0) {
      for (int j = 1; j <= 100; j++) {
        for (int k = 1; k <= 100; k++) {
          if (!visit[j][k]) {
            if (visit[j - 1][k] && visit[j][k-1]) {
              visit1[j][k] = true;
              count++;
            }
          } else {
            if (!visit[j - 1][k] && !visit[j][k-1]) {
              visit1[j][k] = false;
              count--;
            }
          }
        }
      
      }

    memcpy(visit, visit1, sizeof(visit));
    time++;
  }

  return time;
}


int main()
{

  int T;
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  
  for (int i = 1; i <= T; i++) {
    int r;
    Rec recs[1000];
    scanf("%d", &r);

    for (int k = 0 ; k < r; k++) {
      scanf("%d%d%d%d", &recs[k].x1, &recs[k].y1, &recs[k].x2, &recs[k].y2);
    }
    
    printf ("Case #%d: %d\n", i, solve(r, recs));
  }
  return 0;
}