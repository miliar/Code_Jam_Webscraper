/*
To build issue 
	"g++ main.cpp"

To run "./a.out "input file name" "output file name""


g++ compiler of
gcc version 4.2.3 (Ubuntu 4.2.3-2ubuntu7)
*/

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <iterator>

using namespace std;

#include <stdio.h>


vector<string> svec;

void readFile(string);
void process(string);

int main(int argc, char ** argv)
{
  if (argc != 3)
    {
      cout << endl << "Incorrect arg no"<< endl;
      return -1;
    }
  readFile(string(argv[1]));
  process(string(argv[2]));
}

void process(string outName)
{
  ofstream ofile(outName.c_str());
  
  vector<string>::iterator iter1 = svec.begin();
  ++iter1;

  int count = 1;
  while (iter1 != svec.end())
    {
      string lSearch;
      list<string> sOrder;

      list<string> lEngine;

      int noEng = 0;
      int noQueries = 0;

      noEng = atoi((*iter1).c_str());
      ++iter1;
      for (int i = 0; i < noEng; i++)
	{
	  lEngine.push_back(*iter1);
	  ++iter1;
	}

      list<string> tmp(lEngine);

      noQueries = atoi((*iter1).c_str());
      ++iter1;
      for (int i = 0; i < noQueries; ++i)
	{
	  list<string>::iterator iter2 = find(tmp.begin(), tmp.end(), *iter1);
	  if (iter2 != tmp.end())
	    {
	      tmp.erase(iter2);
	      if (tmp.empty())
		{
		  sOrder.push_back(*iter1);
		  lSearch = *iter1;
		  tmp = lEngine;
		  iter2 = find(tmp.begin(), tmp.end(), lSearch);
		  tmp.erase(iter2);
		}
	    }
	  ++iter1;
	}
      
      ofile << "Case #" << count << ": " << sOrder.size() << endl;
      ++count;
    }
}

void readFile(string inName)
{
  ifstream ifile(inName.c_str());

  char tmp[200];
  
  while( ifile.getline(tmp, 200,'\n') )
    {
      svec.push_back(string(tmp));
    }
  



  /*
  istream_iterator<string> start(ifile);
  istream_iterator<string> end;

  copy(start, end, back_inserter(svec));
  */
}
