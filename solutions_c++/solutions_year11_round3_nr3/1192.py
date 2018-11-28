#include <iostream>
using namespace std;

int num[100];

int main()
{
  int n , j , k , l , p;
  cin >> n;
  for (int i =0 ; i < n; i++)
    {
      int min = -1;
      cin >> j >> k >> l;
      for (int z = 0; z < j ; z++)
      {
        cin >> num[z];
      }
      for (int p = k; k <= l; k++)
      {
        bool div = true;
        for (int z = 0; z < j; z++)
        {
 
          if (num[z] > k)
          {
            if (num[z] % k != 0)
              div = false;
          }
          else
          {  
            if (k % num[z] != 0)
              div = false;
          }
        } 
        if (div == true)
        {   
           min = k;
           break;
        }
      }
      cout <<"Case #" << i+1 << ": ";
      if (min!= -1)
        cout << min << endl;
      else
        cout << "NO" << endl;
    }
}
