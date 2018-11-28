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


int cnt_uniq(char *a, int n) {
  int tbl[36];
  for (int i = 0; i < 36; i++) tbl[i] = 0;
  for (int i = 0; i < n; i++) {
    if ('a' <= a[i] && a[i] <= 'z') tbl[a[i]-'a']++;
    if ('0' <= a[i] && a[i] <= '9') tbl[a[i]-'0'+26]++;
  }
  int uniq = 0;
  for (int i = 0; i < 36; i++) {
    if (tbl[i] > 0) uniq++;
  }
  return uniq;
}

int asn(char a) {
  int ans = 0;
  if ('a' <= a && a <= 'z') ans = a-'a';
  if ('0' <= a && a <= '9') ans = a-'0'+26;
  return ans;
}

int64 pw(int a, int n) {
  int64 ans = 1;
  for (int i = 0; i < n; i++) {
    ans *= a;
  }
  return ans;
}

int get_ls(int *c) {
  for (int i = 0; i < 36; i++) {
    if (c[i] == 0) {
      c[i] = 1;
      return i;
    }
  }
}

main() {
  using namespace std;
  int qsn_num, line_num, loop_cnt;
  
  scanf("%d\n", &qsn_num);

  for (loop_cnt = 1; loop_cnt <= qsn_num; loop_cnt++) {
    char buf[1000];
    vector<int> d(1000);
    scanf("%s\n", buf);
    int size = strlen(buf);
    int ls[36]; for (int i = 0; i < 36; i++) { ls[i] = 0; }

    int base = cnt_uniq(buf, size);
    if (base == 1) base = 2;
    
    int tr[36]; for (int i = 0; i < 36; i++) { tr[i] = -1; }
    
    d[0] = 1;
    tr[asn(buf[0])] = 1;
    ls[1] = 1;

    for (int i = 1; i < size; i++) {
      if (tr[asn(buf[i])] != -1) {
        d[i] = tr[asn(buf[i])];
      } else {
        int count = get_ls(ls);
        tr[asn(buf[i])] = count;
        d[i] = count;
      }
    }
//for (int i = 0; i < 36; i++) { printf("%d:%d\n", i,tr[i]); }printf("\n");

    int64 answer = 0;
    for (int i = 0; i < size; i++) {
      answer += d[i] * pw(base, size - i - 1);
    }

    // solve();
//for (int i = 0; i < 10; i++) { printf("%d:%d\n", i,d[i]); }printf("\n");

    printf("Case #%d: ", loop_cnt);
    printf("%lld\n", answer);
  }
}

int solve() {
  int i, j;



}



