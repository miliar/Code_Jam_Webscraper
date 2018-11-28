#include <iostream>
using namespace std;

int main()
{
  int n, t, m;
  int result = 0;
  cin >> n;
  for (int i = 0; i < n ; i++)
  {
    cin >> t;
    result = 0;
    for (int j = 0; j < t; j++)
    {
      cin >> m;
      if (m != j+1)
        result ++;
    }
    cout << "Case #" << i+1 <<": " << result << ".000000" <<endl;
  }   
}
