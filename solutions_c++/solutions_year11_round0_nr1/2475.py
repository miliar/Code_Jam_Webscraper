#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int T; cin >> T;
  for (int i = 0; i < T; ++i)
  {
    int n; cin >> n;

    int opos = 1; int lastot = 0;
    int bpos = 1; int lastbt = 0; 
    int t    = 0;

    for (int j = 0; j < n; ++j)
    {
      char bot; cin >> bot;
      int  but; cin >> but;
      
      if (bot == 'O')
      {
        t += max(0, abs(but - opos) - (t-lastot)) + 1;
        lastot = t;
        opos   = but;
      }
      else
      {
        t += max(0, abs(but - bpos) - (t-lastbt)) + 1;
        lastbt = t;
        bpos   = but;
      }
    }

    cout << "Case #" << (i+1) << ": " << t << endl;
  }
    
  return 0;
}
