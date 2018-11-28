#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std; 

const int MAXN = 110; 
const int MAXT = 32; 

int n, sn, thres; 
int a[MAXN]; 
bool sur[MAXT], unsur[MAXT]; 

int solve(){
  int f[MAXN][MAXN]; 
  
  memset(f, 0, sizeof(f)); 
  for (int i = 1; i<=n; ++i) {
    int high = a[i]/3+(a[i]%3!=0); 
    for (int j = 0; j<=i && j<=sn; ++j) 
      f[i][j] = f[i-1][j]+(high>=thres);
    switch (a[i]%3){
    case 0:
    case 1:
      high = a[i]/3+1; 
      break; 
    case 2:
      high = a[i]/3+2; 
    }
    for (int j = 1; j<=i && j<=sn; ++j) 
      f[i][j] = max(f[i][j] , f[i-1][j-1]+(high>=thres && high<=10 && a[i]>=2)); 
  }
  return f[n][sn]; 
}

int main(){
  int T; 
  scanf("%d", &T); 

  for (int i = 1; i<=T; ++i) {
    scanf("%d%d%d", &n, &sn, &thres); 
    for (int j = 1; j<=n; ++j) 
      scanf("%d", &a[j]); 
    printf("Case #%d: %d\n", i, solve()); 
  }
  return 0; 
}
