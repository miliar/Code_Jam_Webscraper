#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int T;
    freopen("C:\\setup\\in3.txt", "r", stdin);
    freopen("C:\\setup\\out3.txt", "w", stdout);
    scanf("%d", &T);
    int cse = 0;
    while (T--) {
          cse++;
          int n;
          scanf("%d", &n);
          int sum = 0;
          int mn = 1000000000;
          int res = 0;
          for (int i = 0; i < n; i++) {
              int x;
              scanf("%d", &x);
              sum += x;
              if (x < mn) {
                 mn = x;
              }    
              res ^= x;
          }
          if (res != 0) {
             printf("Case #%d: NO\n", cse);        
          } else {
             printf("Case #%d: %d\n", cse, sum - mn);
          }
    }
    //system("pause");
    return 0;    
}
