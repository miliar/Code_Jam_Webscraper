#include <iostream>
#include <vector>
#include <string>

using namespace std;

int L, D, N;
vector<string> words;

int main()
{
  cin >> L >> D >> N;

  words.resize(D);
  for (int i = 0; i < D; i++) cin >> words[i];

  for (int i = 0; i < N; i++)
    {
      bool possible[15][26];
      for (int j = 0; j < L; j++)
	for (int k = 0; k < 26; k++)
	  possible[j][k] = false;

      string s;
      cin >> s;
      for (int j = 0; j < L; j++)
	{
	  if (s[0] == '(')
	    {
	      s.erase(0, 1);
	      while (s[0] >= 'a' && s[0] <= 'z')
		{
		  possible[j][s[0]-'a'] = true;
		  s.erase(0, 1);
		}
	      s.erase(0, 1);
	    }
	  else
	    {
	      possible[j][s[0]-'a'] = true;
	      s.erase(0, 1);
	    }
	}

      int ans = 0;
      for (int j = 0; j < D; j++)
	{
	  bool ok = true;
	  for (int k = 0; k < L; k++)
	    if (!possible[k][words[j][k]-'a'])
	      {
		ok = false;
		break;
	      }
	  if (ok) ans++;
	}
      cout << "Case #" << i+1 << ": " << ans << endl;
    }

  return 0;
}
