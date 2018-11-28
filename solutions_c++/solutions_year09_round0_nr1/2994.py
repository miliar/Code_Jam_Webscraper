#include <string>
#include <iostream>
#include <fstream>
#include <vector>

int main(int argc, char * const argv[])
{
	unsigned L(0), D(0), N(0);
	std::ifstream input("inputlong.txt");

	input >> L >> D >> N; 

#ifdef _DEBUG

	std::cout << "L = " << L << std::endl;
	std::cout << "D = " << D << std::endl;
	std::cout << "N = " << N << std::endl;

	if (L < 1 || L > 15) std::cout << "WARNING : L out of range!" << std::endl;
	if (D < 1 || D > 5000) std::cout << "WARNING : D out of range!" << std::endl;
	if (N < 1 || N > 500) std::cout << "WARNING : N out of range!" << std::endl;

#endif // _DEBUG

	typedef std::vector<std::string> strvec;
	typedef std::vector<std::string>::iterator strveci;
	typedef std::string::size_type strsize;

	strvec words, tests;

	std::string temp;
	// just skip
	std::getline(input, temp);

	for (unsigned i(0); i < D; 
		std::getline(input, temp), words.push_back(temp), ++i);
	for (unsigned i(0); i < N; 
		std::getline(input, temp), tests.push_back(temp), ++i);

	input.close();

	std::ofstream output("outputlong.txt");

	unsigned test(1);
	for (strveci i(tests.begin()); i != tests.end(); ++i)
	{
		strsize l = (*i).length(), c(0);
		strvec characters;

		// built characters map, j is string index, c is map index
		for (strsize j(0); j < l; ++j, ++c)
		{
			characters.push_back("");
			if ('(' == (*i)[j])
			{
				// skip open bracket
				++j;
				if (')' != (*i)[j])
				{
					do characters.at(c).append(1, (*i)[j++]);
					while (')' != (*i)[j]);
				}
			}
			else
			{
				characters.at(c).append(1, (*i)[j]);
			}
#ifdef _DEBUG
			if (c >= L)
			{
				std::cout << "Too long test word : " << (*i) << std::endl;
				break;
			}
#endif // _DEBUG
		}
		// now characters map built, calculate how many words fit
		unsigned counter(0);
		for (strveci j(words.begin()); j != words.end(); ++j)
		{
			bool strmatch(true);

			for (strsize k(0); k < L; ++k)
			{
				std::string	character = characters.at(k);
				strsize cl = character.length();
				bool match(false);

				for (strsize idx(0); idx < cl; ++idx)
				{
					if ((*j)[k] == character[idx])
					{
						match = true;
						break;
					}
				}

				if (!match)
				{
					strmatch = false;
					break;
				}
			}

			counter = strmatch ? ++counter : counter;
		}
		// print output and increase test counter
		output << "Case #" << test++ << ": " << counter << std::endl;
	}
	output.close();

	return EXIT_SUCCESS;
}
