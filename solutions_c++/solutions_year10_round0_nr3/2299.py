#include <iostream>
#include <queue>

#define MAX_R 100000000
#define MAX_k 1000000000
#define MAX_N 1000
#define MAX_g 10000000

using namespace std;

unsigned T, R, k, N;
//unsinged groups[MAX_N];

int main () {
  cin >> T;
  for(unsigned t = 1; t <= T; ++t) {
    queue<unsigned> Q;

    cin >> R >> k >> N;

    for(unsigned g = 0; g < N; ++g) {
      unsigned aux;
      cin >> aux;
      Q.push(aux);
    }
    
    unsigned profits = 0;
    for(unsigned r = 0; r < R; ++r) {
      unsigned people = 0, gr = 0;
      while ((people + Q.front()) <= k && gr < N) {
	people += Q.front();
	++gr;
	Q.push(Q.front());
	Q.pop();
      }
      profits += people;
    }

    cout << "Case #" << t << ": " << profits << endl;
    
    
  }
}
