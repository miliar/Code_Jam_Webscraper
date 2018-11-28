// SAI [ 8 May 2010 ]

#include <string>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cstdlib>

typedef struct
{
  int R;
  int k;
  int N;
  int * queue;
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

		int money = 0;
		int q = 0;
		for (int r = 0; r < input->R; r += 1)
		{
			int space = input->k;			
			int num   = input->N;
			while(space > 0 && num > 0)
			{
				if (space >= input->queue[q])
				{
					space -= input->queue[q]; // let them take their seats
				}	
				else
				{
					break; // no space left
				}
				q    = (q + 1) % input->N;
				num -= 1; // if num == 0 -> no one left
			}
			money += (input->k - space); // collect money
		}
		std::cout << "Case #" << ++cases << ": " << money << std::endl;
	}

	Input * input = 0;
	while (list.size() > 0)
	{
		input = list.front();
		list.erase(list.begin());
		delete [] input->queue;
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
	unsigned int pInd = 0;

	// get number of test case
	fin.getline(line, MAX_LINE_LENGTH);
   	unsigned int cases = atoi(line);

	for (unsigned int i = 0; i < cases; i += 1)
	{
		Input * input = new Input();
		input->queue = 0;

		fin.getline(line, MAX_LINE_LENGTH);
		sscanf(line, "%d %d %d", &(input->R), &(input->k), &(input->N));
		input->queue = new int[input->N];
		memset(input->queue, 0, input->N * sizeof(int));

		fin.getline(line, MAX_LINE_LENGTH);
		char * chr = strtok(line, " \t");
		for (unsigned int j = 0; j < input->N; j += 1)
		{
			input->queue[j] = atoi(chr);
			chr = strtok(NULL, " \t");
		}
		list.push_back(input);
	}

	fin.close();
}
