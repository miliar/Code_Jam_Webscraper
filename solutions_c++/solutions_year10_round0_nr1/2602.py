// SAI [ 8 May 2010 ]

#include <string>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>

typedef struct
{
  int N;
  int K;
}Input;

typedef std::vector<Input*>           InputList;
typedef std::vector<Input*>::iterator InputListIterator;

void ReadData(InputList& list, std::string fileName);

int main(int argc, char * argv[])
{
  	InputList list;
	switch(argc)
	{
	case 2:
		ReadData(list, argv[1]);
		break;
	default:
		std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
		return 1;
	}

	unsigned int cases = 0;
	InputListIterator iter;
	for (iter  = list.begin();
             iter != list.end();
             iter ++)
 	{
		Input * input = *iter;

		if (input->K == 0)
		{
			std::cout << "Case #" << ++cases << ": " << "OFF" << std::endl;
			continue;
		}

		unsigned int value = (unsigned int)pow(2.0, (double) input->N);
		int result = input->K % value;	
		unsigned int check  = (unsigned int)(result + 1);

		// is the result is the (power of 2) - 1
		bool isOn = (((check & (check - 1)) == 0) && (check == value))? true : false;

		std::cout << "Case #" << ++cases << ": " << ((isOn)? "ON" : "OFF") << std::endl;
	}

	Input * input = 0;
	while (list.size() > 0)
	{
		input = list.front();
		list.erase(list.begin());
		delete input;
	}

	return 0;
}

// Read data from file
void
ReadData(InputList& list, std::string fileName)
{
	std::ifstream fin(fileName.c_str());
	const unsigned int MAX_LINE_LENGTH = 2048;
	char line[MAX_LINE_LENGTH];

	// get number of test case
	fin.getline(line, MAX_LINE_LENGTH);
   	unsigned int cases = atoi(line);

	for (unsigned int i = 0; i < cases; i += 1)
	{
		Input * input = new Input();

		fin.getline(line, MAX_LINE_LENGTH);
		sscanf(line, "%d %d", &(input->N), &(input->K));
		list.push_back(input);
	}

	fin.close();
}
