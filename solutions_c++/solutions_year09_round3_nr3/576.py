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

int mymap[25][25];
int mysrch[25][25][250];

int i, j, k, l;
uint64_t ans;
int nCases;
int d, n;
int p, q;

char myline[80];
set<int> rel;
set<int> released;
set<int> stillin;

class node {
public:
  uint64_t cost;
  int start;
  int end;
  node *child[2];

  node(int from, int to) {
    cost = 0;
    start = from;
    end = to;
    child[0] = child[1] = NULL;
  }
  ~node() {
    delete(child[0]);
    delete(child[1]);
  }
};

uint64_t costToRel(int from, int to, set<int> &relRef) {
  set<int> myset(relRef);
  set<int>::iterator si;
  int check;
  uint64_t cost = 0;
  uint64_t minCost = inf;
  bool valid = false;
  
  cout << "CTR " << from << "," << to << endl;
  if (from >= to)
    return 0;

  if (relRef.size() == 0)
    return 0;

  for(si = relRef.begin();
      si != relRef.end();
      si++) {
    if(( *si >= from ) && ( *si <= to )) {
      valid = true;
      myset.erase(*si);
      cout << "Try releasing " << *si << " from " << from << "," << to <<  endl;
      int a, b;
      a= costToRel(from, (*si)-1, myset);
      b=costToRel((*si)+1, to, myset);
      //check = (to - from) + costToRel(from, (*si)-1, myset) + costToRel((*si)+1, to, myset);
      check = (to - from) + a + b;
      cout << "cost:" << a << " + " << b <<  endl;
      cout << "cost:" << check <<  endl;
      //cout << "Try releasing " << *si << " from " << from << "," << to << "  cost:" << check <<  endl;
      if (check < minCost) {
        minCost = check;
      }
      myset.insert(*si);
    }
  }
  if (valid) return minCost; else return 0;
}

uint64_t costToRel(int pos, set<int> &relRef, set<int> &inRef) {
  int check;
  uint64_t cost = 0;
  for(check = pos +1; check < p; check++) {
    // if still there... cost ++
    // else break;
    if(relRef.find(check) == relRef.end())
      cost++;
    else
      break;
  }
  for(check = pos -1; check >= 0; check--) {
    // if still there... cost ++
    // else break;
    if(relRef.find(check) == relRef.end())
      cost++;
    else
      break;
  }
  return cost;
}

int lines;
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
    rel.clear();
    released.clear();
    ans = inf;
#if 0
    for0n(j, 25)
      for0n(k, 25) {
        mymap[j][k] = -100;
        for0n(l,250)
          mysrch[j][k][l] = -1;
      }
#endif
     

    inFile >> p >> q;
    cout << "Case " << i+1 << ": " << p << ", " << q<< endl;

    for0n(j, q) {
      int temp;
      inFile >> temp;
      rel.insert(temp - 1);
      cout << "Have to release " << temp  - 1<< endl;
    }
    for0n(j, p) {
      stillin.insert(j);
    }

    ans = costToRel(0, p-1, rel);
#if 0 
    cout << "cost to release 14: " << costToRel(14 - 1, released, stillin) << endl;
    released.insert(13);
    cout << "cost to release 6: " << costToRel(6 - 1, released, stillin) << endl;
    released.insert(5);
    cout << "cost to release 3: " << costToRel(3 - 1, released, stillin) << endl;
#endif

    cout << "Case #" << i + 1 << ": " << ans << endl;
    outFile << "Case #" << i + 1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
