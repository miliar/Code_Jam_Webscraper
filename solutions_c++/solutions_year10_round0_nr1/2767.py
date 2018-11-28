//  
// build via command line:
// g++ task.cpp -o task
//
// to run program:
// ./task A-task-data
//
// compiler version: gcc version 4.4.3 (Ubuntu 4.4.3-4ubuntu5)
// 
// Coded by bearded
//

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char* argv[]) {
  string filename(argv[1]);
  string outfile = filename + ".out";
  string infile = filename + ".in";
  ifstream in(infile.c_str());
  ofstream out(outfile.c_str());

  int t;
  in >> t;

  for (int i=1; i<=t; i++) {
    int n;
    int k;
    in >> n >> k;

    int powered = pow(2, n);
    bool state = ((k+1) % powered == 0);
    out << "Case #" << i << ": " << (state ? "ON" : "OFF") << endl;
  }

  return 0;
}
