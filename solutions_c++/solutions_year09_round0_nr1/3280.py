#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

unsigned int count;
std::set<std::string> words;

void generateStrings(const std::vector<std::string>& options, std::string str, unsigned int pos)
{
	bool flag = false;
	for(std::set<std::string>::const_iterator i = words.begin(); (i != words.end()) && (flag == false); i++)
	{
		if(i->substr(0, str.length()) == str)
		{
			flag = true;
		}
	}

	if(flag == false)
	{
		return;
	}

	if((flag == true) && (pos == options.size()))
	{
		count++;
		return;
	}

	for(unsigned int i = 0; i < options[pos].length(); i++)
	{
		generateStrings(options, str + options[pos][i], pos + 1);
	}
}

int main(int argc, char **argv)
{
	std::ifstream input("C:/A-small-attempt2.in");
	if(input.is_open() == false)
	{
		std::cout << "Unable to open input file." << std::endl;
		return 1;
	}

	std::ofstream output("C:/A-small-attempt2.out");
	if(output.is_open() == false)
	{
		std::cout << "Unable to open output file." << std::endl;
		input.close();
		return 1;
	}

	unsigned int L, D, N;
	input >> L >> D >> N;
	input.get();
	for(unsigned int i = 0; i < D; i++)
	{
		std::string word;
		std::getline(input, word);
		words.insert(word);
	}

	for(unsigned int i = 0; i < N; i++)
	{
		std::string line;
		std::getline(input, line);
		std::vector<std::string> v;
		unsigned int j = 0;
		while(j < line.length())
		{
			if(line[j] == '(')
			{
				unsigned int end = line.find(')', j);
				v.push_back(line.substr(j + 1, end - j - 1));
				j = end + 1;
			}
			else
			{
				v.push_back(std::string(1, line[j]));
				j++;
			}
		}


		count = 0;
		generateStrings(v, "", 0);
		output << "Case #" << (i + 1) << ": " << count << std::endl;
	}

	input.close();
	output.close();
}