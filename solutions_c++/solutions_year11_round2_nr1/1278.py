#include <iostream>
#include <map>
#include <vector>
#include <string.h>

#define FFF(i, s, x) for (int i = s; i < x; ++i)
#define FF(i, x) FFF(i, 0, x)
#define MMM(i, s) memset(i, s, sizeof(i));

char B[150][150];
long WP[150];
long WPN[150];

double OWP[150];
double OOWP[150];

using namespace std;

int main() {
  int T;
  cin >> T;

  FF(i, T) {

    MMM(B, 0);
    MMM(WP, 0);
    MMM(WPN, 0);
    MMM(OWP, 0);
    MMM(OOWP, 0);

    int N;
    cin >> N;
    
    FF(j, N) {
      FF(k, N) {
        char c;
        cin >> c;
        B[j][k] = c;
      }
    }

    FF(j, N) {
      FF(k, N) {
        if (B[j][k] == '.')
          continue;
        ++WPN[j];
        if (B[j][k] == '1')
          ++WP[j];
      }
    }

    FF(j, N){
      FF(k, N) {
        if (B[j][k] == '.')
          continue;
        long s = (B[j][k] == '1') ? WP[k] : (WP[k] - 1);
        OWP[j] += (double(s) / (WPN[k] - 1)) / WPN[j];
      }
    }
    
    FF(j, N){
      FF(k, N) {
        if (B[j][k] == '.')
          continue;
        OOWP[j] += OWP[k] / WPN[j];
      }
    }    

    cout << "Case #" << i + 1 << ":" << endl;
    FF(j, N) {
      cout << 0.25*WP[j]/WPN[j] + 0.5*OWP[j] + 0.25*OOWP[j] << endl;
    }
    
  }
}
