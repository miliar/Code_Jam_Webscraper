/*
To build issue 
	"g++ main.cpp"

To run "./a.out "input file name" "output file name""


g++ compiler of
gcc version 4.2.3 (Ubuntu 4.2.3-2ubuntu7)
*/


#include <iostream>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

#include <stdio.h>

void read(string);
void process(string);

vector<string> svec;

class myTime
{
private:
  int _hours;
  int _mins;
public:
  bool operator <(const myTime & rhs) const
  {
    if (_hours < rhs._hours)
      return true;
    else if (_hours > rhs._hours)
      return false;
    else if (_mins < rhs._mins)
      return true;
    else 
      return false;
  }
  bool operator == (const myTime &rhs) const
  {
    if (_hours == rhs._hours && 
	_mins == rhs._mins)
      return true;
    else
      return false;
  }
  void addMins(int mins)
  {
    _mins += mins;
    if (_mins > 60)
      {
	_mins -= 60;
	++_hours;
      }
  }
  myTime(int hours, int mins) : _hours(hours), _mins(mins) 
  {}
};



int main(int argc, char ** argv)
{
  if (3 != argc)
    {
      cout << endl << "Not correct argc" << endl;
      return -1;
    }

  read(string(argv[1]));
  process(string(argv[2]));
}

void process(string outName)
{
  ofstream ofile(outName.c_str());

  vector<string>::iterator iter1 = svec.begin();
  ++iter1;
  int turnTime = 0;
  int NA = 0;
  int NB = 0;
  int count = 1;
  while( iter1 != svec.end())
    {
      vector<myTime> depA;
      vector<myTime> arrA;
      vector<myTime> readyA;

      vector<myTime> depB;
      vector<myTime> arrB;
      vector<myTime> readyB;
      
      turnTime = atoi((*iter1).c_str());
      ++iter1;
      NA = atoi((*iter1).c_str());
      ++iter1;
      NB = atoi((*iter1).c_str());
      ++iter1;

      for (int i = 0; i < NA; i++)
	{
	  int hours;
	  int mins;

	  sscanf((*iter1).c_str(), "%d:%d", &hours, &mins);
	  depA.push_back(myTime(hours, mins));
	  ++iter1;

	  sscanf((*iter1).c_str(), "%d:%d", &hours, &mins);
	  myTime tmp(hours, mins);
	  arrB.push_back(tmp);

	  tmp.addMins(turnTime);
	  readyB.push_back(tmp);

	  ++iter1;
	}
      for (int i = 0; i < NB; i++)
	{
	  int hours;
	  int mins;

	  sscanf((*iter1).c_str(), "%d:%d", &hours, &mins);
	  depB.push_back(myTime(hours, mins));

	  ++iter1;

	  sscanf((*iter1).c_str(), "%d:%d", &hours, &mins);
	  myTime tmp(hours, mins);
	  arrA.push_back(tmp);

	  tmp.addMins(turnTime);
	  readyA.push_back(tmp);

	  ++iter1;
	}
      
      sort(depA.begin(), depA.end());
      sort(depB.begin(), depB.end());

      sort(arrA.begin(), arrA.end());
      sort(arrB.begin(), arrB.end());

      sort(readyA.begin(), readyA.end());
      sort(readyB.begin(), readyB.end());
      
      int noA = 0;
      int noB = 0;

      size_t size = 0;
      size_t pos = 0;

      size = readyA.size();
      pos = 0;

      for (vector<myTime>::iterator iter2 = depA.begin();
	   iter2 != depA.end();
	   ++iter2)
	{
	  if (!(pos < size && (readyA[pos] < *iter2 || readyA[pos] == *iter2 )))
	    {
	      ++noA;
	    }
	  else
	    {
	      ++pos;
	    }
	}

      size = readyB.size();
      pos = 0;
      for (vector<myTime>::iterator iter3 = depB.begin();
	   iter3 != depB.end();
	   ++iter3)
	{
	  if (!( pos < size && (readyB[pos] < *iter3 || readyB[pos] == *iter3) ))
	    {
	      ++noB;
	    }
	  else
	    {
	      ++pos;
	    }
	}
      
      ofile << "Case #" << count << ": " << noA << " " << noB;
      ofile << endl;
      ++count;
    }
}




void read(string inName)
{
  ifstream ifile(inName.c_str());

  istream_iterator<string> start(ifile);
  istream_iterator<string> end;
  
  copy(start, end, back_inserter(svec));
}

