// SAI [ 23 May 2010 ]

#include <string>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>

typedef struct 
{
  unsigned int a;
  unsigned int b;
}AB;

typedef std::vector<AB*>           IntList;
typedef std::vector<AB*>::iterator IntListIterator;

typedef struct
{
  int     N;
  IntList list;
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

		unsigned int count = 0;
		while (input->list.size() > 0)
		{
			AB * main = input->list.front();
			input->list.erase(input->list.begin());

			IntListIterator iiter;
			for (iiter = input->list.begin(); iiter != input->list.end(); iiter++)
			{
				AB * curr = *iiter;
				if ((main->a < curr->a && main->b > curr->b) || (main->a > curr->a && main->b < curr->b)) count += 1;
			}
			
			delete main;
		}

		std::cout << "Case #" << ++cases << ": " << count << std::endl;
	}

	Input * input = 0;
	while (list.size() > 0)
	{
		input = list.front();
		list.erase(list.begin());
		while (input->list.size() > 0)
		{
			AB * ab = input->list.front();
			input->list.erase(input->list.begin());
			delete ab;
		}
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

		fin.getline(line, MAX_LINE_LENGTH); // get N
		sscanf(line, "%d", &(input->N));

		for (unsigned int j = 0; j < input->N; j += 1)
		{
			fin.getline(line, MAX_LINE_LENGTH); // get A B
			AB * ab = new AB();
			sscanf(line, "%d %d", &(ab->a), &(ab->b));
			input->list.push_back(ab);
		}
		list.push_back(input);
	}

	fin.close();
}
