#include <iostream>
#include <string>

using namespace std;

#define MAX_X 100
#define MAX_Y 100

//#define MAX_X 5
//#define MAX_Y 5

char getRedChar(int x, int y)
{
  return (x + y) / 2 * 2 == (x + y) ? '/' : '\\';
}

int main()
{
  int T; cin >> T;
  for (int t = 0; t < T; t++)
  {
    cout << "Case #" << t + 1 << ":" << endl;

    char style[MAX_X][MAX_Y];

    for (int y = 0; y < MAX_Y; y++)
      for (int x = 0; x < MAX_X; x++)
        style[x][y] = '\0';

    int R; cin >> R;
    int C; cin >> C;
    
    //
    // Read Style
    //
    for (int y = 0; y < R; y++)
    {
      string s; cin >> s;
      char* buf = (char*)s.c_str();
      for (int x = 0; x < C; x++)
      {
        style[x][y] = *buf;
        buf++;
      }
    }

    //
    // Change Style
    // 
    for (int y = 0; y < R; y++)
    {
      for (int x = 0; x < C; x++)
      {
        if (style[x][y] == '#') // blue
        {
          if (x + 1 < C && y + 1 < R)
          {
            if (
              style[x+1][y  ] == '#' &&
              style[x  ][y+1] == '#' &&
              style[x+1][y+1] == '#')
            {
              style[x  ][y  ] = '/';
              style[x+1][y  ] = '\\';
              style[x  ][y+1] = '\\';
              style[x+1][y+1] = '/';
            }
          }
        }
      }
    }
    
    //
    // Check Style
    // 
    bool ok = true;
    for (int y = 0; y < R; y++)
    {
      for (int x = 0; x < C; x++)
      {
        if (style[x][y] == '#')
        {
          ok = false;
          break;
        }
      }
    }

    if (ok)
    {
      //
      // Write Style
      //
      for (int y = 0; y < R; y++)
      {
        for (int x = 0; x < C; x++)
        {
          char ch = style[x][y];
          cout << ch;
        }
        cout << endl;
      }
    } else
    {
      cout << "Impossible" << endl;
    }
  }
  return 0;
}