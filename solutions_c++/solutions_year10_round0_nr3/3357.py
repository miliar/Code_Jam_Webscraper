#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

int main(int argc, char **args)
{
  if (argc == 1)
    return -1;

  string fileName = args[1];
  freopen((fileName.substr(0, fileName.find('.')) + ".out").c_str(), "wt", stdout);

  ifstream input(fileName.c_str());
  int numCases;
  input >> numCases;

  for (int _case = 0; _case < numCases; ++_case)
  {
    int runs, capacity, numGroups;
    input >> runs;
    input >> capacity;
    input >> numGroups;

    vector<int> groups(numGroups, -1);
    int group;
    for (int i = 0; i < numGroups; ++i)
    {
      input >> group;
      groups[i] = group;
    }

    int result = 0;
    int current = 0;
    int first;
    int sum;
    for (int run = runs; --run >= 0;)
    {
      sum = 0;
      first = current;
      while (sum < capacity && sum + groups[current] <= capacity)
      {
        sum += groups[current % numGroups];
        current = (current + 1) % numGroups;
        
        if (first == current)
          break;
      }

      result += sum;
    }

    printf("Case #%d: %d\n", _case + 1, result);
  }
  
  return 0;
}
