#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    int n;
    scanf("%d", &n);
    vector <string> mat;
    for(int i = 0; i < n; i++) {
      char buf[64];
      scanf(" %s", buf);
      mat.push_back(buf);  
    }
    int cnt = 0;
    for(int i = 0; i < n; i++) {
      int j = i;
      for(j = i; j < n; j++) {
        int good = 1;
        for(int k = i + 1; k < n; k++) if(mat[j][k] == '1') good = 0;
        if(good) break;
      }
      if(i == j) continue;
      for(int k = j; k > i; k--) { cnt++; swap(mat[k], mat[k - 1]); }
    }
    
    printf("Case #%d: %d\n", case_cnt++, cnt);
  }
  
      
  return 0;
}
  

