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

#define MAX_N 2000

int arr[MAX_N], N;
bool vst[MAX_N];

int solve() {
    memset(vst, 0, sizeof(vst));
    int sum = 0;
    for (int i = 1; i <= N; i++) {
        if (!vst[i]) {
           int j = i;
           int k = 0;
           while (!vst[j]) {
                 vst[j] = true;
                 j = arr[j];      
                 k++;
           }         
           if (k > 1) {
              sum += k;      
           }    
        }
    }    
    return sum;
}

int main() {
    int T;
    freopen("C:\\setup\\in4.txt", "r", stdin);
    freopen("C:\\setup\\out4.txt", "w", stdout);
    int cse = 0;
    scanf("%d", &T);
    while (T--) {
          cse++;
          scanf("%d", &N);
          for (int i = 1; i <= N; i++) {
              scanf("%d", arr + i);    
          }      
          int ret = solve();
          printf("Case #%d: %d.000000\n", cse, ret);
    }
    //system("pause");
    return 0;
}
