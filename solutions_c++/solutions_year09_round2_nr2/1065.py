#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <functional>
#include <deque>
#include <numeric>
#include <map>
#include <list>

using namespace std;

#define PI 3.14159265358979323846264338327950288

typedef long long int64;
typedef unsigned long long uint64;
typedef struct tag_point { int x, y; } POINT;

int solve();

// #define WIDTH  
// #define HEIGHT 

int c;

int max_v(vector<int> v, int a, int b) {
  int max = 0;
  for (int i = a; i < b; i++) {
    if (max < v[i]) max = v[i];
  }
  return max;
}



main() {
  using namespace std;
  int qsn_num, line_num, loop_cnt;
  
  scanf("%d\n", &qsn_num);

  for (loop_cnt = 1; loop_cnt <= qsn_num; loop_cnt++) {
    char buf[1000];
    scanf("%s\n", buf);
    int size = strlen(buf);
    vector<int> v(1000);

    for (int i = 0; i < size; i++) v[size - i - 1] = buf[i] - '0';    
//    for (int i = 10; i >= 0; i--) { printf("%d", v[i]); } printf("\n");

    for (int i = 1; i <= size; i++) {
//printf("max:%d\n", max_v(v, 0, i+1));
      if (max_v(v, 0, i+1) != v[i]) {
        int cnt = 0;
        int mn = 10;
        for (int j = 0; j < i; j++) {
          if (v[i] < v[j] && v[j] < mn) {
            mn = v[j];
            cnt = j;
          }
        }
        swap(v[i], v[cnt]);
        
        sort(v.begin(), v.begin() + i, greater<int>());
        
        break;
      }
    }


    // solve();

    int flag = 0;
    printf("Case #%d: ", loop_cnt);
    for (int i = 600; i >= 0; i--) { 
      if (flag == 0 && v[i] == 0) continue;
      flag = 1;
      printf("%d", v[i]);
    } 
    printf("\n");
  }
}

int solve() {
  int i, j;



}



