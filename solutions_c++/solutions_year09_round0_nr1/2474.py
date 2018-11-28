#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

std::ifstream input;

std::ofstream output;

int wordLength = 0;
std::set<std::string> dictionary;

void TestCase(int testCase);

int main()
{
	input.open("A-small-attempt1.in");
	output.open("output.txt", std::ios_base::trunc);

	int numWords = 0;
	int numTestCases = 0;

	std::string buffer;
	std::getline(input, buffer);
	
	std::stringstream sstream(buffer);
	sstream >> wordLength;
	sstream >> numWords;
	sstream >> numTestCases;

	for(int i=0; i<numWords; ++i)
	{
		std::getline(input, buffer);
		dictionary.insert(buffer);
	}
	
	for(int i=0; i<numTestCases; ++i)
	{
		TestCase(i + 1);
	}

	output.close();
	input.close();

	return 0;
}

void LookForWordsR(const std::vector<std::string> &tokens, int curr, std::string word, int &numMatches)
{
	if(curr == tokens.size())
	{
		if(dictionary.find(word) != dictionary.end())
			++numMatches;

		return;
	}

	if(word.length() > 0)
	{
		bool bHit = false;
		std::string temp;
		for(std::set<std::string>::iterator iter=dictionary.begin(); iter!=dictionary.end(); ++iter)
		{
			temp = *iter;
			temp.erase(word.length());
			if(word == temp)
			{
				bHit = true;
				break;
			}
		}
		if(bHit == false)
			return;
	}

	for(unsigned int i=0; i<tokens[curr].size(); ++i)
	{
		LookForWordsR(tokens, curr+1, word + tokens[curr][i], numMatches);
	}
}
void LookForWords(const std::vector<std::string> &tokens, int &numMatches)
{
	LookForWordsR(tokens, 0, std::string(), numMatches);
}
void TestCase(int testCase)
{
	std::string buffer;
	std::getline(input, buffer);
	
	std::vector<std::string> tokens;

	bool inParens = false;
	for(unsigned int i=0; i<buffer.size(); ++i)
	{
		if(buffer[i] == '(')
		{
			inParens = true;
			tokens.push_back(std::string());
		}
		else if(buffer[i] == ')')
		{
			inParens = false;
		}
		else
		{
			if(inParens == false)
			{
				tokens.push_back(buffer.substr(i, i+1));
			}
			else
			{
				tokens.back() += buffer[i];
			}
		}
	}

	int numMatches = 0;
	LookForWords(tokens, numMatches);
	

	output << "Case #" << testCase << ": " << numMatches << '\n';
}
