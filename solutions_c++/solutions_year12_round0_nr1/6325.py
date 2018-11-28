#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void convert(char* str)
{
	int i=0;
	while(str[i] != '\0')
	{
		switch(str[i]-96)//'a'-96 = 1
		{
		case 1:
			*(str+i) = 'y';
			break;
		case 2:
			str[i] = 'h';
			break;
		case 3:
			str[i] = 'e';
			break;
		case 4:
			str[i] = 's';
			break;
		case 5:
			str[i] = 'o';
			break;
		case 6:
			str[i] = 'c';
			break;
		case 7:
			str[i] = 'v';
			break;
		case 8:
			str[i] = 'x';
			break;
		case 9:
			str[i] = 'd';
			break;
		case 10:
			str[i] = 'u';
			break;
		case 11:
			str[i] = 'i';
			break;
		case 12:
			str[i] = 'g';
			break;
		case 13:
			str[i] = 'l';
			break;
		case 14:
			str[i] = 'b';
			break;
		case 15:
			str[i] = 'k';
			break;
		case 16:
			str[i] = 'r';
			break;
		case 17:
			str[i] = 'z';
			break;
		case 18:
			str[i] = 't';
			break;
		case 19:
			str[i] = 'n';
			break;
		case 20:
			str[i] = 'w';
			break;
		case 21:
			str[i] = 'j';
			break;
		case 22:
			str[i] = 'p';
			break;
		case 23:
			str[i] = 'f';
			break;
		case 24:
			str[i] = 'm';
			break;
		case 25:
			str[i] = 'a';
			break;
		case 26:
			str[i] = 'q';
			break;

		}
		i++;
	}

}


int main ()
{
	string line;
	ifstream in;
	ofstream out;
	in.open("input.in");
	out.open("output.out");
	if(in.is_open() && out.is_open())
	{
		getline(in,line);
		int lines = atoi(line.c_str());
		for(int i=0; i<lines; i++)
		{
			getline(in,line);
			convert((char*) line.c_str());
			out << "Case #" << i+1 << ": " << line << '\n';
		}
	}
	
	return 0;
}