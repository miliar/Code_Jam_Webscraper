#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int is_prime(int x)
{
  if(x < 2) return 0;
  for(int i = 2; i * i <= x; i++) if(x % i == 0) return 0;
  return 1;
}

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    int d, k;
    scanf("%d %d", &d, &k);
    vector <int> nums;
    for(int i = 0; i < k; i++) {
      int x;
      scanf("%d", &x);
      nums.push_back(x);
    }
    int p10 = 1;
    for(int i = 0; i < d; i++) p10 *= 10;
    
    int A = -1;
    int B = -1;
    int P = -1;
    set <int> used;
    vector <int> next;
    for(int i = 2; i <= p10; i++) {
      if(k == 1) continue;
      if(!is_prime(i)) continue;
      int flag = 0;
      for(int j = 0; j < k; j++) if(nums[j] >= i) { flag = 1; continue; }
      if(flag) continue;
      for(int a = 0; a < i; a++) {
        int b = nums[1] - a * nums[0];
        b = (b % i + i) % i;
        int good = 1;
        for(int j = 1; j < k; j++) {
          if((nums[j - 1] * a + b) % i != nums[j]) { good = 0; break; }
        }
        if(good) {
          A = a;
          B = b;
          P = i;
          used.insert((nums.back() * A + B) % P);
        }
        if(used.size() > 1) break;
      }
      if(used.size() > 1) break;
    }
    
    if(used.size() != 1) {
      printf("Case #%d: I don't know.\n", case_cnt++);
    }
    else {
      printf("Case #%d: %d\n", case_cnt++, (nums.back() * A + B) % P);
    }
  }
    
  return 0;
}

