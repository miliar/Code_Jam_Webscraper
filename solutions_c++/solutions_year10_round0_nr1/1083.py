#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int
main()
{
  int ncases;

  cin >> ncases;

  for (int i = 1; i <= ncases; i++) {
    unsigned int ndev, nsnap;
    cin >> ndev >> nsnap;
    cout << "Case #" << i << ": ";
    cout << ((((nsnap + 1) & ((1UL << ndev) - 1)) == 0) ? "ON" : "OFF");
    cout << endl;
  }
  return 0;
}
