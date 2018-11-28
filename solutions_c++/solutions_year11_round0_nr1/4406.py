#include <iostream>
#include <stdio.h>

using namespace std;

int t, n;
char * turns;
int poso;
int posb;
int cturn;

int move(int d, int c)
{
    if (d == c)
        return c;
    if (d > c)
        return ++c;
    else
        return --c;
}

int main()
{
  //freopen("in.txt", "r", stdin);
  cin >> t;
  char turns[100] = {' '};
  poso = 0;
  posb = 0;
  for(int i=0 ; i<t ; i++)
  {
    cturn = 0;
    cin >> n;
    int o[100] = {0};
    int b[100] = {0};
    for (int j=0; j<n; j++)
    {
      char r;
      cin >> r;
      int btn;
      cin >> btn;
      turns[j] = r;
      if (r == 'B')
      {
        b[posb] = btn;
        posb++;
      }
      else
      {
        o[poso] = btn;
        poso++;
      }
    }

    int co = 1;
    int to = 0;
    int cb = 1;
    int tb = 0;
    int secs = 0;
    while (cturn < n)
    {
        bool moveo = true;
        bool moveb = true;
      if (turns[cturn] == 'B')
      {
        if (b[tb] == cb)
        {
          cturn++;
          tb++;
          moveb=false;
        }
      }
      else
      {
        if (o[to] == co)
        {
          cturn++;
          to++;
          moveo = false;
        }
      }

      if (moveo)
          co = move(o[to], co);
      if (moveb)
          cb = move(b[tb], cb);

      secs++;
    }

    poso = 0;
    posb = 0;
    cout << "Case #" << i+1 << ": " << secs << endl;
  }
  return 0;
}
