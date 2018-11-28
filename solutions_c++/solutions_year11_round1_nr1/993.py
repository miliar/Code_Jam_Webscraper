#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <utility>
#include <deque>
using namespace std;

int main()
{
  ifstream ifs("A-large.in");
  ofstream ofs("result.dat");
  int T;
  ifs>>T;
  for(int i = 0; i < T; ++i)
  {
    ofs << "Case #"<<(i+1)<<": ";
    long long N, PD, PG;
    ifs>> N >>PD>> PG;

    if ((PG == 0 && PD != 0) || (PG == 100 && PD != 100))
    {
      ofs << "Broken\n";
      continue;
    }
    if (PG == 0 && PD == 0)
    {
      ofs << "Possible\n";
      continue;
    }
    long long tPD = 100, tPG = PD;
    while(tPD > 0)
    {
      if(tPG > tPD) swap(tPD, tPG);
      tPD = tPD - tPD / tPG * tPG;
    }
    tPG = 100 / tPG;
    if (tPG > N)
    {
      ofs << "Broken\n";
      continue;
    }

    ofs << "Possible\n";
  }
  ofs.close();
  ifs.close();
    return 0;
}
