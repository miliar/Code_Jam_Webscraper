#include <iostream>
#include <cstring>
#include <set>

using namespace std;



inline int checkCycles(int n, int a, int b) {
  set <pair<int, int> > S;
  S.clear();
  int len = 0;
  int j = 0;
  int cyc = n;
  int N = n;
  int pow = 1;
  if (n < 10000) {
    if (n < 100) {
      if (n < 10) {
        pow = 1;
        len = 1;
      } else {
        pow = 10;
        len = 2;
      }
    } else {
      if (n < 1000) {
        pow = 100;
        len = 3;
      } else {
        pow = 1000;
        len = 4;
      }
    }
  } else {
    if (n < 1000000) {
      if (n < 100000) {
        pow = 10000;
        len = 5;
      } else {
        pow = 100000;
        len = 6;
      }
    } else {
      pow = 1000000;
      len = 7;
    }
  }
//  do {
//    n /= 10;
//    if (n) pow *= 10;
//    len++;
//  } while (n);
  int l = 0;
  for (int i = 0; i < len - 1; i++) {
    l = cyc % 10;
    cyc /= 10;
    cyc += pow * l;
    if (N < cyc && cyc <= b) {
      S.insert(make_pair(N, cyc));
    }
  }
  return S.size();
}

int main() {
//  int time = clock();  
  int nrTest;
  scanf("%d\n", &nrTest);

  for (int testcase = 1; testcase <= nrTest; testcase++) {
    int a, b;
    int ans = 0;
    scanf("%d%d\n", &a, &b);
    for (int i = a; i <= b; i++) {
      ans += checkCycles(i, a, b);
    }

    printf("Case #%d: %d\n", testcase, ans);
    
  }
//  printf("time = %d\n", clock() - time);
    
 
  return 0; 
}
