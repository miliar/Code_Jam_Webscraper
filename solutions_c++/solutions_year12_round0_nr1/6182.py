#include <iostream>
using namespace std;
#include <fstream>
#include <string.h>

#define FILE_IN "A-small-attempt6.in"
#define FILE_OUT "output.out"

int main()
{	
	ifstream input;
	ofstream output;
	input.open(FILE_IN,ios::in||ios::_Nocreate);
	output.open(FILE_OUT,ios::out);
	int char_value,total,c_value,tchar,length;
	char line[500],buff[5];
	input.getline(buff,5);
	total = atoi(buff);
	for(int i=0;i<total;++i)
	{
		input.getline(line,500);
		length = strlen(line);
		for(int j=0;j<length;++j)
		{
			char_value = int(line[j]);
			c_value = char_value - 96;

			if(char_value == 32)
			{
				tchar = char_value;
			}
			else
			{
				switch (c_value)
				{
				case 1:
					tchar = 25 + 96;
					break;
				case 2:
					tchar = 8 + 96;
					break;
				case 3:
					tchar = 5 + 96;
					break;
				case 4:
					tchar = 19 + 96;
					break;
				case 5:
					tchar = 15 + 96;
					break;
				case 6:
					tchar = 3 + 96;
					break;
				case 7:
					tchar = 22 + 96;
					break;
				case 8:
					tchar = 24 + 96;
					break;
				case 9:
					tchar = 4 + 96;
					break;
				case 10:
					tchar = 21 + 96;
					break;
				case 11:
					tchar = 9 + 96;
					break;
				case 12:
					tchar = 7 + 96;
					break;
				case 13:
					tchar = 12 + 96;
					break;
				case 14:
					tchar = 2 + 96;
					break;
				case 15:
					tchar = 11 + 96;
					break;
				case 16:
					tchar = 18 + 96;
					break;
				case 17:
					tchar = 26 + 96;
					break;
				case 18:
					tchar = 20 + 96;
					break;
				case 19:
					tchar = 14 + 96;
					break;
				case 20:
					tchar = 23 + 96;
					break;
				case 21:
					tchar = 10 + 96;
					break;
				case 22:
					tchar = 16 + 96;
					break;
				case 23:
					tchar = 6 + 96;
					break;
				case 24:
					tchar = 13 + 96;
					break;
				case 25:
					tchar = 1 + 96;
					break;
				case 26:
					tchar = 17 + 96;
					break;
				}
			}
			line[j] = char(tchar);
		}
		output<<"Case #"<<i+1<<": "<<line<<endl;
	}
	input.close();
	output.close();
	system("pause");
	return 0;
}
