#include <climits>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;


typedef long unsigned int lui;

const char* inputFile  = "A-large.in";
const char* outputFile = "A-large.out";

int count_intersects(const vector<pair<int,int> >& wires, const int& N) {
  int count = 0;
  for (int n = 0; n < N - 1; ++n) {
    for (int i = n + 1; i < N; ++i) {
      if (wires[n].first < wires[i].first) {
        if (wires[n].second > wires[i].second)
          ++count;
      }
      else {
        if (wires[n].second < wires[i].second)
          ++count;
      }
    }
  }
  return count;
}

int main(int argc, char** argv) {

  ifstream iFile;
  iFile.open(inputFile);
  if (!iFile.is_open()) {
    cerr << "Failed to open input file!" << endl;
    return 0;
  }

  ofstream oFile;
  oFile.open(outputFile);
  if (!oFile.is_open()) {
    cerr << "Failed to open output file!" << endl;
    return 0;
  }

  clock_t t0 = clock();
  clock_t now;

  int T,N,A,B;
  vector<pair<int,int> > wires (1000);

  iFile >> T;
  for (int t = 1; t <= T; ++t) {

    iFile >> N;
    for (int n = 0; n < N; ++n) {
      iFile >> A >> B;
      wires[n] = make_pair(A,B);
    }

    oFile << "Case #" << t << ": " << count_intersects(wires,N) << endl;

    now = clock();
    printf("T %d/%d : %f\n",t,T,((double)(now - t0))/(double)CLOCKS_PER_SEC);
  }

  iFile.close();
  oFile.close();

  return 0;
}

