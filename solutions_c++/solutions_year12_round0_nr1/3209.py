#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main(int argc, char** argv)
{
	std::string line;
	std::ifstream inputFile ("A-small-attempt0.in");
	std::ofstream outputFile ("output.txt");
	std::string sampleinput[] = {"y qee",
				"ejp mysljylc kd kxveddknmc re jsicpdrysi",
				"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
				"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
		
	std::string sampleoutput[] = {"a zoo",
				"our language is impossible to understand",
				"there are twenty six factorial possibilities",
				"so it is okay if you want to just give up"};
	char dictionary [26];
	for (int i = 0;i<26;i++)
		dictionary[i] = 'Z';


	int pos = 0;
	for(int j = 0; j < 4; j ++)
	{
		for(int i = 0; i < sampleinput[j].length(); i++)
		{
			if(sampleinput[j][i] != ' ')
			{
				pos = sampleinput[j][i] - 97;
				dictionary[pos] = sampleoutput[j][i];
			}
		}
	}
	dictionary[25] = 'q';
	std::string outputstring ="";
	int no_of_cases = 0;
	if (inputFile.is_open())
	{
		// this line gives us the number of test cases
		getline (inputFile,line);
		no_of_cases = atoi(line.c_str());

		for (int counter = 1; counter <= no_of_cases; counter++)
		{
			// read line by line
			getline (inputFile,line);
			outputstring = "";
			for (int i = 0;i<line.length();i++)
			{
				if (line[i] == ' ')
					outputstring += ' ';
				else
				{
					pos = line[i]-97;
					outputstring += dictionary[pos];
				}
			}
			outputFile <<"Case #"<<counter<<": "<<outputstring<<std::endl;
		}
		inputFile.close();
		outputFile.close();
	}
	else 
		std::cout << "Unable to open file"; 
	return 0;
}