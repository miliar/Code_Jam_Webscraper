#include <iostream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
  int L = 0;
  cin >> L;
  int D = 0;
  cin >> D;
  int N = 0;
  cin >> N;
  
  vector<string> lang(D);

  int i;
  for(i = 0; i < D; ++i)
  {
    //char szEngine[101];
    //cin.getline(szEngine, sizeof(szEngine));
    // ignore engine names
    
    cin >> lang[i];
  }

  for(i = 0; i < N; ++i)
  {
    string patternStr;
    cin >> patternStr;

    vector<bitset<'z'-'a' + 1> > pattern(L);

    int letter = 0;
    int j;
    for(j = 0; j < patternStr.size(); ++j)
    {
      if (patternStr[j] == '(')
      {
        ++j;
        while(patternStr[j] != ')')
        {
          pattern[letter].set(patternStr[j] - 'a');
          ++j;
        }
      }
      else
      {
        pattern[letter].set(patternStr[j] - 'a');
      }

      ++letter;
    }

    int res = 0;
    for(j = 0; j < D; ++j)
    {
      int k;
      for(k = 0; k < L; ++k)
      {
        if (!pattern[k].test(lang[j][k] - 'a'))
        {
          break;
        }
      }

      if (k == L)
      {
        ++res;
      }
    }

    cout << "Case #" << (i + 1) << ": " << res << endl;
  }
  
  return 0;
}

