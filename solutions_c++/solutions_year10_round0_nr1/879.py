#include<iostream>
#include<cstdio>
using namespace std;

#define MAXN 100000005
int a[MAXN];

void printbin(int x) {
  for (int i = 0; i < 31; i++) {
    if (x & (1<<i)) {
      cout << '1';
    }
    else cout << ' ';
  }
  cout << endl;
}

int main() {
  int p2[32];
  for (int i = 0; i < 32; i++) {
    p2[i] = (1<<i);
  }
  a[0] = 0;
  for (int i = 1; i < MAXN; i++) {
    int mask = 0;
    int j;
    for (j = 0; j < 31 && (p2[j] & a[i-1]) ; j++) {
      mask |= p2[j];
    }
    mask |= p2[j];
    a[i] = mask ^ a[i-1];
  }
  
  if (false) {
  for (int i = 0; i < 100; i++) {
    printbin(a[i]);
  }
  return 0;
  }
  
  int ncase, n, k;
  cin >> ncase;
  for (int i = 1; i <= ncase; i++) {
    cin >> n >> k;
    printf("Case #%d: ", i);
    int j;
    for (j = 0; j < n; j++) {
      if (! ( p2[j] & a[k])) break;
    }
    if ( j == n ) cout << "ON\n";
    else cout << "OFF\n";
  }
  return 0;
}
