#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int max[10000];



int 
main(int argc, const char *argv[])
{
  unsigned int i, t;

  cin >> t;

  for(i = 0; i < t ; ++i)
  {
    int p, j,k, Result = 0;
    int a[10000], b[10000];

    cin >> p;

    for(j = 0; j < p ; ++j)
    {
      cin >> a[j];
      cin >> b[j];
    }
    
    for(j = 0; j < p ; ++j)
    {
      for(k = j + 1; k < p ; ++k)
      {
        if(a[j] < a[k])
        {
          if(b[j] > b[k])
          {
            Result += 1;
          }
        }
        else
        {
          if(b[j] < b[k])
          {
            Result += 1;
          }
        }
      }
    }


    cout << "Case #" << i+1 << ": " << Result << endl;
  }

  return 0;
}