#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
  ifstream file ("A-small-attempt0.in");
  ofstream outfile("outfile.out");
  int n, k, t, num; // # snappers, # snaps, # cases, current case
  num = 1;
  file >> t; 
  while (file >> n >> k)
  {
  if (k > pow(2, n))
  {
    while (k >= pow(2, n))
      k -= pow(2, n);
  }
  
  if (k == pow(2, n)-1)
    outfile << "Case #" << num << ": ON" << endl;
  else
    outfile << "Case #" << num << ": OFF" << endl;

    num++;
  }
  return 0;
}
