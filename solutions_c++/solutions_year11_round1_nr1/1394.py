#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <functional>

using namespace std;

bool is_round(float n)
{
  return (float)((int)n) == n;
}

int main() 
{
  int T;
  cin >> T;

  for(int i = 0; i < T; i++)
  {
    int N, Pd, Pg;
    cin >> N >> Pd >> Pg;

    bool possible = false;

    for(int d = 1; d <= N && d <= 100 && possible == false; d++)
    {
      float p = (float)(Pd * d) / (float)100.;
      possible = is_round(p);
    }

    if(possible)
    {
      if(Pg == 100 && Pd != 100)
	possible = false;

      if(Pg == 0 && Pd != 0)
	possible = false;
    }

    cout << "Case #" << i + 1 << ": " << (possible ?  "Possible" : "Broken") << endl;
  }
}
