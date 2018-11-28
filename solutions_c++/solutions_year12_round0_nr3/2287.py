#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>


size_t Solve(int a, int b)
{
	std::set<std::pair<int, int> > recycled;

	for( size_t i = a; i <=b; ++i)
	{
		std::ostringstream ostr;

		ostr << i;
		std::string number = ostr.str();

	//	std::cout << i << std::endl;
		for( size_t j = 1; j < number.size(); ++j)
		{
			std::string newNumber = number.substr(j, number.size() - j) + number.substr(0, j);

			if (newNumber >= number )
			{
				std::istringstream istr(newNumber);
				size_t newNumberValue;
				istr >> newNumberValue;

				if(newNumberValue >= a && newNumberValue <= b && i < newNumberValue)
				{
				//	std::cout << i << " " << newNumberValue << std::endl;
					recycled.insert(std::make_pair(i, newNumberValue));
				}
			}
		}

	}
	//for(std::set<std::pair<int,int> >::const_iterator it = recycled.begin(); it != recycled.end(); ++it )
	//	std::cout << it->first << " " << it->second << std::endl;
	return recycled.size();
}

int main(int argc, char** argv)
{
	int nbTest = 0;
	std::ifstream ifs( "Debug/C-large.in");
	std::ofstream file( "Debug/C-large.out" );

	ifs >> nbTest;
	std::string line;
	std::getline(ifs, line);

	for( int test = 1; test <= nbTest; ++test )
	{
		int a, b;

		ifs >> a;
		ifs >> b;

		size_t maxScore = Solve(a, b);

		std::cout << test << ":" << maxScore << std::endl;
		file << "Case #" << test << ": "<<  maxScore << std::endl;
	}
	std::cout << "Finish" << std::endl;
	return 0;
}
