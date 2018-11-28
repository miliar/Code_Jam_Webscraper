#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  unsigned T = 0;
  ifs >> T;

  for (unsigned t = 0; t < T; ++t) {
    unsigned N = 0;
    ifs >> N;
    unsigned sec = 0;
    unsigned oldPosB = 1;
    unsigned oldPosO = 1;
    unsigned oldSecB = 0;
    unsigned oldSecO = 0;
    for (unsigned n = 0; n < N; ++n) {
      char R;
      unsigned P;
      ifs >> R;
      ifs >> P;
      int posDiff = 0;
      int secDiff = 0;
      if ('B' == R) {
        posDiff = (P > oldPosB) ? (P - oldPosB) : (oldPosB - P);
        secDiff = sec - oldSecB;
        sec += (secDiff > posDiff) ? 0 : posDiff - secDiff;
        ++sec;
        oldPosB = P;
        oldSecB = sec;
      } else {
        posDiff = (P > oldPosO) ? (P - oldPosO) : (oldPosO - P);
        secDiff = sec - oldSecO;
        sec += (secDiff > posDiff) ? 0 : posDiff - secDiff;
        ++sec;
        oldPosO = P;
        oldSecO = sec;
      }
    }

    ofs << "Case #" << t + 1 << ": " << sec << endl;
  }


return 0;
}
