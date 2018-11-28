#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>

using namespace std;

#define FOR(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int main(void)
{
  ifstream infile("input.txt");
  int lines;
  int googlers;
  int surprises;
  int passValue;
  int total;
  int count;
  int val;
  int mod;
  
  infile >> lines;
  
  FOR(i, lines)
  {
    count = 0;
    infile >> googlers >> surprises >> passValue;
    cout << "Case #" << i + 1 << ": ";
    if(!passValue)
    {
      count = googlers;
      FOR(ii, googlers)
        infile >> total;
    }
    else
    {
      FOR(ii, googlers)
      {
        infile >> total;
        val = total / 3;
        
        if(val >= passValue)
        {
          ++count;
          continue;
        }
        
        mod = total - 3 * val;
        
        switch(passValue - val)
        {
          case 2:
            if(surprises && mod == 2)
            {
              ++count;
              --surprises;
            }
            break;
          case 1:
            if(mod > 0)
            {
              ++count;
            }
            else if(surprises && total)
            {
              ++count;
              --surprises;
            }
            break;
          default:
            break;
        }
      }
    }
    cout << count << endl;
  }
  
  return 0;
}