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

int move[4][2] = { {0, 1} , {1, 0} , {0, -1} , {-1, 0} };

//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
int N, M;

int best;
string bestword;

deque<string> dict;
string srch;

int check (int index)
{
  //cout << "Try: " << dict[index] << endl;
  int lc[26];
  int wrong = 0;
  int guess = 0;
  for0n(l, 26)
    lc[l] = 0;
  for0n(l, dict[index].length()) {
    lc[dict[index][l] - 'a']++;
  }
  set<string> poss;
  for0n(l, N) {
    if (dict[index].length() == dict[l].length()) {
      //cout << "--i: " << dict[l] << endl;
      poss.insert(dict[l]);
    }
  }
  for0n(guess, 26) {
    if (poss.size() == 1) {
      // Only one left, no more wrong guesses.
      return wrong;
    }
    char cg = srch[guess];
    // Is the letter in the remaining words?
    bool inremain = false;
    set<string>::iterator sit;
    for(sit = poss.begin(); sit != poss.end();sit++) {
      if((*sit).find(cg) != string::npos) {
        inremain = true;
        break;
      }
    }
    if (!inremain) {
      // Don't guess this letter.
      continue;
    }

    //cout << "-- guess: " << cg;
    if (lc[cg - 'a'] == 0)  {
      wrong++;
      //cout << " X" << endl;
      // Remove everyone from the list that has that letter.
      for(sit = poss.begin(); sit != poss.end();) {
        if ((*sit).find(cg) != string::npos) {
          //cout << "-- remove: " << *sit << endl;
          set<string>::iterator nit = sit;
          nit++;
          poss.erase(sit);
          sit = nit;
        } else {
          sit++;
        }
      }
    } else {
      //cout << " found" << endl;
      // Got a letter right.
      for0n(l, dict[index].length()) {
        if (dict[index][l] == cg) {
          // Remove everyone from the list that doesn't have the letter here.
          set<string>::iterator sit;
          for(sit = poss.begin(); sit != poss.end();) {
            if ((*sit)[l] != cg) {
              //cout << "-- remove: " << *sit << endl;
              set<string>::iterator nit = sit;
              nit++;
              poss.erase(sit);
              sit = nit;
            } else {
              sit++;
            }
          }
        } else {
          // Remove everyone from the list that DOES have the letter here.
          set<string>::iterator sit;
          for(sit = poss.begin(); sit != poss.end();) {
            if ((*sit)[l] == cg) {
              //cout << "-- remove: " << *sit << endl;
              set<string>::iterator nit = sit;
              nit++;
              poss.erase(sit);
              sit = nit;
            } else {
              sit++;
            }
          }
        }
      }
    }
  }
  return wrong;
}

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
    dict.clear();
    best = -1;

    inFile >> N >> M;

    for0n(i, N) {
      string word;
      inFile >> word;
      dict.push_back(word);
    }

    cout << "Case #" << c + 1 << ": ";
    outFile << "Case #" << c + 1 << ": ";

    for0n(i, M) {
      best = -1;
      inFile >> srch;
      //cout << srch << endl;

      for0n(j, N) {
        int cval = check(j);
        //cout << "----v: " << cval << endl;
        if (cval > best) {
          //cout << "---- NEW"  << endl;
          best = cval;
          bestword = dict[j];
        }
      }

      // output the best word
      cout << bestword;
      outFile << bestword;
      if (i + 1 != M) {
        cout << " ";
        outFile << " ";
      }
    }

    cout << endl;
    outFile << endl;
  }

  outFile.close();
  return 0;
}
