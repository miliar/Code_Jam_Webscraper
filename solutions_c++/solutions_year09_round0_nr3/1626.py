#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
#include <iomanip>
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

uint32_t my32;
uint32_t temp;

uint64_t i, k, l, ans;
int j;
int nCases;
uint64_t n, m, x, y, z;
vector<uint64_t> svec;

string inString;
vector<uint64_t> avec;
//vector<uint64_t[26]> avec;
int counters[500][25];
string wtcj("welcome to code jam");

uint64_t numCases(int fromPos, int wtcjPos)
{
  int ii, jj;
  int count = 0;
  //cout << "Cur: " << inString[fromPos] << endl;

  if (fromPos >= inString.length()) {
    return 0;
  }

  if(counters[fromPos][wtcjPos] != 0) {
    //cout << "-- Found " << counters[fromPos][wtcjPos] << "@" << fromPos << "/" << wtcjPos << endl;
    return (counters[fromPos][wtcjPos]);
  }

  if(inString[fromPos] != wtcj[wtcjPos]) {
    count = numCases(fromPos+1, wtcjPos);
    counters[fromPos][wtcjPos] = count % 10000;
  } else {
    //cout << "-- Match " << wtcj[wtcjPos] << endl;
    if (wtcjPos == (wtcj.length() - 1)) {
      //cout << "-- Ding! " << endl;
      count = 1 + numCases(fromPos+1, wtcjPos);
      counters[fromPos][wtcjPos] = count % 10000;
    } else {
      count = numCases(fromPos+1, wtcjPos) + numCases(fromPos+1, wtcjPos + 1);
      counters[fromPos][wtcjPos] = count % 10000;
    }
  }

  return count;
}

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  cout << wtcj << " length = " << wtcj.length() << endl;;

  inFile >> nCases;
  //for0n(i, 1) {
  char raw[520];
  inFile.getline(raw, 520) ;
  for0n(i, nCases) {
    cout << "Running case #" << i+1 << endl;
    memset(counters, 0, sizeof(counters));
    ans = 0;
    svec.clear();
    avec.clear();

    //inFile >> inString ;
    inFile.getline(raw, 520) ;
    inString.assign(raw);
#if 0
    avec.clear();
    for0n(j, inString.length()) {
      avec.push_back(0);
    }

    //forn(j, inString.length(), 0) {
    for (j=inString.length(), j >= 0, j--){
      ans += numCases(j);
    }
    for0n(j, inString.length()) {
      cout << j << ":" << inString[j] << endl;
      ans += numCases(j, 0);
    }
#endif
    ans += numCases(j, 0);
    ans %= 10000;
    cout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << ans << endl;
    outFile << "Case #" << i+1 << ": " << setw(4) << setfill('0') << ans << endl;
  }

  outFile.close();
  return 0;
}
