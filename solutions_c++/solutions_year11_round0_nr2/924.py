#include <string.h>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
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
#define ZERO(arr) for(int CNT=0;CNT<sizeof(arr);CNT++){arr[CNT]=0;}

const int MAX = 1000000;
const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;

vector<string> comb;
vector<pii> dest;
string elements;
string ans;
int counts[26];

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  ifstream inFile(argv[1]);
  ofstream outFile("output.txt", fstream::trunc);

  inFile >> nCases;
  cout << nCases << " cases." << endl;
  for0n(c,nCases) {
    comb.clear();
    dest.clear();
    elements.clear();
    ans.clear();
    ZERO(counts);

    int C, D;
    inFile >> C;
    for0n(i, C) {
      string in;
      inFile >> in;
      comb.push_back(in);
    }
    inFile >> D;
    for0n(i, D) {
      string in;
      inFile >> in;
      dest.push_back(make_pair(in[0]-'A', in[1]-'A'));
    }
    inFile >> i;
    inFile >> elements;

    for0n(i, elements.length()) {
      ans.push_back(elements[i]);
      counts[elements[i] - 'A']++;

      // Check for combine.
      int len = ans.length();
      if(len > 1) {
        vector<string>::iterator it;
        for (it = comb.begin();
             it != comb.end();
             it++) {
          if (((ans[len - 1] == it->at(0)) && (ans[len - 2] == it->at(1))) ||
              ((ans[len - 1] == it->at(1)) && (ans[len - 2] == it->at(0)))) {
            // Combine!
            ans = ans.substr(0, len - 2);
            ans += it->at(2);

            counts[it->at(0) - 'A']--;
            counts[it->at(1) - 'A']--;
            counts[it->at(2) - 'A']++;
          }
        }
      }

      // Check for destroy.
      vector<pii>::iterator it;
      for (it = dest.begin();
           it != dest.end();
           it++) {
        if (counts[it->first] && counts[it->second]) {
          // Clear everything.
          ans.clear();
          ZERO(counts);
        }
      }
    }

    cout << "Case #" << c + 1 << ": [";
    if (ans.length()) {
      for0n(i, ans.length() - 1) {
        cout << ans[i] << ", ";
      }
    }
    cout << ans[i] << "]" << endl;

    outFile << "Case #" << c + 1 << ": [";
    if (ans.length()) {
      for0n(i, ans.length() - 1) {
        outFile << ans[i] << ", ";
      }
      outFile << ans[i] << "]" << endl;
    } else {
      outFile << "]" << endl;
    }
  }

  outFile.close();
  return 0;
}
