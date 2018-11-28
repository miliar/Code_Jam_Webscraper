#include <iostream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

int main(int argc, char **argv) {
  
    int nbtests;
    cin >> nbtests;
  
    long k;
    int n;
    for (int test = 0; test<nbtests; test++)
    {
      cin >> n;
      cin >> k;
      if (k == 0)
      {
	cout << "Case #" << test+1 <<": OFF" << endl;
      }
      else
      {
	long switchs = pow(2, n);
	if ((k % switchs) == switchs - 1)
	  cout << "Case #" << test+1 <<": ON" << endl;
	else
	  cout << "Case #" << test+1 <<": OFF" << endl;
      }
    }
    
    return 0;
}
