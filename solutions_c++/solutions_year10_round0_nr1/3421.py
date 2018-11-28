#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int t;
cin >> t;
for(int i = 0 ; i < t ; i++)
  {
  int n, k, power;
  cin >> n >> k;
  power = pow(2, n);
  if(k % power == power - 1)
    cout << "Case #" << i + 1 << ": ON" << endl;
  else
    cout << "Case #" << i + 1 << ": OFF" << endl;
  }
return 0;
}