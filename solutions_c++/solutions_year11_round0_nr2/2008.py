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
  int numberOfElements = sizeof(baseElements)/sizeof(char);
  char combinationTable[numberOfElements][numberOfElements];
  int opposeTable[numberOfElements];
  int dangerTable;
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
      int numberOfCombination, numberOfOppose, lenOfSequence, lenOfOutputSeq;
      char sequence[101];
      char outputSeq[101];
      int timeConsumed = 0;
      memset(combinationTable, 0, sizeof(char)*numberOfElements*numberOfElements);
      memset(opposeTable, 0, sizeof(int)*numberOfElements);
      dangerTable = 0;
      memset(outputSeq, 0, sizeof(char)*101);

      inFile>>numberOfCombination;
      for(ii=0;ii<numberOfCombination;ii++)
	{
	  char combinationRule[4];
	  int e1, e2;
	  char nb;

	  inFile>>combinationRule;
	  e1 = indexOfElement(combinationRule[0]);
	  e2 = indexOfElement(combinationRule[1]);
	  nb = combinationRule[2];
	  cout<<" ("<<e1<<" "<<e2<<"->"<<nb<<"),";
	  combinationTable[e1][e2]=nb;
	  combinationTable[e2][e1]=nb;
	}

      inFile>>numberOfOppose;
      for(ii=0;ii<numberOfOppose;ii++)
	{
	  char opposePair[3];
	  int e1, e2;
	  
	  inFile>>opposePair;
	  e1 = indexOfElement(opposePair[0]);
	  e2 = indexOfElement(opposePair[1]);
	  opposeTable[e1]=opposeTable[e1]|(1<<e2);
	  opposeTable[e2]=opposeTable[e2]|(1<<e1);
	  cout<<" ("<<opposePair[0]<<"X"<<opposePair[1]<<"),";
	}

      inFile>>lenOfSequence;
      inFile>>sequence;
      cout<<sequence<<endl;
      lenOfOutputSeq = 0;
      for(ii=0; ii<lenOfSequence; ii++)
	{
	  if(lenOfOutputSeq==0)
	    {
	      lenOfOutputSeq = 1;
	      outputSeq[0]= sequence[ii];
	      dangerTable=0;	      
	    }
	  else
	    {
	      int e1 = indexOfElement(outputSeq[lenOfOutputSeq-1]);
	      int e2 = indexOfElement(sequence[ii]);
	      if ((e1>=0)&&(combinationTable[e1][e2]!=0))
		{
		  outputSeq[lenOfOutputSeq-1]=combinationTable[e1][e2];
		}
	      else
		{
		  if((dangerTable&(1<<e2))||(opposeTable[e1]&1<<e2))
		    {
		      lenOfOutputSeq = 0;
		    }
		  else
		    {
		      if (e1>=0)
			dangerTable = dangerTable|opposeTable[e1];
		      lenOfOutputSeq++;
		      outputSeq[lenOfOutputSeq-1]=sequence[ii];
		    }
		}
	    }
	}
      
      outFile<<"Case #"<<(i+1)<<": [";
      for(ii=0;ii<lenOfOutputSeq;ii++)
	{
	  if(ii==lenOfOutputSeq-1)
	    outFile<<outputSeq[ii];
	  else
	    outFile<<outputSeq[ii]<<", ";
	}
      outFile<<"]"<<endl;
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
