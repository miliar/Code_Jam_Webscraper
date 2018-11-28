#include <cstdio>
#include <map>

using namespace std;

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    int n;
    scanf("%d", &n);
    map <int, int> x;
    for(int i = 0; i < n; i++) {
      int a, b;
      scanf("%d %d", &a, &b);
      x[a] += b;
    }
    
    int cnt = 0;
    for( ; ; ) {
      int found = 0;
      for(map <int, int>::iterator it = x.begin(); it != x.end(); it++) {
        int a = it->first;
        int b = it->second;
        if(b > 1) {
          cnt += b / 2; 
          found = 1;
          x[a] %= 2;
          x[a - 1] = x[a - 1] + b / 2;
          x[a + 1] = x[a + 1] + b / 2;
          break;
        }
      }
      if(!found) break;
    }
    
    printf("Case #%d: %d\n", case_cnt++, cnt);
  }
    
  return 0;
}

