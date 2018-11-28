#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
    int C;
    cin >> C;
    const int m = 'Z' - 'A' + 1;
    char comb[m][m];
    for(int i = 0; i < m; i++)
    {
      for(int j = 0; j < m; j++)
      {
        comb[i][j] = 0;
      }
    }
    for(int i = 0; i < C; i++)
    {
      string s;
      cin >> s;
      comb[s[0]-'A'][s[1]-'A'] = s[2];
      comb[s[1]-'A'][s[0]-'A'] = s[2];
    }
    int D;
    cin >> D;
    char opp[m][m];
    for(int i = 0; i < m; i++)
    {
      for(int j = 0; j < m; j++)
      {
        opp[i][j] = 0;
      }
    }
    for(int i = 0; i < D; i++)
    {
      string s;
      cin >> s;
      opp[s[0]-'A'][s[1]-'A'] = 1;
      opp[s[1]-'A'][s[0]-'A'] = 1;
    }
    int N;
    cin >> N;
    string s;
    cin >> s;
    vector<char> in(s.rbegin(), s.rend());
    vector<char> f;

    while(!in.empty())
    {
      f.push_back(in.back());
      in.pop_back();
      while(f.size() >= 2)
      {
        char a = f.at(f.size() - 1);
        char b = f.at(f.size() - 2);
        if(comb[a - 'A'][b - 'A'] != 0)
        {
          f.pop_back();
          f.pop_back();
          f.push_back(comb[a - 'A'][b - 'A']);
        }
        else
        {
          break;
        }
      }
      if(f.size() >= 2)
      {
        char a = f.at(f.size() - 1);
        for(size_t i = 0; i < f.size() - 1; i++)
        {
          if(opp[a - 'A'][f.at(i) - 'A'] != 0)
          {
            f.clear();
            break;
          }
        }
      }
    }

    cout << "Case #" << t << ": [";
    for(size_t i = 0; i < f.size(); i++)
    {
      cout << f.at(i);
      if(i != f.size() - 1)
      {
        cout << ", ";
      }
    }
    cout << "]" << endl;
  }
}

