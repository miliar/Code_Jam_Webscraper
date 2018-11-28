#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main () {
  ifstream ifs("C-small-attempt0.in");
  ofstream ofs("C.out");
  int T, rides, space, groups, monies, passed, ipassed, sub, count;
  int * argroups;
  ifs >> T;
  for (int k =0; k < T; k++)
  {
    monies = 0;
    passed = 0;
    ifs >> rides;
    ifs >> space;
    ifs >> groups;
    argroups = new int[groups];
    for (int j = 0; j < groups; j++)
    {
      ifs >> argroups[j];
    }
    for (int i =0; i < rides; i++)
    {
      sub = 0;
      count = 0;
      ipassed = passed;
      do
      {
        sub += argroups[((count+ipassed)%groups)];
        count++;
        passed++;
      }
      while ((sub <= space)&&(count<=groups));
      passed--;
      monies += (sub - argroups[((count-1+ipassed)%groups)]);
    }
    delete[] argroups;
    ofs << "Case #" << (k+1) << ": " << monies << '\n';
  }
  return 0;
}