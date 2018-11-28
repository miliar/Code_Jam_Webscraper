#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

int L = 0;
int D = 0;
int N = 0;

bool check(const std::vector<std::map<char, int>>& pattern, const std::string& word)
{
	for (int i = 0 ; i < word.size() ;++i)
	{
		const std::map<char, int>& decipher = pattern.at(i);
		if (decipher.find(word.at(i)) == decipher.end())
		{
			return false;
		}
	}
	return true;
}

int checkPatternCount(const std::string& pattern, const std::vector<std::string>& wordList)
{
	int result = 0;
	std::vector<std::map<char, int>> patternDecipher;
	for (int i = 0 ; i < pattern.size() ;++i)
	{
		std::map<char, int> charDecipher;
		if (pattern.at(i) == '(')
		{
			for (; i < pattern.size() && pattern.at(i) != ')'; ++i)
			{
				charDecipher.insert(std::make_pair(pattern.at(i),1));
			}
		}
		else
		{
			charDecipher.insert(std::make_pair(pattern.at(i),1));
		}
		patternDecipher.push_back(charDecipher);
	}

	for (int i = 0 ; i < wordList.size(); ++i)
	{
		if (check(patternDecipher, wordList.at(i)))
		{
			++result;
		}
	}
	return result;
}

int main()
{
	std::ifstream input("C:\\in.txt");
	std::ofstream output("C:\\out.txt");

  input >> L >> D >> N;

  std::vector<std::string> wordList;
  wordList.reserve(D);

  std::vector<std::string> patternList;
  patternList.reserve(N);

  int d = D;
  while(d--)
  {
    std::string word;
    input >> word;
	wordList.push_back(word);
  }

  int n = N;
  while(n--)
  {
	  std::string pattern;
	  input >> pattern;
	  patternList.push_back(pattern);
  }

  std::vector<std::string> results;
  for (int i = 0 ; i < patternList.size() ; ++i)
  {
	  int count = checkPatternCount(patternList.at(i), wordList);
	  std::stringstream str;
	  str << "Case #" << i + 1 << ": " << count;
	  results.push_back(str.str());
  }

  for (int i = 0; i  <results.size() ; ++i)
  {
	  output << results.at(i) << std::endl;
  }
}