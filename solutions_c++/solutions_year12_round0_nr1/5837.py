#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;
char get_value(char key);
int main(int argc, char* argv[])
{
	int NO,a,i=0;
	string line;
	ifstream myfile (argv[1]);
	ofstream output;
	output.open("output.txt");
	if (myfile.is_open())
	{
		while ( myfile.good() )
		{
			getline (myfile,line);
			a=line.length();
			if(a>2)
			{
				output<<"Case #"<<i+1<<": ";
				for(int j=0;j<a;j++)
				output<<get_value(line[j]);
				i++;
				output<<endl;
			}
			
		}
		myfile.close();
		output.close();
	}
}
char get_value(char key)
{
    switch (key)
    {
        case 'a':
            return 'y';
        case 'b':
            return 'h';
        case 'c':
            return 'e';
        case 'd':
            return 's';
        case 'e':
            return 'o';
        case 'f':
            return 'c';
        case 'g':
            return 'v';
        case 'h':
            return 'x';
        case 'i':
            return 'd';
        case 'j':
            return 'u';
        case 'k':
            return 'i';
        case 'l':
            return 'g';
        case 'm':
            return 'l';
        case 'n':
            return 'b';
        case 'o':
            return 'k';
        case 'p':
            return 'r';
        case 'q':
            return 'z';
        case 'r':
            return 't';
        case 's':
            return 'n';
        case 't':
            return 'w';
        case 'u':
            return 'j';
        case 'v':
            return 'p';
        case 'w':
            return 'f';
        case 'x':
            return 'm';
        case 'y':
            return 'a';
        case 'z':
            return 'q';			
        default:
            return key;// Do whatever is appropriate when the key is not valid
    }
}