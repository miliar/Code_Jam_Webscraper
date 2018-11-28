#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cmath>
using namespace std;

#define maxn 550

#define mineps 1e-6

inline int cmp(double x) {
  if (fabs(x) < mineps) return 0;
  else if (x < 0) return -1;
  else return 1;
}

int T, n, m;
double a[maxn][maxn], sx[maxn][maxn], sy[maxn][maxn];
double sumx[maxn][maxn], sumy[maxn][maxn], mymass[maxn][maxn];
int ans;

int main() {
    
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    double D;
    
    cerr << "Test Case " << ctn << endl;
    
    scanf("%d%d%lf\n", &n, &m, &D);
    memset(a,0,sizeof(a));
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= m; j++) {
        char cht;
        cht = getchar();
        a[i][j] = (double)(cht - '0');  
       // printf("a[i][j] = %lf\n", a[i][j]);
        sx[i][j] = a[i][j] * i;
        sy[i][j] = a[i][j] * j;   
      }
      scanf("\n");
    }
    
    memset(sumx,0,sizeof(sumx));
    memset(mymass,0,sizeof(mymass));
    memset(sumy,0,sizeof(sumy));
    for(int i = 1; i <= n; i++)
      for(int j = 1; j <= m; j++) {
        double t_sumx = a[i][j] * i;
        double t_sumy = a[i][j] * j;
        double t_mass = a[i][j];
        sumx[i][j] = sumx[i-1][j] + sumx[i][j-1] - sumx[i-1][j-1] + t_sumx;
        sumy[i][j] = sumy[i-1][j] + sumy[i][j-1] - sumy[i-1][j-1] + t_sumy;
        mymass[i][j] = mymass[i-1][j] + mymass[i][j-1] - mymass[i-1][j-1] + t_mass;        
      }
      
      
   // printf("sumx[5][5] = %lf, sumy[5][5] = %lf, mymass[5][5] = %lf\n", sumx[5][5], sumy[5][5], mymass[5][5]);
      
    ans = 2;
    for(int i = 1; i <= n; i++)
      for(int j = 1; j <= m; j++)
        for(int k = ans+1; i+k-1 <= n && j+k-1 <= m; k++) {
          int i2 = i+k-1, j2 = j+k-1;
          double tot_mass = mymass[i2][j2] - mymass[i-1][j2] - mymass[i2][j-1] + mymass[i-1][j-1]
          - a[i][j] - a[i][j2] - a[i2][j] - a[i2][j2];
          //double avr_mass = tot_mass / (k*k-4);
          
          double sumx_mass = sumx[i2][j2] - sumx[i-1][j2] - sumx[i2][j-1] + sumx[i-1][j-1] 
                  - sx[i][j] - sx[i][j2] - sx[i2][j] - sx[i2][j2];  
                  
          double sumy_mass = sumy[i2][j2] - sumy[i-1][j2] - sumy[i2][j-1] + sumy[i-1][j-1] 
                  - sy[i][j] - sy[i][j2] - sy[i2][j] - sy[i2][j2];                  
                      
          double ci = 0.5 * (i + i + k - 1), cj = 0.5 * (j + j + k - 1);
          
        //  printf("sumx_mass = %lf, sumy_mass = %lf, tot_mass = %lf, ci = %lf, cj = %lf\n", sumx_mass, sumy_mass, tot_mass, ci, cj);
          
          if (cmp(sumx_mass - tot_mass * ci) == 0 && cmp(sumy_mass - tot_mass * cj) == 0) {
            if (k > ans) ans = k;                  
          }
                           
        }
        
    printf("Case #%d: ", ctn);
    if (ans < 3) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
          
  }   
  
  return 0;
    
}
