#include <stdio.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

bool checkAncestors(bool *snappers, int pos)
{
  while (pos != -1) {
    if (!snappers[pos])
      return false;
    pos--;
  }
  return true;
}

int main(int argc, char **argv)
{
  if (argc == 1)
    return -1;

  string fileName = argv[1];
  freopen((fileName.substr(0, fileName.find('.')) + ".out").c_str(), "wt", stdout);

  ifstream input(fileName.c_str());
  int t, n, k;
  input >> t;

  for (int i = 0; i < t; ++i) { 
    input >> n;
    input >> k;
    bool *snappers = new bool[n];
    memset(snappers, 0, n);

    bool allOn = false;
    while(k--) {
      allOn = true;
      for (int j = n - 1; j >= 0; --j) {
        if (j == 0)
          snappers[j] = !snappers[j];
        else {
          if (checkAncestors(snappers, j - 1))
            snappers[j] = !snappers[j];
        }

        if (allOn)
          allOn = snappers[j];
      }
    }
    if (allOn)
      printf("Case #%d: ON\n", i + 1);
    else
      printf("Case #%d: OFF\n", i + 1);
    delete snappers;
  }

  return 0;
}