#include<cstdio>

double pos(int x1, int y1, int x2, int y2, int x)
{
  return y1 + (y2 - y1) / (double)(x2 - x1) * (x - x1);
}

int calc_maxy(int x1, int y1, int x2, int y2, int x)
{
  int Y = (int)(pos(x1, y1, x2, y2, x) - 2);
  if(Y < 0) throw 0; // yabai
  return Y;
}

int main()
{
  int T;
  scanf("%d", &T);
  
  for(int CN=1; CN<=T; ++CN) {
    int N, to[2048];
    scanf("%d", &N);
    
    for(int i=0; i<N-1; ++i)
      scanf("%d", &to[i]), to[i]--;
    
    try {
      int visited[2048] = {0}, height[2048];
      for(int i=0; i<N; ++i) {
        if(visited[i]) continue;
        int tbd[2048], ts = 0;
        for(int u=i; ; u=to[u]) {
          tbd[ts++] = u;
          if(i>0 && u>to[i-1]) throw 1;
          if(u == N-1 || visited[u]) break;
          visited[u] = 1;
        }
        ts--;
        
        if(i == 0) {
          for(int j=0; j<=ts; ++j)
            height[tbd[j]] = 1000000000;
        } else {
          int x1 = i-1, y1 = height[i-1], x2 = to[i-1], y2 = height[to[i-1]];
          for(int j=ts-1; j>=0; --j) {
            height[tbd[j]] = calc_maxy(x1, y1, x2, y2, tbd[j]);
            if(j != ts-1) { x2 = x1; y2 = y1; }
            x1 = tbd[j]; y1 = height[tbd[j]];
          }
        }
      }
      printf("Case #%d:", CN);
      for(int i=0; i<N; ++i)
        printf(" %d", height[i]);
      puts("");
    } catch(int pos) {
      fprintf(stderr, "failed: %d\n", pos);
      printf("Case #%d: Impossible\n", CN);
    }
  }
  
  return 0;
}
