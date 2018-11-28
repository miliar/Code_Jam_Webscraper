#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 64

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    int n, k, b, T;
    scanf("%d %d %d %d", &n, &k, &b, &T);
    vector <int> x;
    vector <int> v;
    vector <int> ones;
    for(int i = 0; i < n; i++) {
      int a;
      scanf("%d", &a);
      x.push_back(a);
    }
    for(int i = 0; i < n; i++) {
      int a;
      scanf("%d", &a);
      v.push_back(a);
      if((b - x[i]) <= T * v[i]) ones.push_back(n - i - 1);
    }
    
    if(ones.size() < k) {
      printf("Case #%d: IMPOSSIBLE\n", case_cnt++);
    }
    else {
      int cnt = 0;
      int pos = 0;
      reverse(ones.begin(), ones.end());
      for(int i = 0; i < k; i++) {
        cnt += ones[i] - pos;
        pos++;
      }
      printf("Case #%d: %d\n", case_cnt++, cnt);
    }
  }
    
  return 0;
}



