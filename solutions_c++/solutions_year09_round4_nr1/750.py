#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

string getLine() {
  string s;
  while (!feof(stdin)) {
    char c = fgetc(stdin);
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
  }
  return s;
}

int getNum() {
    string s = getLine();
    return atoi(s.c_str());
}

int main() {
  int count=0;
  int T=getNum();

  while(T--) {
    int N=getNum();
    int x[40];
    for (int n=0;n<N; n++) {
      string s = getLine();
      x[n] = -1;
      for (int i=N-1;i>=0;i--) {
        if (s[i] == '1') {
          x[n] = i;
          break;
        }
      }
    }
    
    int answer=0;
    /*
      for (int i = 0; i < N; i++) {
        printf ("%d ", x[i]);
      }
      printf("\n");
    */
    for (int n=0;n<N;n++) {
      if (x[n] <= n) continue;
      
      for (int i=n;i<N;i++) {
        if (x[i] > n) continue;
        int tmp = x[i];
        for (int j = i; j > n; j--) {
          x[j] = x[j-1];
          answer++;
        }
        x[n] = tmp;
        break;
      }
/*
      for (int i = 0; i < N; i++) {
        printf ("%d ", x[i]);
      }
      printf("\n");
    */
    }
    
    printf("Case #%d: %d\n", ++count, answer);
  }
  return 0;
}
