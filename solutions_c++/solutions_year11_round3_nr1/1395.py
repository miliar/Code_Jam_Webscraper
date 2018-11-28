#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

char pic[51][51];

int main(int argc,char **args)
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int testcase;
  cin>>testcase;
  for (int caseId=1;caseId<=testcase; caseId++)
  {
    printf("Case #%d:\n",caseId);
    int R, C;
    cin>>R>>C;
    for(int i = 0; i < R; ++i)
      for(int j = 0; j < C; ++j)
      {
        cin>>pic[i][j];
      }
    /*
    for(int i = 0; i < R; ++i)
    {
      for(int j = 0; j < C; ++j)
        cerr<<pic[i][j];
      cerr<<endl;
    }*/
    bool possible = true;
    for(int i = 0; i < R; ++i)
    {
      for(int j = 0; j < C; ++j)
      {
        if(pic[i][j] == '#' && (i==R-1 || j == C-1))
        {
          possible = false;
          break;
        }
        if(pic[i][j] == '#' && pic[i][j+1] == '#' && pic[i+1][j] == '#' && pic[i+1][j+1] == '#')
        {
          pic[i][j]='/';
          pic[i][j+1]='\\';
          pic[i+1][j]='\\';
          pic[i+1][j+1]='/';
        }
      }
    }
    for(int i = 0; i < R; ++i)
    {
      for(int j = 0; j < C; ++j)
      {
        if(pic[i][j] == '#')
        {
          possible = false;
          break;
        }
      }
    }
    if(!possible)
    {
      cerr<<"Impossible\n";
      cout<<"Impossible\n";
    }
    else
    {
      for(int i = 0; i < R; ++i)
      {
        for(int j = 0; j < C; ++j)
        {
          cerr<<pic[i][j];
          cout<<pic[i][j];
        }
        cerr<<endl;
        cout<<endl;
      }
    }
    fflush(stdout);
  }
  return 0;
}