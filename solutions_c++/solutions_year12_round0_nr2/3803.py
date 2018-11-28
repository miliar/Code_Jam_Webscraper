#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int casenumber = 1; casenumber <= T; casenumber++)
  {
    int N; cin >> N;
    int S; cin >> S;
    int p; cin >> p;
    vector<int> googlers;
    for (int i =0; i < N; ++i)
    {
      int t; cin >> t;
      googlers.push_back(t);
    }
    sort(googlers.begin(), googlers.end(), less<int>());
    int count = 0;
    for (int i = 0; i < googlers.size(); ++i)
    {
      int n;
      bool flag = true;
      if (S > 0)
      {
        bool flag2 = true;
        switch(googlers[i] % 3)
        {
          case 0:
          {
            n = (googlers[i] + 3)/3;            
            break;
          }
          case 1:
          {
            n = (googlers[i] + 2)/3;
            break;
          }
          case 2:
          {
            n = (googlers[i] + 4)/3;
          }
        }
        flag2 = n>= 2 and n <= 10;
        if (n >= p and n > 1) 
        { 
          ++count;
          --S;    
          flag = false;
        }
      }
      if (flag)
      {
        bool flag2 = false;
        switch(googlers[i] % 3)
        {
          case 0:
          {
            n = (googlers[i])/3;
            flag2 = (n >= 0 and n <= 10);
            break;
          }
          case 1:
          {
            n = (googlers[i] + 2)/3;
            flag2 = n>=1 and n<= 10;
            break;
          }
          case 2:
          {
            n = (googlers[i] + 1)/3;
            flag2 = n>= 1 and n<= 10;
          }
        }
        if (n >= p and flag2)
        { 
          ++count;
        }
      }
    }
    cout << "Case #" << casenumber << ": " << count << endl;
  }
}