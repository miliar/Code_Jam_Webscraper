/*
ID: Plagapong
LANG: C++
TASK: game
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#define INF 999999999

using namespace std;
int n;
int l[1005];
int p[1005];
int q[1005];
int ans[1005];

bool comparez(int a, int b) {
  if (l[a] * p[b] == l[b] * p[a]) {
    return a < b;
  }
  return l[a] * p[b] < l[b] * p[a];
}

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  
}

void process() {
  // Code here!
  int garbage = scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    garbage = scanf("%d", &l[i]);
    ans[i] = i;
  }
  for (int i = 0; i < n; i++) {
    garbage = scanf("%d", &p[i]);
    q[i] = 1 - p[i];
  }
  // Small
  sort(ans, ans + n, comparez);
  for (int i = 0; i < n; i++) {
    printf("%d", ans[i]);
    if (i != n-1) printf(" ");
  }
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
