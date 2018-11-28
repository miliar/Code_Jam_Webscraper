#include<iostream>
using namespace std;

int main()
{
  int t, n;
  int count = 0;
  cin >> t;
  for (int i = 0; i < t ; i ++)
  {
    cin >> n;
    int count = i;
    int total = 0;
    int min = 1000000;
    int result = 0;
    int input;
    for (int j = 0 ; j < n ; j++)
    {
      cin >> input;
      total += input;
      if (input < min)
        min = input;  
      result ^= input;
    }
    total -= min;
    cout << "Case #" << count + 1 << ": ";
    if (result == 0)
      cout << total << endl;
    else 
      cout << "NO" << endl;
  }
}

