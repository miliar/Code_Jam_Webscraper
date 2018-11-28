#include <fstream>
#include <iostream>
#include <list>
using namespace std;

typedef long unsigned int li;

struct Snapper {
  bool state;
  bool powered;

  Snapper(void) {
    state = powered = false;
  }
};
typedef list<Snapper> Snappers;


void snap(Snappers& snappers) {
  bool has_power = true;
  Snappers::iterator itr;
  for (itr = snappers.begin(); itr != snappers.end(); ++itr) {

    if (itr->powered)
      itr->state = !itr->state;

    itr->powered = has_power;

    if (!itr->state)
      has_power = false;
  }
}

bool check_lamp(Snappers& snappers) {
  Snappers::const_iterator itr;
  for (itr = snappers.begin(); itr != snappers.end(); ++itr) {
    if (!itr->state || !itr->powered)
      return false;
  }

  return true;
}

int main(int argc, char** argv){

  if (argc != 2) {
    cerr << "Input file missing!" << endl;
    return 0;
  }

  ifstream iFile;
  iFile.open(argv[1]);
  if (!iFile.is_open()) {
    cerr << "Failed to open input file!" << endl;
    return 0;
  }

  ofstream oFile;
  oFile.open("out.txt");
  if (!oFile.is_open()) {
    cerr << "Failed to open output file!" << endl;
    return 0;
  }

  li T,N,K;
  iFile >> T;

  for (li t = 1; t <= T; ++t) {

    iFile >> N >> K;

    // Connecte Snappers
    Snappers snappers;
    for (li n = 0; n < N; ++n)
      snappers.push_back(Snapper());
    snappers.begin()->powered = true;  // plug the first in the socket

    for (li k = 0; k < K; ++k) {
      snap(snappers);
    }

    oFile << "Case #" << t << ": " << ((check_lamp(snappers)) ? ("ON") : ("OFF")) << endl;
  }

  iFile.close();
  oFile.close();

  return 0;
}
