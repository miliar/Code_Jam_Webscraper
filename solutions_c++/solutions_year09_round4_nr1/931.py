#include <iostream>
#include <string>
#include <limits>
using namespace std;

int T,N;
int last[40];

int main(int argc, char *argv[]) {
  int numswaps, toswap, tmp;
  char ch;
  int k;
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    numswaps = 0;
    cin >> N >> ws;
    for(int i=0; i<N; i++) {
      last[i] = -1;
      cin >> ws;
      for(int j=0; j<N; j++) {
        cin >> ch;
        if(ch == '1') last[i] = j;
      }
    }
    
    while(true) {
      toswap = -1;
      for(int i = 0; i<N; i++) {
        if(last[i] > i) {
          toswap = i;
          break;
        }
      }
      if(toswap == -1) break;      
      for(int i = toswap+1; i<N; i++) {
        if(last[i] <= toswap) {
          k = i;
          break;
        }
      }

      tmp = last[k];
      last[k] = last[k-1];
      last[k-1] = tmp;
      numswaps++;
    }
    cout << "Case #" << t << ": " << numswaps << endl;
  }
  return 0;
}
