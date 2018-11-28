/*
 * Google code jam 2010 / Qualification round 
 * Task A: Snapper Chain
 *
 * Created by Krisztian Balog on 5/8/10.
 */

#include <iostream>
using namespace std;

void changestate(long& state) {
  
}

int main(int argc, char* argv[]) {

  int T = 0;
  cin >> T;
  
  for (int i=0;i<T;i++) {
    long K;
    int N;
    
    cin >> N;
    cin >> K;
    
    // init 
    unsigned long state = 0;
    unsigned long all_on = 1;
    for (int j=1;j<N;j++)
      all_on = (all_on << 1) | 1;
        
    // this could be done in a smarter way, but it's good enough for now ;)
    for (long j=0;j<K;j++) {
      state++;
      if (state > all_on) state = 0;
    }
    
    // output
    cout << "Case #" << (i+1) << ": ";
    if (state == all_on) cout << "ON";
    else cout << "OFF";
    cout << endl;
  }
    
  return 0;
}
