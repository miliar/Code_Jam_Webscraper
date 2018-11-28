#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

const int MAX_LETTERS = 1000;
int P, K, L;

int main ()
{
  int num;
  cin >> num;
  int i, j, c;
  int key, str;
  for ( i = 0; i++ < num; )
  {
    cin >> P >> K >> L;
    vector<int> f;
    for ( j = 0; j++ < L; )
    {
      cin >> c;
      f.push_back( c );
    }
    sort( f.begin(), f.end(), greater<int>() );
    int strokes = 0;
    key = 0;
    str = 1;
    for ( j = 0; j < L; j++ )
    {
      strokes += str * f[j];
      if ( ++key >= K )
      {
        key = 0;
        str++;
      }
    }

    cout << "Case #" << i << ": " << strokes << endl;
  }

  return 0;
}
