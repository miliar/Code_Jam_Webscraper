// P1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int length;
int n_words;
int n_tests;
vector<string> words;

int _tmain(int argc, _TCHAR* argv[])
  {
  cin >> length >> n_words >> n_tests;

  for (int i = 0; i < n_words; ++i)
    {
    string word;
    cin >> word;
    words.push_back(word);
    }

  for (int ctest = 0; ctest < n_tests; ++ctest)
    {
    string test;
    cin >> test;

    vector<string> tokens;
    for (size_t i = 0; i < test.size(); ++i)
      if (test[i] != '(')
        {
        tokens.push_back(string(1, test[i]));
        }
      else
        {
        string token = "";
        while (test[++i] != ')')
          token += test[i];
        tokens.push_back(token);
        }

    int ans = 0;
    if (tokens.size() == length)
      for (int i = 0; i < n_words; ++i)
        {
        bool ok = true;
        for (int j = 0; j < length; ++j)
          if (tokens[j].find(words[i][j]) == string::npos)
            ok = false;

        if (ok)
          ++ans;
        }

    printf("Case #%d: %d\n", ctest + 1, ans);
    }

	return 0;
  }


