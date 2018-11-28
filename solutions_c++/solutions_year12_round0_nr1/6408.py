#include <map>
#include <cassert>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;


string translate(const string& s)
{
	map<char, char> mapper;

	mapper['a'] = 'y';
	mapper['b'] = 'h';
	mapper['c'] = 'e';
	mapper['d'] = 's';
	mapper['e'] = 'o';
	mapper['f'] = 'c';
	mapper['g'] = 'v';
	mapper['h'] = 'x';
	mapper['i'] = 'd';
	mapper['j'] = 'u';
	mapper['k'] = 'i';
	mapper['l'] = 'g';
	mapper['m'] = 'l';
	mapper['n'] = 'b';
	mapper['o'] = 'k';
	mapper['p'] = 'r';
	mapper['q'] = 'z';
	mapper['r'] = 't';
	mapper['s'] = 'n';
	mapper['t'] = 'w';
	mapper['u'] = 'j';
	mapper['v'] = 'p';
	mapper['w'] = 'f';
	mapper['x'] = 'm';
	mapper['y'] = 'a';
	mapper['z'] = 'q';

	assert(mapper.size() == 'z' - 'a' + 1);

	string ret(s);
	for (size_t i=0; i<ret.size(); ++i)
	{
		const char c = s[i];

		if (c == ' ')
			continue;

		assert(c >= 'a' && c <= 'z');
		
		const char new_char = mapper[c];
		assert(new_char >= 'a' && new_char <= 'z');
		
		ret[i] = new_char;
	}

	return ret;
}

void solve(istream& is, ostream& os)
{
	size_t num_cases;
	is >> num_cases;

	char line[256];
	is.getline(line, sizeof(line));
	
	assert(num_cases >= 1 && num_cases <= 30);

	for (size_t i=0; i<num_cases; ++i)
	{
		char line[256];
		is.getline(line, sizeof(line));

		os << "Case #" << i+1 << ": " << translate(line) << "\n";
	}
}

void unittests()
{
	{
		const string translated = translate("ejp mysljylc kd kxveddknmc re jsicpdrysi");
		assert(translated== "our language is impossible to understand");
	}

	{
		const string translated = translate("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
		assert(translated == "there are twenty six factorial possibilities");
	}
	
	{
		const string translated = translate("de kr kd eoya kw aej tysr re ujdr lkgc jv");
		assert(translated == "so it is okay if you want to just give up");
	}

	{
		const string translated = translate("y qee");
		assert(translated == "a zoo");
	}

	{
		istringstream is("3\n"
		                 "ejp mysljylc kd kxveddknmc re jsicpdrysi\n"
		                 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n"
		                 "de kr kd eoya kw aej tysr re ujdr lkgc jv\n");

		ostringstream os;
		solve(is, os);
		const string expected =
			"Case #1: our language is impossible to understand\n"
			"Case #2: there are twenty six factorial possibilities\n"
			"Case #3: so it is okay if you want to just give up\n";

		const string translated = os.str();
		assert(translated == expected);
	}
}

int main(int argc, char* argv[])
{
	//unittests();
	solve(cin, cout);
}

