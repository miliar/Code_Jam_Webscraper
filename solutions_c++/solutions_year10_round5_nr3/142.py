#include <iostream>
using namespace std;

const int MAXP = 4000000;
int vendors[MAXP];
int T,C,P,V;

int main(int argc, char *argv[]) {
  int count, j;
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    for(int i=0; i<MAXP; i++) {
      vendors[i] = 0;
    } 
    count = 0;
    cin >> C >> ws;
    for(int i=0; i<C; i++) {
      cin >> P >> V;
      vendors[P+2000000] = V;
    }

    j = 0;
    while(j < MAXP) {
      if(vendors[j] <= 1) {
        j++;
      } else {
        vendors[j] -= 2;
        vendors[j-1]++;
        vendors[j+1]++;
        count++;
        j--;
      }
    }
    cout << "Case #" << t << ": " << count << endl;
  }

  return 0;
}
