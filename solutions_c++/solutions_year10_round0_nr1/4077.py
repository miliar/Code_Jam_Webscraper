#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;
int main(int argc, char * argv[])
{
  int n,k,T,pown;

  cin >> T;
  for (int i = 0; i < T; i++)
  {
    cin >> n >> k;
    pown = pow(2,n);
    k = k%pown;

    if ( k == pown - 1)
      cout << "Case #"<<i+1<<": ON\n";
    else
      cout << "Case #"<<i+1<<": OFF\n";

  }

  cout << endl;
  
}
