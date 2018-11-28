#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <string>

using namespace std;

const int MAX_STRING = 41;

int d[MAX_STRING];
int sign[MAX_STRING]; // 0 .. none, 1 .. plus, 2 .. minus
int len;

inline bool incr ()
{
  if ( len < 2 ) return false;
  int i = 0;
  do
  {
    if ( ++sign[i] < 3 ) return true;
    sign[i++] = 0;
  } while ( i < len-1 );
  return false;
}

bool ugly ()
{
  long long total = 0;
  int si = 1;
  long long num = d[0];
  int i = 0;
  while ( i < len - 1 )
  {
    switch ( sign[i++] )
    {
    case 0:
      num = num * 10 + d[i];
      break;
    case 1:
      if ( si == 1 )
        total += num;
      else
        total -= num;
      num = d[i];
      si = 1;
      break;
    case 2:
      if ( si == 1 )
        total += num;
      else
        total -= num;
      num = d[i];
      si = 2;
      break;
    }
  }

  if ( si == 1 )
    total += num;
  else
    total -= num;

  return( (total & 1) == 0 ||
          total % 3 == 0 ||
          total % 5 == 0 ||
          total % 7 == 0 );
}

int main ()
{
  int num;
  cin >> num;
  int i, j;
  for ( i = 0; i++ < num; )
  {
    string s;
    cin >> s;
    len = s.length();
    for ( j = 0; j < len; j++ )
      d[j] = s[j] - '0';

    int ug = 0;
    memset( sign, 0, sizeof(sign) );
    do
    {
      if ( ugly() ) ug++;
    } while ( incr() );

    cout << "Case #" << i << ": " << ug << endl;
  }

  return 0;
}
