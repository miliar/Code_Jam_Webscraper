// AlienLanguage.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[])
{
  int L, D, N;
  std::cin >> L >> D >> N;
  std::vector<std::string> words;
  for(int i = 0; i < D; ++i)
  {
    std::string word;
    std::cin >> word;
    words.push_back(word);
  }
  for(int i = 0; i < N; ++i)
  {
    std::vector<unsigned int> pattern;
    for(int j = 0; j < L; ++j)
    {
      unsigned int letter = 0;
      bool open = false;
      do {
        char c;
        std::cin >> c;
        if(c >= 'a' && c <= 'z')
          letter |= (1<<(c-'a'));
        if(c == '(')
          open = true;
        if(c == ')')
          break;
      } while(letter == 0 || open);
      pattern.push_back(letter);
    }
    int count = 0;
    for(int j = 0; j < D; ++j)
    {
      std::string word = words[j];
      bool good = true;
      for(int k = 0; k < L; ++k)
      {
        if(((1<<(word[k]-'a'))&pattern[k])==0)
        {
          good = false;
          break;
        }
      }
      if(good)
        count++;
    }
    std::cout << "Case #" << (i+1) << ": " << count << "\n";
  }
	return 0;
}

