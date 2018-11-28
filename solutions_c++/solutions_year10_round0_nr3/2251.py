#include <windows.h>
#include <limits.h>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

typedef long      unsigned int li;
typedef long long unsigned int lli;

struct DynamicNode {
  li  cost;
  int next;
};

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

  li T,R,k,N;
  li groups[1000];
  li next_group;
  li free_seats;
  li first_group_on_roller;

  lli total_cash;

  DynamicNode nodes[1000];

clock_t t0 = clock();
clock_t now;

  iFile >> T;
  for (li t = 1; t <= T; ++t) {

now = clock();
printf("T %ld/%ld : %f\n",t,T,((double)(now - t0))/(double)CLOCKS_PER_SEC);

    iFile >> R >> k >> N;
    for (li n = 0; n < N; ++n) {
      iFile >> groups[n];
      nodes[n].next = -1;
    }

    total_cash = 0;
    next_group = 0;

    while (R > 0) {
      free_seats            = k;
      first_group_on_roller = next_group;

      DynamicNode* node = &nodes[next_group];
      if (node->next == -1) {
        do {
          free_seats -= groups[next_group];
          next_group = (next_group + 1)%N;
        } while ((free_seats >= groups[next_group]) && (first_group_on_roller != next_group));

        node->next = next_group;
        node->cost = k - free_seats;
      }
      else
        next_group = node->next;

      total_cash += node->cost;

      --R;
    }

    oFile << "Case #" << t << ": " << total_cash << endl;
  }

  iFile.close();
  oFile.close();

  return 0;
}
