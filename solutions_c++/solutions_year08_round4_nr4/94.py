#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <numeric>
#include "MyLib.h"

using namespace std;

int main()
{
  long long i, j, ans, t_count, test, n, tmp, m, best;
  char s[1001], str[1001];
  int p[20], k;
  
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    cin >> k;
    gets(s);
    gets(s);

    for (i = 0; i < k; i++)
      p[i] = i;
    n = strlen(s);
    m = n / k;

//    cout << m << endl;

    best = 1000000;
    while (1)
    {
      for (i = 0; i < m; i++)
      {
//        cout << "i = " << i << endl;
        for (j = 0; j < k; j++)
        {
          str[i * k + j] = s[i * k + p[j]];
//          cout << p[j] << ' ' << s[i * k + p[j]] << endl;
        }

//        ans = n;


//        cout << "! " << ans << endl;
//        cout << str << ' ' << s <<  endl;
//        Print(p, k);

      }

      ans = n;

      for (int ii = 1; ii < n; ii++)
        if (str[ii] == str[ii - 1])
          ans--;

        if (ans < best)
          best = ans;


      if (next_permutation(p, p + k) == false)
        break;
    }

    cout << best;

    cout << endl;
  }

  return 0;
}