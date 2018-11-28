#include <windows.h>
#include <math.h>
#include <float.h>
#include <iostream>
#include <fstream>
#include <string>

//
// I use C++ Big Integer library by Matt McCutchen
// Available here: http://mattmccutchen.net/bigint/ 
//

#include "BigIntegerLibrary.hh"

using namespace std;

BigInteger mcd(const BigInteger & x,const BigInteger & y)
{
  BigInteger result;
  if(y == 0)
  {
    result = x;
  }
  else
  {
    result = mcd(y, x%y);
  }
  return result;
}

int cmp(const void *a, const void *b)
{
  int Result = 0;
  BigInteger BigResult;

  BigResult = *(BigInteger*)b - *(BigInteger*)a;
  if(BigResult < 0)
  {
    Result = -1;
  }
  else
  {
    if(BigResult > 0)
    {
      Result = 1;
    }
  }
  return Result;
}

int 
main(int argc, const char *argv[])
{
  unsigned int c, i;

  cin >> c;

  for(i = 0; i < c ; ++i)
  {
    BigInteger list[1000];
    BigInteger result;
    unsigned int j, k, n;

    cin >> n;

    for(j = 0; j < n ; ++j)
    {
      string s;

      cin >> s;
      list[j] = stringToBigInteger(s);
    }

    qsort(list, n, sizeof(BigInteger), cmp);

    result = list[0] - list[1];

    for(j = 0; j < n ; ++j)
    {
      for(k = 0; k < j ; ++k)
      {
        result = mcd(result, list[k] - list[j]);
      }
    }

    if(list[0] % result != 0)
    {
      result = (result * ((list[0] / result) + 1)) - list[0];
    }
    else
    {
      result = 0;
    }
    cout << "Case #" << i+1 << ": " << result << endl;
  }

  return 0;
}