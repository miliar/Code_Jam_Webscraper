#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;

	infile.open("A-small-attempt0.in", ifstream::in);
	outfile.open ("output");

	if( (infile != NULL) && (outfile != NULL) )
	{
		int i = 1;
		char ch = 0;
		int count = 0;

		infile >> count;
		ch = infile.get();
		while (infile.good())
		{
			if(ch == 'a') {ch = 'y';} else
			if(ch == 'b') {ch = 'h';} else
			if(ch == 'c') {ch = 'e';} else
			if(ch == 'd') {ch = 's';} else
			if(ch == 'e') {ch = 'o';} else
			if(ch == 'f') {ch = 'c';} else
			if(ch == 'g') {ch = 'v';} else
			if(ch == 'h') {ch = 'x';} else
			if(ch == 'i') {ch = 'd';} else
			if(ch == 'j') {ch = 'u';} else
			if(ch == 'k') {ch = 'i';} else
			if(ch == 'l') {ch = 'g';} else
			if(ch == 'm') {ch = 'l';} else
			if(ch == 'n') {ch = 'b';} else
			if(ch == 'o') {ch = 'k';} else
			if(ch == 'p') {ch = 'r';} else
			if(ch == 'q') {ch = 'z';} else
			if(ch == 'r') {ch = 't';} else
			if(ch == 's') {ch = 'n';} else
			if(ch == 't') {ch = 'w';} else
			if(ch == 'u') {ch = 'j';} else
			if(ch == 'v') {ch = 'p';} else
			if(ch == 'w') {ch = 'f';} else
			if(ch == 'x') {ch = 'm';} else
			if(ch == 'y') {ch = 'a';} else
			if(ch == 'z') {ch = 'q';}

			if((ch == '\n') && (i <= count))
			{
				if(i > 1) outfile << "\n";
				outfile << "Case #" << i++ << ": ";
			}
			else
			{
				outfile << ch;
			}
			ch = infile.get();
		}
		infile.close();
		outfile.close();
	}

	return 0;
}
