#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include <unistd.h>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>

using namespace std;

typedef std::pair<std::string, int> action_pair;
typedef std::vector<action_pair> action_list;

std::vector<action_list> actions;
std::vector<int> results;

void read(std::string const & filename);
void write(std::string const & filename);
int next(std::vector<action_list>::const_iterator al,  std::string const & robot, int from);

int main(int argc, char** argv)
{
	std::string input(argv[1]);

	read(input);

	for (std::vector<action_list>::const_iterator iter = actions.begin(); iter != actions.end(); ++iter)
	{
		int next_org = next(iter, std::string("O"), 0);
		int next_blu = next(iter, std::string("B"), 0);

		int current_org	= 1;
		int current_blu	= 1;
		int current		= 0;

		int sec	= 0;

		while (current < iter->size())
		{
			if (next_org < iter->size())
			{
				if (current_org < iter->operator[](next_org).second)
				{
					current_org++;
				}
				else if (current_org > iter->operator[](next_org).second)
				{
					current_org--;
				}
				else
				{
					// Orange action
					if (iter->operator[](current).first == "O")
					{
						current++;
						next_org = next(iter, std::string("O"), current);
	
						if (current_blu < iter->operator[](next_blu).second)
						{
							current_blu++;
						}
						else if (current_blu > iter->operator[](next_blu).second)
						{
							current_blu--;
						}

						sec++;
						continue;
					}
				}
			}

			if (next_blu < iter->size())
			{
				if (current_blu < iter->operator[](next_blu).second)
				{
					current_blu++;
				}
				else if (current_blu > iter->operator[](next_blu).second)
				{
					current_blu--;
				}
				else
				{
					// Blue action
					if (iter->operator[](current).first == "B")
					{
						current++;	
						next_blu = next(iter, std::string("B"), current);
					}
				}
			}
			
			std::cout << "STEP " << current_org << "\t" << current_blu << std::endl;

			sec++;
		}

		results.push_back(sec);	
	}

	write("101.out");

	return (EXIT_SUCCESS);
}

int next(std::vector<action_list>::const_iterator al, std::string const & robot, int from)
{
	int i = from;
	for (; i < al->size(); ++i)
	{
		if (al->operator[](i).first != robot) 
		{ 
			continue; 
		}
		else
		{
			break;
		}
	}
	return i;
}

void write(std::string const & filename)
{
	std::ofstream fout(filename.c_str());

	int c = 1;
	BOOST_FOREACH (int sec, results)
	{
		fout << "Case #" << c++ << ": " << sec << std::endl;
	}

	fout.close();
}

void read(std::string const & filename)
{
	std::ifstream fin(filename.c_str());

	std::string line;
	// First line is the number of testcast
	getline(fin, line);

	while (getline(fin, line))
	{
		std::vector< std::string > strs;
		boost::split(strs, line, boost::is_any_of("\t "));

		action_list tmp;
		for(int i = 1; i < strs.size(); i+=2)
		{
			tmp.push_back( std::make_pair(strs[i], boost::lexical_cast<int>(strs[i + 1])) );
		}

		// Save
		actions.push_back(tmp);
	}

	fin.close();
}

