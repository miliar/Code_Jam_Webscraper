#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int a[1000], b[1000], N;
    cin >> N;
    for (int n = 0; n < N; n++) 
      cin >> a[n];
    memset(b, 0, sizeof(b));
    int start = 0;
    int total = 0;
    while (start < N) {
      if (b[start] == 1) {
        start++;
        continue;
      }
      
      int next = a[start] - 1;
      b[start] = 1;
      int length = 1;
      while (next != start) { 
        b[next] = 1;
        next = a[next] - 1;
        length++;
      }
      total += length == 1? 0 : length;
      start++;
    }
    printf("Case #%d: %.6f\n", t + 1, (float)total); 
      
  }  
  
  return 0;
}


