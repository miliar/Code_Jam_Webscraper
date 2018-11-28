#include <iostream>
#include <string>
#include <fstream>
#include <boost/lexical_cast.hpp>
#include <vector>

std::vector<std::string> words;

void getAns(int* matches, const std::vector<std::string>* v, std::string w, unsigned int pos)
{
  int a = 0;

  // Each group of letters
  if (pos < v->size())
  {
    std::string s = v->at(pos);

    // Each permutation of characters
    for (unsigned int j = 0; j < s.size(); ++j)
    {
      w.push_back(s.at(j));
      // Each word in dictionary
      for (unsigned int k = 0; k < words.size(); ++k)
      {
        
        if (words.at(k).substr(0, pos+1) == w)
        {
          getAns(matches, v, w, pos+1);
          if (pos == v->size() - 1)
            (*matches)++;
          break;
        }
      }
      w.erase(pos);
    }
  }
}

int main(int argc, char* argv[])
{
  std::fstream inFile(argv[1]);
  std::string input;
  inFile >> input;
  int wordLength = boost::lexical_cast<int>(input);
  inFile >> input;
  int numWords = boost::lexical_cast<int>(input);
  inFile >> input;
  int numCases = boost::lexical_cast<int>(input);

  // Words
  for (int i = 0; i < numWords; ++i)
  {
    inFile >> input;
    words.push_back(input);
  }

  // Test cases
  for (int i = 1; i <= numCases; ++i)
  {
    inFile >> input;
    std::vector<std::string>* permutations;
    permutations = new std::vector<std::string>;
    for (unsigned int j = 0; j < input.size(); ++j)
    {
      if (input.at(j) == '(')
      {
        ++j;
        std::string c;
        while (input.at(j) != ')')
        {
          c.push_back(input.at(j++));
        }
        permutations->push_back(c);
      }
      else
      {
        // Damn you C++
        std::string c;
        c.push_back(input.at(j));
        permutations->push_back(c);
      }
    }

    int answer = 0;
    std::string s = "";
    getAns(&answer, permutations, s, 0);
    std::cout << "Case #" << i << ": " << answer << "\n";
  }

  inFile.close();
  return 0;
}