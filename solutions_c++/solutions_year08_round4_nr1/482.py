#include <iostream>
#include <cstdio>

using namespace std;

int a[10000][4];

void foo(int idx) {
  int M, V;
  scanf("%d%d", &M, &V);

  for(int i = 0; i < (M-1)/2; ++i) {
    scanf("%d%d", &a[i][0], &a[i][1]);
    a[i][2] = 20000;
    a[i][3] = 20000;
  }
  for(int i = (M-1)/2; i < M; ++i) {
    scanf("%d", &a[i][0]);
    if(a[i][0] == 0) {
      a[i][2] = 0;
      a[i][3] = -1;
    } else {
      a[i][2] = -1;
      a[i][3] = 0;

    }
  }

  int T = (M-1)/2;

  for(int i = T-1; i >= 0; --i) {
    int t1 = i * 2 + 1;
    int t2 = t1 + 1;
    // if AND
    if(a[t1][2] != -1 and a[t2][2] != -1) {
      a[i][2] = min(a[i][2], a[t1][2] + a[t2][2]);
    }

    if(a[t1][3] != -1 and a[t2][3] != -1) {
      a[i][3] = min(a[i][3], a[t1][3] + a[t2][3]);
    }
    if(a[t1][2] != -1 and a[t2][3] != -1) {
      if(a[i][0]) {
        a[i][2] = min(a[i][2], a[t1][2] + a[t2][3]);
      } else {
        a[i][3] = min(a[i][3], a[t1][2] + a[t2][3]);
      }

      if(a[i][1]) {
        a[i][2] = min(a[i][2], a[t1][2] + a[t2][3]+1);
        a[i][3] = min(a[i][3], a[t1][2] + a[t2][3]+1);
      }
    }


    if(a[t1][3] != -1 and a[t2][2] != -1) {
      if(a[i][0]) {
        a[i][2] = min(a[i][2], a[t1][3] + a[t2][2]);
      } else {
        a[i][3] = min(a[i][3], a[t1][3] + a[t2][2]);
      }

      if(a[i][1]) {
        a[i][2] = min(a[i][2], a[t1][3] + a[t2][2]+1);
        a[i][3] = min(a[i][3], a[t1][3] + a[t2][2]+1);
      }
    }

  }

  if(a[0][2+V] != 20000) {
    cout << "Case #" << idx << ": " << a[0][2+V] << "\n";
  } else {
    cout << "Case #" << idx << ": IMPOSSIBLE\n";
  }
}


int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    foo(i+1);
  }
}
