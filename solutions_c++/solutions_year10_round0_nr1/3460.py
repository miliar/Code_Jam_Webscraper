#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <list>
using namespace std;

/*class Snappers
{
  public:
    Snappers(size_t size) : snappers(size, false), cache(size, -1)
    {
    }

    void snap(int numSnaps)
    {
      for (int i = numSnaps; --i >= 0;)
        snap();
    }

    bool isPowered(int i) const
    {
      if (cache[i] != -1)
        return cache[i] == 1;

      //bool powered = (snappers[i] && (i == 0 || isPowered(i - 1)));
      bool powered = snappers[i];
      if (powered)
      {
        int j = i;
        while (--j > 0)
          if (!snappers[j])
          {
            powered = false;
            break;
          }
      }
      cache[i] = powered ? 1 : 0;
      return powered;
    }

  private:
    void snap()
    {
      cache = vector<int>(snappers.size(), -1);
      for (int i = (int) snappers.size(); --i >= 0;)
        if (i == 0 || isPowered(i - 1))
          snappers[i]= !snappers[i];
    }

    vector<bool> snappers;
    mutable vector<int> cache;
};*/

int main(int argc, char **args)
{
  if (argc == 1)
    return -1;

  string fileName = args[1];
  freopen((fileName.substr(0, fileName.find('.')) + ".out").c_str(), "wt", stdout);

  ifstream input(fileName.c_str());
  int numCases;
  input >> numCases;

  for (int i = 0; i < numCases; ++i)
  {
    unsigned long long numSnappers, snaps;
    input >> numSnappers;
    input >> snaps;

    /*Snappers snappers(numSnappers);
    snappers.snap(snaps);

    printf("Case #%d: %s\n", i + 1, snappers.isPowered(numSnappers - 1) ? "ON" : "OFF");*/

    unsigned long long period = 1;
    if (numSnappers == 1)
      period = 1;
    else
    {
      period = 4;
      for (int i = 2; i < numSnappers; ++i)
        period *= 2;
    }
    
    bool powered = false;
    if (numSnappers == 1)
    {
      powered = ((snaps % 2) == 1);
    }
    else
    {
      if (snaps > 0 && snaps == period - 1)
        powered = true;
      else if (snaps > period)
      {
        if (snaps == period - 1)
          powered = true;

        snaps -= period - 1;
        powered = ((snaps % period) == 0);
      }
    }

    printf("Case #%d: %s\n", i + 1, powered ? "ON" : "OFF");
  }

  return 0;
}
