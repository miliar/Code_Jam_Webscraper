#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int t; cin >> t;

  for (int i = 0; i < t; ++i)
  {
    char combines[26][26] = { 0 };
    char opposes [26][26] = { 0 };

    int c; cin >> c;

    for (int j = 0; j < c; ++j)
    {
      char base_1; cin >> base_1;
      char base_2; cin >> base_2;
      char comb  ; cin >> comb;

      combines[base_1-'A'][base_2-'A'] = comb;
      combines[base_2-'A'][base_1-'A'] = comb;
    }

    int d; cin >> d;

    for (int j = 0; j < d; ++j)
    {
      char base_1; cin >> base_1;
      char base_2; cin >> base_2;

      opposes[base_1-'A'][base_2-'A'] = 1;
      opposes[base_2-'A'][base_1-'A'] = 1;
    }

    int n; cin >> n;
    
    vector<char> elist;

    for (int j = 0; j < n; ++j)
    {
      char elem; cin >> elem;
      
      if (elist.size() > 0)
      {
        if (combines[elem-'A'][elist.back()-'A'])
          elist.back() = combines[elem-'A'][elist.back()-'A'];
        else
        {
          bool clear = false;

          for (int k = 0; k < elist.size(); ++k)
            if (opposes[elem-'A'][elist[k]-'A'])
            {
              clear = true;
              break;
            }
          
          if (clear)
            elist.clear();
          else
            elist.push_back(elem);
        }
      }
      else
      {
        elist.push_back(elem);
      }
    }

    cout << "Case #" << (i+1) << ": [";

    for (int j = 0; j < elist.size(); ++j)
    {
      cout << elist[j];
      if (j != elist.size()-1)
        cout << ", ";
    }

    cout << "]" << endl;
  }

  return 0;
}

