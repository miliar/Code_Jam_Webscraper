// P3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int ntests;

string s;

const string w = "welcome to code jam";


int _tmain(int argc, _TCHAR* argv[])
  {
  cin >> ntests;
  getline(cin, s);
  for (int ctest = 0; ctest < ntests; ++ctest)
    {
    getline(cin, s);

    int ans[1024][32];

    memset(ans, 0, sizeof(ans));

    for (int i = 0; i < s.size(); ++i)
      for (int j = 0; j <= w.size(); ++j)
        if (j == 0)
          ans[i][j] = 1;
        else
          {
          int r = 0;

          if (i)
            r = ans[i - 1][j];

          if (s[i] == w[j - 1])
            if (i == 0)
              {
              if (j == 1)
                (r += 1) %= 10000;
              }
            else
              (r += ans[i - 1][j - 1]) %= 10000;

          ans[i][j] = r;
          }

    ostringstream t;
    t << 10000 + ans[s.size() - 1][w.size()];

    printf("Case #%d: %s\n", ctest + 1, t.str().c_str() + 1);
    }

	return 0;
  }

