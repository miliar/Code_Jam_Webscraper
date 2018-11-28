#include <map>
#include <vector>
#include <string>
#include <iomanip>
#include <fstream>
#include <iostream>

#include <unistd.h>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>

using namespace std;

std::vector< std::vector< unsigned int > > test_cases;
std::vector< int > results;

void read(std::string const & filename);
void write(std::string const & filename);

int main(int argc, char **argv)
{
	read(argv[1]);

	std::vector< std::vector< unsigned int > >::iterator iter = test_cases.begin();

	for (;iter != test_cases.end(); ++iter)
	{
		int correct = 0;

		for (int i = 0; i < iter->size(); ++i)
		{
			if (iter->operator[](i) == i + 1) { correct++; }
		}

		results.push_back(iter->size() - correct);
	}

	write("104.out");

	return (EXIT_SUCCESS);
}

void read(std::string const & filename)
{
	std::ifstream fin(filename.c_str());

	std::string line;
	// First line is the number of testcase
	getline(fin, line);

	int c = boost::lexical_cast< int >(line);

	for (int i = 0; i < c; ++i)
	{
		getline(fin, line);	
		getline(fin, line);

		std::vector< std::string > strs;
		boost::split(strs, line, boost::is_any_of("\t "));

		std::vector< unsigned int > tmp;
		BOOST_FOREACH (std::string s, strs)
		{
			tmp.push_back( boost::lexical_cast< unsigned int >(s) );
		}

		test_cases.push_back(tmp);
	}

	fin.close();
}

void write(std::string const & filename)
{
	std::ofstream fout(filename.c_str());

	int c = 1;
	BOOST_FOREACH (int i, results)
	{
		fout << "Case #" << c++ << ": " << std::setprecision(6) << fixed << double(i) << std::endl;
	}

	fout.close();
}

