
#include <iostream>
#include <cassert>
using namespace std;

int T, N;
int oPos, bPos, oTime, bTime;
int currentTime;

int main() {

  cin >> T;
  for (int t = 0; t < T; t++) {

    oPos = 1;
    bPos = 1;
    oTime = 0;
    bTime = 0;
    currentTime = 0;

    cin >> N;
    for (int i = 0; i < N; i++) {
      char bot;
      int move;
      cin >> bot >> move;

      int& pos = (bot == 'O') ? oPos : bPos;
      int& time = (bot == 'O') ? oTime : bTime;

      int dist = move - pos;
      if (dist < 0) dist = -dist;

      int dtime = currentTime - time;
      /*cout << "currentTime=" << currentTime <<
        " bot=" << bot << " move=" << move <<
        " pos=" << pos << " time=" << time << endl;
      */

      if (dist > dtime) {
        currentTime += dist - dtime;
      }
      currentTime++;

      time = currentTime;
      pos = move;

    }

    cout << "Case #" << t+1 << ": " << currentTime << endl;

  }

}

