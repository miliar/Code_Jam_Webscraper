#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>

int main(int argc, char** argv)
{
	std::string output =  "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo";
	std::string input = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee";
	std::vector<char> toGooglerese(256, '_');
	std::set<char> inputChars;
	std::set<char> outputChars;

	for( char c= 'a'; c <= 'z'; ++c)
	{
		inputChars.insert(c);
		outputChars.insert(c);
	}

	for( size_t i = 0; i < input.size(); ++i)
	{
		inputChars.erase(input[i]);
		outputChars.erase(output[i]);
		toGooglerese[input[i]] = output[i];
	}

	if( inputChars.size() != 1 && outputChars.size() != 1)
		throw std::runtime_error("Error");

	toGooglerese[*inputChars.begin()] = *outputChars.begin();
	std::cout << *inputChars.begin() << "->" << *outputChars.begin() << std::endl;

	for( char c= 'a'; c <= 'z'; ++c)
		std::cout << c << ":" << toGooglerese[c] << " ";
	std::cout << std::endl;

	for( size_t i = 0; i < input.size(); ++i)
	{
		std::cout << toGooglerese[input[i]];
	}
	std::cout << std::endl;

	int nbTest = 1;
	std::ifstream ifs( "Debug/A-small-attempt0.in");
	std::ofstream file( "Debug/A-small-attempt0.out" );
	ifs >> nbTest;
	std::string line;
	std::getline(ifs, line);

	for( int test = 1; test <= nbTest; ++test )
	{


		std::getline(ifs, line);

		file << "Case #" << test << ": ";
		for( int i = 0; i < line.size(); ++i)
			file << toGooglerese[line[i]];
		file << std::endl;
	}
	std::cout << "Finish" << std::endl;
	return 0;
}
