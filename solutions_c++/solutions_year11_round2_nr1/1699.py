#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

//#define DEBUG

void doTest(int t) {
  int N;
  char ch;
  scanf("%d", &N);
  getchar();
#ifdef DEBUG
      cerr << "N = " << N << endl;
#endif
  char ARR[N][N];
  int numWon[N];
  int numPlayed[N];
  double WP[N];
  double OWP[N];
  double OOWP[N];
  for (int n=0; n<N; ++n) {
    numWon[n] = 0; numPlayed[n] = 0;
    for (int nn=0; nn<N; ++nn) {
      scanf("%c", &ch);
      ARR[n][nn] = ch;
#ifdef DEBUG
      cerr << n << "," << nn << " = " << ch << endl;
#endif
      if (ch == '1') {
        ++numWon[n];
      }
      if (ch != '.') {
        ++numPlayed[n];
      }
    }
    getchar();
  }

  cout << "Case #" << t << ":" << endl;
  for (int n=0; n < N; ++n) {
     WP[n] = numWon[n] / (double)numPlayed[n];
#ifdef DEBUG
     cerr << n << ": #Won = " << numWon[n] << " #played = " << numPlayed[n] << " WP = " << WP[n] << endl;
#endif
     OWP[n] = 0.0;
     for (int nn=0; nn < N; ++nn) {
       if (n == nn) continue;
       if (ARR[n][nn] == '.') continue;
       int allExMe = (ARR[nn][n] == '1') ? numWon[nn]-1:numWon[nn];
       OWP[n] += allExMe/(double)(numPlayed[nn]-1);
     }
     OWP[n] /= numPlayed[n];
#ifdef DEBUG
    cerr << " OWP = " << OWP[n] << endl;
#endif
  }

  for (int n=0; n < N; ++n) {
     OOWP[n] = 0.0;
     for (int nn=0; nn < N; ++nn) {
       if (n == nn) continue;
       if (ARR[n][nn] == '.') continue;
       OOWP[n] += OWP[nn];
     }
     OOWP[n] /= numPlayed[n];
#ifdef DEBUG
    cerr << " OOWP = " << OOWP[n] << endl;
#endif
     printf("%0.12lg\n", 0.25 * WP[n] + 0.5 * OWP[n] + 0.25 * OOWP[n]);
  }
}

int main() {
  int T;
  scanf("%d", &T);
  
  for (int t=1; t<=T; ++t) {
     doTest(t);
  }
  return 0;
}

