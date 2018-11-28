#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

int indexOfElement(char e);

char baseElements[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
int main(int argc, char*argv[])
{
  int i,j;
  int numberOfLines = 0;
  ifstream inFile;
  ofstream outFile;

  if (argc!=3)
    {
      cout<<"usage: botTrust <input File> <output File>"<<endl;
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
  for(i=0;i<numberOfLines;i++)
    {
      int ii;
      int numberOfCandy;
      int patrickCandy = 1<<20;
      int totalCandies = 0;
      int trickTotal=0;
      inFile>>numberOfCandy;
      cout<<numberOfCandy<<endl;
      for(ii=0;ii<numberOfCandy;ii++)
	{
	  int candy;
	  inFile>>candy;
	  cout<<candy<<" ";
	  totalCandies+=candy;
	  if(candy<patrickCandy)
	    patrickCandy=candy;
	  trickTotal = trickTotal^candy;
	}
      cout<<endl;
      outFile<<"Case #"<<(i+1)<<": ";
      if (trickTotal)
	{
	  outFile<<"NO"<<endl;
	}
      else
	{
	  outFile<<totalCandies-patrickCandy<<endl;
	}
    }

  return 0;
}

int indexOfElement(char e)
{
  int i;
  int numberOfElements = sizeof(baseElements)/sizeof(char);
  for (i = 0;i<numberOfElements;i++)
    {
      if (baseElements[i]==e)
	return i;
    }
  return -1;
}
