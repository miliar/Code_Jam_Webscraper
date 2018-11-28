/*
ID: Plagapong
LANG: C++
TASK: swinging
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#define INF 999999999

using namespace std;
int garbage;
int n;
int d[10005], l[10005];
int dd;
int g[10005];

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  for (int i = 0; i < 10005; i++) {
    g[i] = -1;
  }
}

void process() {
  // Code here!
  garbage = scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    garbage = scanf("%d%d", &d[i], &l[i]);
  }
  garbage = scanf("%d", &dd);
  // Dynamic
  g[0] = d[0];
  for (int i = 1; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (d[i] - d[j] <= g[j]) {
        g[i] = max(g[i], min(l[i], d[i] - d[j]));
      }
    }
  }
  //for (int i = 0; i < n; i++) printf("%d ", g[i]);
  for (int i = 0; i < n; i++) {
    if (dd - d[i] <= g[i]) {
      printf("YES");
      return;
    }
  }
  printf("NO");
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}
