#include <iostream>
#include <bitset>
#include <vector>

using namespace std;

int main()
{
  freopen("words.txt", "r", stdin);
  freopen("wordsOut.txt", "w", stdout);
  int l, d, n;
  cin >> l >> d >> n;

  vector<string> words(d);

  for (int i = 0; i < d; ++i)
    cin >> words[i];

  for (int test = 0; test < n; ++test)
  {
    string word;
    cin >> word;

    std::vector<bitset<26> > wordSet(word.size());
    int j = 0;
    bool in = false;
    for (int i = 0; i < word.size(); ++i)
    {
      char ch = word[i];
      if (ch == '(')
      {
        in = true;
        continue;
      }

      if (ch == ')')
      {
        in = false;
        ++j;
        continue;
      }

      wordSet[j].set(ch - 'a');
      if (!in)
      {
        ++j;
      }
    }

    int result = 0;

    if (j == l)
    {
      for (int i = 0; i < words.size(); ++i)
      {
        bool ok = true;
        for (int j = 0; j < words[i].size(); ++j)
        {
          ok &= wordSet[j].test(words[i][j] - 'a');
        }

        result += ok == true;
      }
    }

    cout << "Case #" << (test + 1) << ": " << result << "\n";
  }

  return 0;
}