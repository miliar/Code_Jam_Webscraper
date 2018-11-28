/***********************************
 *
 * Prblem A
 * Googlerese decoder
 *
 * by Jesus Armando Anaya Orozco
 *
 * jesus.anaya.dev@gmail.com
 *
 **********************************/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <list>
#include <cstring>

class Googlerese
{
	public:
		Googlerese();

		void Decoder(std::string filename);
		bool DecodeALine(std::string& line);
		void OutputResult();

	private:
		std::map<char, char> trans;
		std::list<std::string> lines;
		bool error;
};

/*
Sample Code
	
Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/

Googlerese::Googlerese(): error(false)
{
	// create a map to translate each word
	trans['a'] = 'y';
	trans['b'] = 'h';
	trans['c'] = 'e';
	trans['d'] = 's';
	trans['e'] = 'o';
	trans['f'] = 'c';
	trans['g'] = 'v';
	trans['h'] = 'x';
	trans['i'] = 'd';
	trans['j'] = 'u';
	trans['k'] = 'i';
	trans['l'] = 'g';
	trans['m'] = 'l';
	trans['n'] = 'b';
	trans['o'] = 'k';
	trans['p'] = 'r';
	trans['q'] = 'z';
	trans['r'] = 't';
	trans['s'] = 'n';
	trans['t'] = 'w';
	trans['u'] = 'j';
	trans['v'] = 'p';
	trans['w'] = 'f';
	trans['x'] = 'm';
	trans['y'] = 'a';
	trans['z'] = 'q';
	trans[' '] = ' ';
}

void Googlerese::Decoder(std::string filename)
{
	char buffer[255];
	std::string line;
	std::ifstream input_file(filename, std::ifstream::in);

	if(input_file.is_open())
	{
		while(!input_file.eof())
		{
			// get a line from file
			std::memset(buffer, 0, 255);
			input_file.getline(buffer, 255);
			line = buffer;

			// decode each line
			if(DecodeALine(line))
			{
				// add line to lines list
				lines.push_back(line);
			}
		}
	}
	else
	{
		error = true;
		std::cerr << "Error open file" << std::endl;
	}
}

bool Googlerese::DecodeALine(std::string& line)
{
	if(line.size() > 2)
	{
		for(unsigned int i = 0; i < line.size(); i++)
		{
			line[i] = trans[line[i]]; 
		}
		return true;
	}
	return false;
}

void Googlerese::OutputResult()
{
	if(!error)
	{
		std::ofstream output_file("result.txt", std::ofstream::out);
		std::list<std::string>::iterator it;
		int i = 1;

		for(it = lines.begin(); it != lines.end(); it++, i++)
		{
			output_file << "Case #" << i << ": " << ((std::string)*it) << std::endl;
		}

	}
}

int main(int argc, char *argv[])
{
	Googlerese gerese = Googlerese();
	
	if(argc == 2)
	{
		gerese.Decoder(argv[1]);
		gerese.OutputResult();
	}
	else
	{
		std::cerr << "Error, not correct namefile as parameter" << std::endl;
	}
	return 0;
}