#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/trim.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <sstream>

template<typename RT, typename T, typename Trait, typename Alloc>
RT str_convert( const std::basic_string<T, Trait, Alloc>& the_string )
{
	std::basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
	RT num;
	temp_ss >> num;
	return num;
}

struct Language
{
	void clear()
	{
		words.clear();
	}
	std::vector<std::string> words;
	int dictSize;
	int wordLength;
};

class Case
{
public:
	Case() : matchingCounter(0){};
	friend std::istream& operator >> (std::istream& inStr, Case& outCase);
	friend std::ostream& operator << (std::ostream& outStr, Case& inCase);
	void checkLanguage(Language& inLang)
	{
		for(unsigned i = 0; i < inLang.words.size(); ++i)
			checkMatch(inLang.words[i]);
	}
private:
	void checkMatch(std::string& inString)
	{
		if(inString.size() != possibleWord.size())
			std::cerr << "Something went really wrong with input...";
		bool isOk = true;
		for(unsigned i = 0; i < possibleWord.size(); ++i)
		{
			if(possibleWord.at(i).find(inString[i]) == std::string::npos)
				isOk = false;
		}
		if(isOk)
			matchingCounter++;
	}
	std::vector<std::string> possibleWord;
	int matchingCounter;
};
std::istream& operator >> (std::istream& inStr, Language& outLang)
{
	std::string line;
	for(int i = 0; i < outLang.dictSize; ++i)
	{
		std::getline(inStr, line);
		boost::algorithm::trim(line);
		outLang.words.push_back(line);
	}
	return inStr;
}

std::istream& operator >> (std::istream& inStr, Case& outCase)
{
	std::string line;
	std::getline(inStr, line);
	boost::algorithm::trim(line);
	std::string tmp;
	bool opened = false;
	for(unsigned i = 0; i < line.size(); ++i)
	{
		if(line[i] == '(')
		{
			opened = true;
			if(tmp.empty())
				continue;
			else
			{
				outCase.possibleWord.push_back(tmp);
				tmp.clear();
			}
		}
		else if(line[i] == ')')
		{
			opened = false;
			if(tmp.empty())
				continue;
			else
			{
				outCase.possibleWord.push_back(tmp);
				tmp.clear();
			}
		}
		else
		{
			tmp.push_back(line[i]);
			if(!opened)
			{
				outCase.possibleWord.push_back(tmp);
				tmp.clear();
			}
		}
	}
	if(!tmp.empty())
		outCase.possibleWord.push_back(tmp);
	return inStr;
}

std::ostream& operator << (std::ostream& outStr, Case& inCase)
{
	outStr << inCase.matchingCounter;
	return outStr;
}


int main( int argc, char* argv[] )
{
	std::string inFilename = "input.txt";
	std::string outFilename = "output.txt";
	if(argc > 1)
	{
		inFilename = argv[1];
	}
	if(argc > 2)
	{
		outFilename = argv[2];
	}
	std::ifstream inFile(inFilename.c_str(), std::ios_base::in);
	if(!inFile.is_open())
	{
		std::cerr << "Unable to open file: " << inFilename;
		return 1;
	}
	std::ofstream outFile(outFilename.c_str(), std::ios_base::out | std::ios_base::trunc);
	if(!outFile.is_open())
	{
		std::cerr << "Unable to open file: " << outFilename;
		inFile.close();
		return 2;
	}
	std::string line;
	std::getline(inFile, line);
	std::vector<std::string> strings;
	boost::algorithm::split(strings, line, boost::algorithm::is_any_of(" "));
	int caseNum;
	Language lang;
	lang.wordLength = str_convert<int>(strings[0]);
	lang.dictSize = str_convert<int>(strings[1]);
	caseNum = str_convert<int>(strings[2]);
	inFile >> lang;
	for(int i = 0; i < caseNum; ++i)
	{
		Case tmp;
		inFile >> tmp;
		tmp.checkLanguage(lang);
		std::cout << "Case #" << i+1 << std::endl;
		outFile << "Case #" << i+1 << ": " << tmp << std::endl;
	}


	inFile.close();
	outFile.close();
}
