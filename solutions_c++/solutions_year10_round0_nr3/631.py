#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())

#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)

const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

uint64_t R, k, N;
uint64_t euros, eurosPerUnit;
uint64_t peopleOnRide;
int nCases;
int i, j, gptr, lastgptr, ridesPerUnit;
uint32_t groups[1000];
bool beenHead[1000];
int loopHead;

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> nCases;
  for0n(i, nCases) {
    inFile >> R >> k >> N;
    euros = 0;
    gptr = 0;
    ridesPerUnit = 0;
    eurosPerUnit = 0;
    loopHead = -1;
    for0n(j,1000) {
      groups[j] = 0;
      beenHead[j] = false;
    }


    for0n(j, N) {
      inFile >> groups[j];
    }

    // Iterate over the rides. Count them until we get back to the start of
    // the queue. That's the unit of number of rides.
    for0n(j,R) {
      peopleOnRide = 0;
      lastgptr = gptr;
      if ((loopHead == -1) && beenHead[gptr] == true) {
        loopHead = gptr;
      }
      beenHead[gptr] = true;
      for (;;) {
        if (groups[gptr] + peopleOnRide <= k) {
          peopleOnRide += groups[gptr];

          gptr += 1;
          if (gptr == N) gptr = 0;
        }
        if ((lastgptr == gptr) || (groups[gptr] + peopleOnRide > k)) {
          // Send the ride.
          euros += peopleOnRide;
          if (loopHead != -1) {
            ridesPerUnit++;
            eurosPerUnit += peopleOnRide;
          }
          break;
        }
      }
      if (gptr == loopHead) {
        // We came back to the front. Divide the remaining rides by the unit size.
        uint32_t unitsLeft = (R - j - 1)/ridesPerUnit;
        cout << "Case #" << i+1 << " " << loopHead << " " << unitsLeft << endl;
        euros += eurosPerUnit * unitsLeft;
        j += ridesPerUnit * unitsLeft;
        loopHead = -2;
      }
    }
    outFile << "Case #" << i+1 << ": " << euros << endl;
  }

  outFile.close();
  return 0;
}
