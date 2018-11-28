#include <cstdio>
#include <iostream>

int main()
{
  unsigned long long res, beg[1010];
  int t, r, k, n, g[1010], begin[1010], sub[1010];
  scanf("%i", &t);
  
  for(int T = 0; T < t; T++) {
    memset(begin, 0, sizeof(begin));
    memset(sub, 0, sizeof(sub));
    memset(beg, 0, sizeof(beg));
    scanf("%i%i%i", &r, &k, &n);
    //sum = 0;
    for(int i = 0; i < n; i++) {
      scanf("%i", &g[i]);
      //sum += g[i];
    }
    
    /*
    if(sum < k) {
      printf("SUM < K!!!!!!!!!!!!!!!!!!!!!!!!!!");
      fflush(stdout);
      while(1);
    }//*/
    
    res = 0;
    int cur = 0, it = 0, i = 0;
    
    /* test 
    while(it < r) {
      cur = 0;
      int first = i;
      while((cur == 0 || first != i) && cur + g[i] <= k) {
        cur += g[i];
        i++;
        i %= n;
      }
      res += cur;
      //std::cout << "res: " << res << std::endl;
      it++;
    }
    unsigned long long realRes = res;*/
    
    res = 0;
    cur = it = i = 0;
    
    while(!begin[i]) {
      begin[i] = 1;
      sub[i] = it;
      beg[i] = res;
      int first = i;
      if(it == r) break;
      cur = 0;
      while((cur == 0 || first != i) && cur + g[i] <= k) {
        cur += g[i];
        i++;
        i %= n;
      }
      res += cur;
      //std::cout << "res: " << res << std::endl;
      it++;
    }
    if(r != it) {
      r -= it;
      res = (res - beg[i]) * (r / (it - sub[i])) + res;
      r = r % (it - sub[i]);
    } else r = 0;
    //std::cout << "res: " << res << std::endl;
    //printf("sub: %i\n", sub[i]);
    //printf("r: %i, it: %i\n", r, it);
    it = 0;
    while(it < r) {
      cur = 0;
      int first = i;
      while((cur == 0 || first != i) && cur + g[i] <= k) {
        cur += g[i];
        i++;
        i %= n;
      }
      res += cur;
      //std::cout << "res: " << res << std::endl;
      it++;
    }
    std::cout << "Case #" << T + 1 << ": " << res << std::endl;
        /* test 
    if(res != realRes) {
      printf("HERE!!!!!!!!!!!!!!!");
      std::cout << realRes << std::endl;
      std::cout.flush();
      while(1);
    } //*/
  }
}
