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
#include <vector>

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
    int r;
    int k;
    int n;
    in >> r >> k >> n;

    vector<int> v(n);
    for (int j=1; j<=n; j++) {
        in >> v[j-1];
    }

    int queue = 0;
    long money = 0;
    for (int j=1; j<=r; j++) {
        int sits = 0;
        int queuestart = queue;
        while (sits + v[queue] <= k) {
            sits += v[queue];
            if (queue == n-1) {
                queue = 0;
            } else {
                queue++;
            }
            if (queue == queuestart)
                break;
        }
        money += sits;
    }

    out << "Case #" << i << ": " << money << endl;
  }

  return 0;
}
