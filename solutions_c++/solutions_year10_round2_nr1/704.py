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

int i, j, k, l, ans, N, M;
int nCases;
int d, n;

class dir {
public:
  dir(string name) : iName(name)
  {
  }
  dir* getSubDir(string name) {
    addSubDir(name);
    list<dir *>::iterator it;
    for (it = subdir.begin(); it != subdir.end(); it++) {
      if ((*it)->iName == name) {
        return (*it);
      }
    }
    return NULL;
  }
  bool isSubDir(string name) {
    list<dir *>::iterator it;
    for (it = subdir.begin(); it != subdir.end(); it++) {
      if ((*it)->iName == name) {
        return true;
      }
    }
    return false;
  }
  void addSubDir(string name) {
    if (!isSubDir(name)) {
      dir *newSubDir = new dir(name);
      subdir.push_front(newSubDir);
      ans++;
    }
  }
  string iName;
  list<dir *> subdir;
};

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output.txt", fstream::out);

  inFile >> nCases;
  //cout << nCases << endl;
  for0n(i,nCases) {
    inFile >> N >> M;
    ans = 0;
    dir *rootDir = new dir("");
    //cout << "A" << endl;
    for0n(j, N) {
      dir *curDir = rootDir;
      //cout << "B" << endl;
      string dirName;
      char cstring[200];
      // Add pre-existing dirs.
      inFile >> dirName;
      strcpy(cstring, dirName.c_str());
      //cstring = dirName.c_str();
      char *nextTok;
      //cout << cstring << endl;
      nextTok = strtok(cstring, "/");
      while (nextTok != NULL) {
        //cout << nextTok << endl;
        curDir = curDir->getSubDir(nextTok);
        nextTok = strtok(NULL, "/");
      }


    }
    ans = 0;
    for0n(j, M) {
      dir *curDir = rootDir;
      //cout << "B" << endl;
      string dirName;
      char cstring[200];
      // Add pre-existing dirs.
      inFile >> dirName;
      strcpy(cstring, dirName.c_str());
      //cstring = dirName.c_str();
      char *nextTok;
      //cout << cstring << endl;
      nextTok = strtok(cstring, "/");
      while (nextTok != NULL) {
        //cout << nextTok << endl;
        curDir = curDir->getSubDir(nextTok);
        nextTok = strtok(NULL, "/");
      }
    }

    delete(rootDir);
    outFile << "Case #" << i+1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
