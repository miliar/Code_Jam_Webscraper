#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <ctype.h>

using namespace std;

string num2str(int i)
{
	stringstream ss;
	ss<<i;
	return ss.str();
}

int main()
{
	const int MAX_LINE_NUMBER = 30;
	const int MIN_LINE_NUMBER = 1;
	const int MAX_CHAR_NUMBER = 100;

	char normal_array[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char secret_array[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	string line;
	int line_number = 1;
	string strCase = "Case #";
	int number = 0;
	int total_line_number = 0;
	ifstream fin("A-small-attempt10.in"); 
	ofstream fout("output.out",ios::app);
	while (getline(fin,line))
	{
		if (line_number==1)
		{
			total_line_number=atoi(line.c_str());
		}
		else
		{
			for (int i=0;i<line.size()&&i<MAX_CHAR_NUMBER;i++)
			{
				if (line[i]==(char)32)
				{
					line[i] = (char)32;
				}
				else
				{
					number = int(line[i])-97;
					line[i] = toascii(secret_array[number]);
				}
			}
			fout << strCase << toascii(line_number-1) << ": "<< line;
			if (line_number<=30)
			{
				fout << endl;
			}
		}

		line_number++;
		if (line_number-1 > MAX_LINE_NUMBER)
		{
			break;
		}
	}
	return 0;
}