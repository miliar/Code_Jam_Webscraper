// vim:ts=4:sw=4:cindent:
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <boost/lexical_cast.hpp>
#include <libgen.h> // basename

using std::istream;
using std::ostream;
using std::fstream;
using std::string;
using std::vector;
using std::list;
using std::map;

static istream *input = NULL;
static int case_num = 0;
#define output_case(x, y...) { case_num++; printf("Case #%d: "x, case_num, ##y); fflush(stdout); }
#ifdef DEBUG
# define debug(x, y...) { fprintf(stderr, x, ##y); }
#else
# define debug(x, y...) {}
#endif

void read_string(string& x)
{
	x.clear();
	(*input) >> x;
	if (x.size() == 0) {
		fprintf(stderr, "ERROR: Expecting a string from input file! (Got nothing instead.)\n");
		exit(1);
	}
}

void read_int(int& n)
{
	string x;
	read_string(x);

	try {
		n = boost::lexical_cast<int>(x);
	} catch (std::exception& e) {
		fprintf(stderr, "ERROR: Expecting an integer from input file! (Got \"%s\" instead.)\n", x.c_str());
		exit(1);
	}
}

void read_float(float& f)
{
	string x;
	read_string(x);

	try {
		f = boost::lexical_cast<float>(x);
	} catch (std::exception& e) {
		fprintf(stderr, "ERROR: Expecting a float from input file! (Got \"%s\" instead.)\n", x.c_str());
		exit(1);
	}
}

void do_problem();

int main(int argc, char **argv)
{
	if (argc > 2) {
		fprintf(stderr, "Usage: %s [ <file> ]\n", basename(argv[0]));
		fprintf(stderr, "If an input file is not specified, then stdin will be used.\n");
		exit(1);
	}

	if (argc == 1) {
		input = &std::cin;
		fprintf(stderr, "Reading from stdin.\n");
	} else {
		fstream *fin = new fstream();
		fin->open(argv[1], std::ios_base::in|std::ios_base::binary);
		if (fin->fail()) {
			fprintf(stderr, "Unable to open input file %s\n", argv[1]);
			exit(1);
		}
		input = fin;
	}

	do_problem();
	return 0;
}

