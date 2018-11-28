#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <windows.h>

int main(int argc, const char* argv[])
{
	long int before = GetTickCount();

	if(argc != 2)
	{
		std::cerr << "Invalid argument number (" << argc << ")." << std::endl;
		exit(1);
	}

	std::ifstream is(argv[1]);
	std::ofstream os("output");

	if (!is)
	{
		std::cerr << "File '" << argv[1] << "' could not be opened." << std::endl;
		exit(1);
	}

	int test_cases;
	is >> test_cases;

	unsigned long long int rides, capacity;
	long int group_size;
	int group_nr;
	std::vector<long int> groups;
	for(int i = 1; i <= test_cases; ++i)
	{
		groups.clear();
		is >> rides >> capacity >> group_nr;
		for(int j = 1; j <= group_nr; ++j)
		{
			is >> group_size;
			groups.push_back(group_size);
		}

		unsigned long long int euros = 0;
		long int boarded_people = 0;
		long int people = 0;
		int first = 0;
		int last = 0;

		for (unsigned j = 0; j < groups.size(); ++j)
			people += groups.at(j);

		if(capacity >= people)
			euros = people*rides;

		for (unsigned long int r = 0; r < rides && capacity < people; ++r)
		{
			for (unsigned k = first; k < groups.size();)
			{
				if((boarded_people + groups.at(k)) <= capacity)
				{
					boarded_people += groups.at(k);
					last = k++;
				}
				else break;

				if (k == group_nr)
				{
					k = 0;
					continue;
				}
			}
			euros += boarded_people;
			boarded_people = 0;
			first = (last == group_nr-1) ? 0 : last+1;
		}

		std::cout << "Case #" << i << ": " << euros << std::endl;
		os << "Case #" << i << ": " << euros << std::endl;
	}

	os.close();
	long int after = GetTickCount();
	std::cout << "Execution time: " <<((after-before)/1000) << "s." << std::endl;
	return 0;
}
