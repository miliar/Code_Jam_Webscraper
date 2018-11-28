#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

int num[] = {1, 2, 4, 5, 10, 20, 25, 50, 100};
int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N;
    int PD, PG;
    cin >> N >> PD >> PG;
    int minD = 1;
    for (int i = 0; i < 9; i++)
      if (PD * num[i] % 100 == 0) {
	minD = num[i];
	break;
      }
    int minT = minD * PD / 100;
    int minF = minD * (100 - PD) / 100;

    bool success = 1;
    if (PG == 0) {
      if (minT > 0)
	success = 0;
    } else if (PG == 100) {
      if (minF > 0)
	success = 0;
    } else if (minD > N) {
      success = 0;
    }

    cout << "Case #" << t << ": ";
    if (success)
      cout << "Possible";
    else
      cout << "Broken";
    cout << endl;
  }
  return 0;
}
