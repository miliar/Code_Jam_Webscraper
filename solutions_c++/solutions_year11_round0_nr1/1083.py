#include <iostream>
#include <map>

using namespace std;

int myabs(int a) {
  return (a<0)?-a:a;
}
int main() {
  int T;
  cin >> T;
  
  int N;

  char R[105];
  int P[105];
  int minicost[105];

  P[0] = 1;
  minicost[0] = 0;

  int lastPosition[2] = {0,0}; // 0 for 'O' and 1 for 'B'
  
  for(int t = 1; t <= T; t++) {
    cin >> N;
    lastPosition[0] = lastPosition[1] = 0; // other variables will be recauculate on the way 
    for(int i = 1; i<=N; i++) {
      cin >> R[i] >> P[i];
    }
    for(int i = 1; i<= N; i++) {
      if (i==1) {
        minicost[i] = P[i];
        lastPosition[R[i]=='O'?0:1] = i;
      } else if (R[i] == R[i-1]) {
        // has the same color as previous button
        minicost[i] = minicost[i-1] + myabs(P[i]-P[i-1]) + 1;
        lastPosition[R[i]=='O'?0:1] = i;
      } else {
        // has different color from previous button,
        int lastp = lastPosition[R[i]=='O'?0:1];
        minicost[i] = max(minicost[i-1]+1,
                          minicost[lastp] + myabs(P[lastp]-P[i])+1);
        lastPosition[R[i]=='O'?0:1] = i;
      }
    }
    cout << "Case #" << t << ": " << minicost[N] << endl;    
  }
}
