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

char line[50000];
int numcount[10];
int numarray[22];
int numToUse[10];

int i, j, k, l;
uint64_t ans;
int nCases;
int d, n;

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> nCases;
  cout << nCases << endl;
  for0n(i,nCases) {
    memset(numcount, 0, sizeof(numcount));
    memset(numToUse, 0, sizeof(numToUse));
    memset(numarray, 0, sizeof(numarray));
    ans = 0;
    uint64_t number, temp = 0, total = 0;
    inFile >> number;
    cout << "Case " << i + 1 << ": " << number << endl;

    temp = number;
    while(temp) {
      numarray[total]=temp%10;
      numcount[temp%10]++;
      temp /= 10;
      total++;
    }
    numcount[0] = 21 - total;

    bool incr=true;
    bool decr=true;
    bool leadingZero = true;
    int curnum = -1;
    int smallest = 10;
    int smallestPos = -1;
    int pos;
    int lastnum = -1;
    for0n(j,22) {
#if 0
      if ((numarray[j] == 0) && leadingZero) {
        continue;
      } else {
        leadingZero = false;
      }
#endif
      if (numarray[j]<=smallest) {
        smallest = numarray[j];
        smallestPos = j;
      }
      if ( (numarray[j]>=curnum) ) {
      //if ((numarray[j]>=curnum) || (numarray[j] == 0)) {
        //cout << "Can use " << numarray[j] << endl;
        numToUse[numarray[j]]++;
        curnum = numarray[j];
        continue;
      } else {
        lastnum = numarray[j];
        incr = false;
        break;
      }
    }

#if 0
    if (incr) {
      cout << "All incr" << endl;
    } else {
      cout << "Stop incr @ " << j << " lastnum " << lastnum << endl;
    }
#endif

    for(l = lastnum + 1; l < 10; l++) {
      if (numToUse[l] > 0) {
        numarray[j] = l;
        numToUse[l]--;
        //cout << "replace with " << l << endl;
        break;
      }
    }
    numToUse[lastnum]++;

#if 0
    for0n(k, 22){
      cout << numarray[21-k];
    }
    cout << endl;
#endif

    for(k = j-1; k >= 0; k--) {
      for0n(l, 10) {
        if (numToUse[l] > 0) {
          //cout << "use " << l << endl;
          numarray[k] = l;
          numToUse[l]--;
          break;
        }
      }
    }

#if 0
    for0n(k, 22){
      cout << numarray[21-k];
    }
    cout << endl;
#endif

    uint64_t val = 1;
    for0n(k,22) {
      ans+=(val * numarray[k]);
      val*=10;
    }
    cout << "Case " << i + 1 << ": " << ans << endl;

    outFile << "Case #" << i+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
