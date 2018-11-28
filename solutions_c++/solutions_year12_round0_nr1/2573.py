#include <fstream>
#include <string>
#include <algorithm>

using namespace std;


struct Mapping
{
	char english;
	char googlerese;
};

const Mapping MAPPINGS[] = 
{
	{'a', 'y'},
	{'b', 'h'},
	{'c', 'e'},
	{'d', 's'},
	{'e', 'o'},
	{'f', 'c'},
	{'g', 'v'},
	{'h', 'x'},
	{'i', 'd'},
	{'j', 'u'},
	{'k', 'i'},
	{'l', 'g'},
	{'m', 'l'},
	{'n', 'b'},
	{'o', 'k'},
	{'p', 'r'},
	{'q', 'z'},
	{'r', 't'},
	{'s', 'n'},
	{'t', 'w'},
	{'u', 'j'},
	{'v', 'p'},
	{'w', 'f'},
	{'x', 'm'},
	{'y', 'a'},
	{'z', 'q'},
	{' ', ' '},
};


class Translater
{
public:
	char operator()(char letter)
	{
		if (letter >= 'a' && letter <= 'z')
			return MAPPINGS[letter - 'a'].googlerese;

		return ' ';
	}
};


int main()
{
	using namespace std;

	ifstream ifs("A-small-attempt0.in");
	ofstream ofs("A-small-attempt0.out");

	string line;
	getline(ifs, line);

	int number = 1;
	while (getline(ifs, line))
	{
		ofs << "Case #" << number++ << ": ";

		transform(line.begin(), line.end(), ostream_iterator<char>(ofs), Translater());

		ofs << "\n";
	}

	return 0;
}
