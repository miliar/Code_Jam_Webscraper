#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

long greatestCommonFactor(long num1, long num2) {
    //  determines the maximum range to search; chooses the smaller of the two
    //  arguments (since the highest GCF is the smaller of the two numbers)
    long maxrange=(num1>=num2 ? num2 : num1);

    //  sets initial GCF to 1
    long lastGCF=1;
    for (long factor=2; factor<=maxrange; ++factor) {
        if ( num1%factor==0 && num2%factor==0 ) {
            //  if both numbers are divisible by the current factor, it is a
            //  common factor, so store and go on to the next
            lastGCF=factor;
        }
    }
    return lastGCF;
} 


int main(int argc, char*argv[])
{
  int i,j;
  ifstream inFile;
  ofstream outFile;
  int numberOfLines;

  if (argc!=3)
    {
      cout<<"usage: freeCell <input File> <output File>"<<endl;
      exit(0);
    }
  inFile.open(argv[1], ios::in);
  if (!inFile)
    {
      cerr<<"Cant's open input file "<<argv[1]<<endl;
      exit(1);
    }
  outFile.open(argv[2], ios::out);
  if (!outFile)
    {
      cerr<<"Cant's open input file "<<argv[2]<<endl;
      exit(1);
    }
  if (inFile.eof())
    {
      cerr<<"Input file formation error!"<<endl;
      exit(1);
    }

  inFile>>numberOfLines;
  cout<<numberOfLines<<endl;
  for (i=0; i<numberOfLines; i++)
    {
      bool possible = true;
      long N, Pg, Pd, gcf;
      inFile>>N;
      inFile>>Pd;
      inFile>>Pg;
      gcf = greatestCommonFactor(100, Pd);
      if ((Pd!=0)&&(N < 100/gcf))
	{
	  possible = false;
	}
      if ((Pg==100)&&(Pd!=100))
	{
	  possible = false;
	}
      if ((Pg==0)&&(Pd!=0))
	{
	  possible = false;
	}
      if (possible)
	{
	  outFile<<"Case #"<<i+1<<": Possible"<<endl;
	}
      else
	{
	  outFile<<"Case #"<<i+1<<": Broken"<<endl;
	}
    }
}


