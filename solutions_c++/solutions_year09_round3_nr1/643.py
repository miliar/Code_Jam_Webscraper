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

int i, j, k, l;
uint64_t ans;
set<char> sym;
vector<char> num;
int val[256];
bool numused[256];
int nCases;
int d, n;

char myline[80];
bool first;
char firstsym;
char inchar;

set<string> features;

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

      inFile.getline(myline, 80);
  for0n(i,nCases) {
    ans = 0;
    sym.clear();
    num.clear();
    for0n(j, 256) {
      val[j] = -1;
      numused[j] = false;
    }
    first = true;
    firstsym = 0;
    bool firsttime = true;

    do {
      inFile.get(inchar);
      if ((inchar == ' ') || (inchar == '\n')) {
        break;
      }
      cout << inchar ;
      if (firstsym == 0) 
        firstsym = inchar;

      if ((firstsym != inchar) && (firsttime))
      {
        val[inchar] = 0;
        numused[0] = true;
        firsttime = false;
        first = false;
        cout << "." ;
      }
      cout << "Inserting " << inchar << endl;
      sym.insert(inchar);
      num.push_back(inchar);

    } while ((inchar != ' ') && (inchar != '\n'));

    if (first) {
      sym.insert(0);
      numused[0] = true;
    }

    uint64_t base = 1;
    int start;
    int value;
    for0n(j, num.size()) {
      if (val[num[j]] != -1) {
        value = val[num[j]];
      } else {
        if(num[j] == first) {
          start = 1;
        } else {
          start = 0;
        }
        for(k = start; k < sym.size() ; k++){
        //for(k = sym.size()-1; k >= 0 ; k--){
          if (numused[k] == false)  {
            val[num[j]] = k;
            numused[k] = true;
            break;
          }
        }
      }
      value = val[num[j]];
      cout << num[j] << " is " << value << endl;
    }
    for (j = num.size() - 1; j >= 0; j--) {
      value = val[num[j]];
      ans += value * base;
      base *= sym.size();
    }




    cout << "Case " << i + 1 << ": ";
    outFile << "Case #" << i+1 << ": ";
    cout << ans << endl;
    outFile << ans << endl;

  }

  outFile.close();
  return 0;
}
