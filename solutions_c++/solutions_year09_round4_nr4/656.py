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

int x[40],y[40],r[40];
double dist[40][40];

int main() {
  int count=0;
  int C=getNum();

  while(C--) {
    int N=getNum();
    for (int n=0;n<N; n++) {
      string s = getLine();
      sscanf(s.c_str(), "%d%d%d", &x[n], &y[n], &r[n]);
    }
    
    double dist_max = -1;
    double dist_min = -1;
    int i1 = 0;
    int i2 = 0;
    for (int i=0; i<N; i++) {
      for (int j=0; j<=i; j++) {
        dist[i][j] = sqrt(double((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]))) + r[i] + r[j];
        dist[j][i] = dist[i][j];
        if (i != j && (dist_min < 0 || dist_min > dist[i][j])) {
          dist_min = dist[i][j];
          i1 = i;
          i2 = j;
        }
      }
    }

    double answer;
    if (N == 1) {
      answer = dist[0][0]/2.0;
    } else if (N == 2) {
      if (dist[0][0] > dist[1][1]) {
        answer = dist[0][0]/2.0;
      } else {
        answer = dist[1][1]/2.0;
      }
    } else {
      answer = dist_min/2.0;
    }
    printf("Case #%d: %.6f\n", ++count, answer);
  }
  return 0;
}
