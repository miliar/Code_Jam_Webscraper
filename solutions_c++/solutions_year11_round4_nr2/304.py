#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define MST(t,v) memset(t,v,sizeof(t))
int R, C, D;
int ax[512][512], ay[512][512], bx[512][512], by[512][512];
char S[512][512];
int M[512][512];
int Sum(int i, int j, int i2, int j2, int ax[][512]) {
    return  ax[i2][j2] - ax[i-1][j2] - ax[i2][j-1] + ax[i-1][j-1];
}
bool ok(int i, int j, int k){
	int i2 = i+k-1;
     int j2 = j+k-1;
	  int v2 = (Sum(i, j, i2, j2, bx)
              - M[i2][j2] - M[i][j2] - M[i2][j] - M[i][j]) * (j + j2);
     int v1 = (Sum(i, j, i2, j2, ax)
           - M[i2][j2] * j2 - M[i][j2] * j2 - M[i2][j] * j - M[i][j] * j) * 2;
    
    bool same =  v1 == v2;
    v1 = (Sum(i, j, i2, j2, ay)
           - M[i2][j2] * i2 - M[i][j2] * i - M[i2][j] * i2 - M[i][j] * i) * 2;
    v2 = (Sum(i, j, i2, j2, by)
              - M[i2][j2] - M[i][j2] - M[i2][j] - M[i][j]) * (i + i2);
    bool sameb = v1  == v2;
    return same && sameb;           
}
int main()
{
    freopen("a.in", "r", stdin);freopen("a.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
		memset(ax, 0, sizeof(ax));
       memset(bx, 0, sizeof(bx));
        memset(ay, 0, sizeof(ay));
       memset(by, 0, sizeof(by));
       scanf("%d%d%d", &R, &C, &D);
       for(i = 1; i <= R; ++i)
       {
           scanf("%s", S[i] + 1);
           for(j = 1; j <= C; ++j)
              M[i][j] = S[i][j] - '0';
       }
       for(i = 1; i <= R; ++i)       
          for(j = 1; j <= C; ++j)
          {
              ax[i][j] = ax[i-1][j] + ax[i][j-1] - ax[i-1][j-1] + M[i][j]* j;
              ay[i][j] = ay[i-1][j] + ay[i][j-1] - ay[i-1][j-1] + M[i][j] * i;
              
              bx[i][j] = bx[i-1][j] + bx[i][j-1] - bx[i-1][j-1] + M[i][j];
              by[i][j] = by[i-1][j] + by[i][j-1] - by[i-1][j-1] + M[i][j];
          }
       
       int ans = 0;
       
       for(i = 1; i <= R; ++i)
           for(j = 1; j <= C; ++j)
               for(k = max(ans + 1, 3); k <= min(R - i, C - j) + 1; ++k)
               {
                   if(ok(i, j, k)) ans = k;
               }
      if(ans < 3) {
              printf("Case #%d: IMPOSSIBLE\n", ++cs);
       } else {
        printf("Case #%d: %d\n", ++cs, ans);
       }
    }
	return 0;
}

