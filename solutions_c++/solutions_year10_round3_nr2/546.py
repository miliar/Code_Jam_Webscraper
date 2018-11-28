#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int max[10000];



int 
main(int argc, const char *argv[])
{
  unsigned int i, t;

  cin >> t;

  for(i = 0; i < t ; ++i)
  {
    int Count = 0;
    int l, p, c, Result = 0;

    cin >> l;
    cin >> p;
    cin >> c;

    l *= c;

    while(l < p)
    {
      l*= c;
      Count += 1;
    }

    while(Count != 0)
    {
      Result += 1;
      Count /= 2;
    }

    cout << "Case #" << i+1 << ": " << Result << endl;
  }

  return 0;
}