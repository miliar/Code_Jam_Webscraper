#include <iostream>
#include <cmath>
using namespace std;

const int MAXP = 100002;
bool prime[MAXP];
int output[11];
int T,D,K;

int main(int argc, char *argv[]) {
  int foo, b, guess, newguess, maxi;
  bool ok;
  for(int i=2;i<MAXP;i++) {
    prime[i] = true;
    for(int j=2;j<(int) (sqrt(i)+1); j++) {
      if(i % j == 0) {
        prime[i] = false;
        break;
      }
    }
  }

  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    guess = -1;
    cin >> D >> K;
    for(int k=0; k<K; k++) {
      cin >> output[k];
    }

    if(K <= 1) {
      cout << "Case #" << t << ": I don't know." << endl;
      continue;
    }

    maxi = (int) pow((double) 10, (double) D);
    for(int i=2; i<maxi; i++) {
      if(prime[i]) {
        ok = true;
        for(int k=0; k<K; k++) {
          if(output[k] >= i) ok=false;
        }
        if(!ok) continue;
        for(int a=0; a<i; a++) {
          foo = (output[0] * a) % i;
          b = output[1] - foo;
          if(b<0) b+=i;
          ok = true;
          for(int k = 1; k < K-1; k++) {
            foo = (output[k] * a + b) % i;
            if(foo != output[k+1]) {
              ok = false;
              break;
            }
          }
          if(ok) {
            newguess = (output[K-1] * a + b) % i;
            if(guess == -1 || newguess == guess) {
              guess = newguess;
            } else {
              guess = -2;
            }
          }
        }
      }
    }

    if(guess >= 0) {
      cout << "Case #" << t << ": " << guess << endl;
    } else {
      cout << "Case #" << t << ": I don't know."  << endl;
    }
  }

  return 0;
}
