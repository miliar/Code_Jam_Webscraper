#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define MAX 128

int b[2][MAX],foi[MAX][MAX][MAX];

typedef struct tq
{
  int x[2],t,done;
} tq;

bool operator <(const tq &X, const tq &Y)
{
  return(X.t <= Y.t);
}

int main(void)
{
  int T,caso;

  for(scanf("%d",&T), caso = 1; caso <= T; caso++)
  {
    int N;
    scanf("%d",&N);
    for(int i = 0; i < N; i++)
    {
      char s[8];
      scanf("%s %d",s,&b[1][i]);
      b[0][i] = (s[0] == 'B');
    }

    memset(foi,0x3f,sizeof(foi));

    set<tq> q;
    tq u,v;
    u.x[0] = u.x[1] = 1;
    u.t = 0;
    u.done = 0;
    foi[u.x[0]][u.x[1]][u.done] = u.t;

    q.insert(u);

    while(!q.empty())
    {
      /*
      for(set<tq>::iterator it = q.begin(); it != q.end(); it++)
        printf("[%d %d / %d %d]", it->x[0], it->x[1], it->t, it->done);
      printf("\n");
      */
      u = *(q.begin());
      //printf("[%d %d / %d %d]", u.x[0], u.x[1], u.t, u.done);
      q.erase(q.begin());
      if (u.done >= N)
        break;


      v.t = u.t+1;
      int w = b[0][u.done];
      //printf("(%d %d)", w, b[1][u.done]);

      // press
      if (u.x[w] == b[1][u.done])
      {
        v.x[w] = u.x[w];
        v.done = u.done+1;
        for(v.x[1-w] = u.x[1-w]-1; v.x[1-w] <= u.x[1-w]+1; v.x[1-w]++)
          if (v.x[1-w] >= 1 && v.x[1-w] <= 100)
            if (v.t < foi[v.x[0]][v.x[1]][v.done])
            {
              int temp = v.t;
              v.t = foi[v.x[0]][v.x[1]][v.done];
              if (v.t < 0x3f3f3f3f)
                q.erase(q.find(v));
              v.t = temp;
              foi[v.x[0]][v.x[1]][v.done] = v.t;
              q.insert(v);
            }
      }
      else
      {
        v.done = u.done;
        for(v.x[0] = u.x[0]-1; v.x[0] <= u.x[0]+1; v.x[0]++)
          if (v.x[0] >= 1 && v.x[0] <= 100)
            for(v.x[1] = u.x[1]-1; v.x[1] <= u.x[1]+1; v.x[1]++)
              if (v.x[1] >= 1 && v.x[1] <= 100)
                if (v.t < foi[v.x[0]][v.x[1]][v.done])
                {
                  int temp = v.t;
                  v.t = foi[v.x[0]][v.x[1]][v.done];
                  if (v.t < 0x3f3f3f3f)
                      q.erase(q.find(v));
                  v.t = temp;
                  foi[v.x[0]][v.x[1]][v.done] = v.t;
                  //printf("(%d %d / %d %d)", v.x[0], v.x[1], v.t, v.done);
                  q.insert(v);
                }
      }

    }

    printf("Case #%d: %d\n", caso, u.t);
  }

  return(0);
}

