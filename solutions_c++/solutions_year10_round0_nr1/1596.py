#include <iostream>

using namespace std;

typedef long long int llint;

void solveCase(unsigned int caseNum)
{
  llint n, k,i ;
  cin >> n >> k;

  for(i = 0; i < n; i++)
  {
    if((k % (1 << (i+1))) < (1 << i))
    {
      cout << "Case #" << caseNum << ": OFF"  << endl;
      return;
    }
  }
  cout << "Case #" << caseNum << ": ON" << endl;
}

int main()
{
  unsigned int t, i;

  cin >> t;
  for(i=1; i<=t; i++)
    solveCase(i);

  return 0;
}
