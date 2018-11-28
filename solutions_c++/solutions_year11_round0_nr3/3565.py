// SAI [ 7 May 2011 ]

#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>

typedef std::vector<unsigned int>           IntList;
typedef std::vector<unsigned int>::iterator IntListIterator;


typedef struct
{
  IntList intList;
  int     num;
}Input;

typedef std::vector<Input*>           InputList;
typedef std::vector<Input*>::iterator InputListIterator;

int  Jamstart(InputList& list);
void ReadData(InputList& list, std::string fileName);

bool mysort (unsigned int i, unsigned int j) { return (i > j); }
int 
Jamstart(InputList& list)
{
  unsigned int cases = 0;
  InputListIterator iter;
  for (iter  = list.begin();
       iter != list.end();
       iter ++)
  {
    Input * input = *iter;
    unsigned int result = 0;
    for (IntListIterator ii = input->intList.begin(); ii != input->intList.end(); ii++)
    {
      int val = *ii;
      result ^= val;
    }

    if (result != 0)
    {
      std::cout << "Case #" << ++cases << ": NO" << std::endl;
      continue;
    }

    std::sort(input->intList.begin(), input->intList.end(), mysort);
    result = 0;
    unsigned int seanCandy = 0;
    unsigned int seanSum = 0;
    for (IntListIterator ii = input->intList.begin(); ii != (input->intList.end() - 1); ii++)
    {
      int val = *ii;
      result  ^= val; 
      seanSum += val;
      
      unsigned int sec = 0;
      for (IntListIterator ij = ii + 1; ij != input->intList.end(); ij++)
      {
        val = *ij;
        sec ^= val;
      }

      if (result == sec)
      {
        seanCandy = seanCandy < seanSum ? seanSum : seanCandy;
      }
    }

    std::cout << "Case #" << ++cases << ": " << seanCandy << std::endl;
  }
}

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

        Jamstart(list);

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
  const unsigned int MAX_LINE_LENGTH = 2048000;
  char * line = new char[MAX_LINE_LENGTH];

  // get number of test case
  fin.getline(line, MAX_LINE_LENGTH);
  unsigned int cases = atoi(line);

  for (unsigned int i = 0; i < cases; i += 1)
  {
    Input * input = new Input();

    fin.getline(line, MAX_LINE_LENGTH);
    input->num = atoi(line);

    fin.getline(line, MAX_LINE_LENGTH);

    char * ptr = strtok(line, " ");
    while (ptr != 0)
    {
      input->intList.push_back(atoi(ptr));
      ptr = strtok (0, " ");
    }

    list.push_back(input);
  }

  delete [] line;
  fin.close();
}
