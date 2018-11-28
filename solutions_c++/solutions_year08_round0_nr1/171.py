#include <iostream>

using namespace std;

char s[1010][200];
char q[1010][200];


int main()
{
  int n, k, m, t, use[1010], _count = 0, pos, col[1010], best, ind;
  int i, j;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

  for (t = 0; t < n; t++)
  {
    cin >> k;
    gets(s[0]);
    for (i = 0; i < k; i++)
      gets(s[i]);

    cin >> m;
    gets(q[0]);
    for (i = 0; i < m; i++)
      gets(q[i]);

    pos = 0;
    while (pos < m)
    {
      _count++;

      best = -1;
      for (i = 0; i < k; i++)
      {
//        col[i] = 0;
        j = 0;
        while ((j + pos < m) && strcmp(s[i], q[j + pos]) != 0)
          j++;                  

        col[i] = j;

        if (col[i] > best)
        {
          best = col[i];
          ind = i;
        }
      }

      pos += best;
//      cout << pos << ' ' << s[ind] << endl;
    }

    if (_count <= 0)
      _count = 1;

    cout << "Case #" << t + 1 << ": " << _count - 1 << endl;
    _count = 0;
  }

  return 0;
}