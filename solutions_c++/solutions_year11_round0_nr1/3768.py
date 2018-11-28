#include <iostream>
#include "parse_file.h"

using std::cerr;

int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		cerr<<"Usage: bot_trust <infile> <outfile>\n";
		return 1;
	}
	try
	{
	    parsed_file p = ParseInFile(argv[1]);
		AnswersToFile(argv[2], p);
	}
	catch(std::exception& e)
	{
		cerr<<"Error: "<<e.what()<<"\n";
		return 1;
	}
	return 0;
}

