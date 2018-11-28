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
uint64_t modArr[3][3];

uint64_t i, j, k, l, ans, ans2;
int nCases;
uint64_t d, n;
vector<string> dict;
vector<string> poss;
vector<string> newposs;
string word;
string input;
set<char> charSet;


int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> l >> d >> nCases;
  dict.clear();
  for0n(i,d) {
      inFile >> word;
      dict.push_back(word);
      cout << word << endl;
  }
  for0n(i, nCases) {
    newposs.clear();
    ans2 = ans = 0;

    poss = dict;
    cout << poss.size() << endl;
    inFile >> input;
    string::iterator siter = input.begin();
    for0n(j, l) {
      cout << input << endl;

      if (poss.size() == 0) {
        // No possibilities left.
        break;
      }
      // For each letter in the word.
      charSet.clear();
      if (*siter == '(') {
        siter++;
        while (*siter != ')') {
          charSet.insert(*siter);
          siter++;
        }
      } else {
        charSet.insert(*siter);
      }
      siter++;

      for (vector<string>::iterator viter = poss.begin();
           viter != poss.end();
           viter++) {
        if(charSet.find((*viter)[j]) == charSet.end() ) {
          //cout << "Not in " << *viter << endl;
        } else {
          newposs.push_back(*viter);
        }
      }
      cout << "Remaining options: " << newposs.size() << endl;
      poss = newposs;
      newposs.clear();

    }
    ans2=poss.size();
    outFile << "Case #" << i+1 << ": " << ans2 << endl;
  }

  outFile.close();
  return 0;
}
