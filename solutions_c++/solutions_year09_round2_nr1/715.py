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
double ans;
int nCases;
int d, n;

class node {
public:
  int type;
  double weight;
  string feature;
  node *child[2];

  node(void) {
    type = -1;
    weight = 0.0;
    feature.clear();
    child[0] = child[1] = NULL;
  }
  ~node() {
    delete(child[0]);
    delete(child[1]);
  }

};

node *head;
char myline[80];

void processIn(fstream& stm, node *ptr) {
  char inchar;
  double inwt;
  do {
    stm.read(&inchar, 1);
  } while ((inchar == ' ') || (inchar == '\n'));

  // just read the (
  stm >> inwt;
  ptr->weight = inwt;
  cout << "got wt " << inwt << endl;

  // Now check to see if there is a feature or a close ).
  do {
    stm.read(&inchar, 1);
  } while ((inchar == ' ') || (inchar == '\n'));

#if 0
  if (inchar == '\(') {
    ptr->child[0] = new node();
    ptr->child[1] = new node();
    ptr->type = 1;
    processIn(stm, &(ptr->child[0]));
    processIn(stm, &(ptr->child[1]));
  } else 
#endif
  if (inchar == ')') {
    ptr->type = 0;
    cout << "* return" << endl;
    return;
  } else {
    stm.putback(inchar);
    stm >> ptr->feature;
    cout << "got feature " << ptr->feature << endl;
    ptr->child[0] = new node();
    ptr->child[1] = new node();
    ptr->type = 1;


    processIn(stm, (ptr->child[0]));
    processIn(stm, (ptr->child[1]));
    do {
      stm.read(&inchar, 1);
    } while (( inchar != ')' ));
  }
}

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
  for0n(i,nCases) {
    int numAn = 0;
    int numFt = 0;
    string anNam;
    ans = 1.0;
    inFile >> lines;
      inFile.getline(myline, 80);
    memset (myline, 0, sizeof(myline));
    head = new node();
    processIn(inFile, head);

    cout << "Case " << i + 1 << ": " << endl;
    outFile << "Case #" << i+1 << ": " << endl;
    inFile >> numAn;
    for0n(k, numAn) {
      ans = 1.0;
      features.clear();
      inFile >> anNam; // Garbage
      cout << "Animal " << k << " is " << anNam << endl;
      inFile >> numFt;
      for0n(l, numFt) {
        inFile >> anNam;
        features.insert(anNam);
      }

      // Now walk the tree.
      node *ptr = head;
      while (ptr != NULL) {
        ans *= ptr->weight;
        if (ptr->type == 1) {
          if (features.find(ptr->feature) != features.end()) {
            ptr = ptr->child[0];
          } else {
            ptr = ptr->child[1];
          }
        } else {
          break;
        }
      }
    outFile.precision(8);
    outFile.setf(ios::fixed,ios::floatfield);
    cout.precision(7);
    cout.setf(ios::fixed,ios::floatfield);
    cout << ans << endl;
    outFile << ans << endl;
    }
    delete(head);

  }

  outFile.close();
  return 0;
}
