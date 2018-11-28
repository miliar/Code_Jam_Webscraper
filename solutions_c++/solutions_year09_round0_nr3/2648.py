#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

void countsub(const string & big, 
	      const unsigned int & bigi,
	      const unsigned int &smalli,
	      unsigned int &counter);

const string small("welcome to code jam");

int main(int argc, char **argv)
{
  
  ifstream ifile(argv[1]);
  ofstream ofile(argv[2]);

  char arg[1024];
  ifile.getline(arg, 1024);
  
  unsigned int testno = 1;
  while (ifile.getline(arg,1024))
    {
      unsigned int counter = 0;
      string big = arg;
      countsub(big,0,0,counter);
      ofile << "Case #" << testno++ << ": " << setfill('0') << setw(4)  << counter << endl;
    }
}

void countsub(const string & big, 
	      const unsigned int & bigi,
	      const unsigned int &smalli,
	      unsigned int &counter)
{
  if ( (small.size()-smalli) > 
       (big.size()-bigi))
    {
      return;
    }

  if (big[bigi] == small[smalli])
    {
      if (small.size() == (smalli+1))
	{
	  counter++;
	  counter %=10000;
	}
      else if (big.size() > (bigi+1))
	{
	  countsub(big, bigi+1, smalli+1, counter);
	}
    }
  if (big.size() > (bigi+1))
    {
      countsub(big,bigi+1,smalli,counter);
    }
}
