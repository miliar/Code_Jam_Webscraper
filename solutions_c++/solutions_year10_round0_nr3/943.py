#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int 
main(int argc, const char *argv[])
{
  __int64 t, i;

  cin >> t;

  for(i = 0; i < t ; ++i)
  {
    __int64 r, k, n, j;
    __int64 groups[1000];
    __int64 p;
    __int64 g = 0;
    __int64 result = 0;
    __int64 t = 0;


    cin >> r;
    cin >> k;
    cin >> n;
    
    for(j = 0; j < n ; ++j)
    {
      cin >> groups[j];
      t += groups[j];
    }

    if(t <= k)
    {
      result = t * r;
    }
    else
    {
      for(j = 0 ; j < r ; ++j)
      {
        p = 0;
        while(k-p >= groups[g])
        {
          p += groups[g++];
          if(g >= n)
          {
            g = 0;
          }
        }
        result += p;
      }
    }
    cout << "Case #" << i+1 << ": " << result << endl;
  }

  return 0;
}