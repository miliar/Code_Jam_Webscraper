#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

int main()
{
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);

  int T;
  string s;
  string result;
  bool dot;

  cin>>T;
  getline(cin,s);
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);

    dot = false;
    int xrow[4] = {0};
    int xcol[4] = {0};
    int xdiagn = 0;
    int xdiagp = 0;
    int yrow[4] = {0};
    int ycol[4] = {0};
    int ydiagn = 0;
    int ydiagp = 0;


    //read data
    for (int i = 0; i < 4; ++i)
    {
      getline(cin, s);
      for (int j = 0; j < 4; ++j)
      {
        if (s[j] == '.') dot = true;
        if(s[j] == 'X' || s[j] == 'T')
        {
          if (i==j) ++xdiagn;
          if (i+j==3) ++xdiagp;
          ++xrow[i];
          ++xcol[j];
        }
        if (s[j] == 'O' || s[j] == 'T')
        {
          if (i==j) ++ydiagn;
          if (i+j==3) ++ydiagp;
          ++yrow[i];
          ++ycol[j];
        }
      }
    }
    //consume empty line
    getline(cin, s);

    //check win
    bool xwon = false;
    bool ywon = false;
    for (int i = 0; i < 4; ++i)
    {
      if (xrow[i] == 4 || xcol[i] == 4)
      { 
        xwon = true; 
        break;
      }

      //cout<<yrow[i]<<ycol[i]<<endl;

      if (yrow[i] == 4 || ycol[i] == 4)
      { 
        ywon = true; 
        break;
      }
    }

    if (xwon || xdiagp == 4 || xdiagn == 4)
    {  
      printf("X won\n");
      continue;
    }

    if (ywon || ydiagp == 4 || ydiagn == 4)
    {
      printf("O won\n");
      continue;
    }

    if (dot) printf("Game has not completed\n");
    else printf("Draw\n");

  }
}
