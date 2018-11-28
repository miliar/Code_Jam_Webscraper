// CodeJam2009-A.cpp : Defines the entry point for the console application.
//
/*
My Solution uses bit mapping instead of brute-force to perform matching of individule positions.
So that each position can be compared in constant time by using bitwise logical operation
*/
#include "stdafx.h"
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  char c;
  string number;
  string line;
  string determinateStrings[5000];
  int index;
  int count;
  int L,D,N;
  int i, j, k;
  ifstream inputFile ("A-large.txt");
  ofstream outputFile ("output.txt");
  int *mask;
  int mappingTable[26];

 /*Initializing mapping talbe*/
  mappingTable[0] = 1;
  for(i = 1; i<26; i++)
  {
		mappingTable[i] = mappingTable[i-1] << 1;
  }

  if (inputFile.is_open())
  { 
	  /* Read parameter L */
	c = inputFile.get();

	while(c!=0x20)
	{ 
		number += c; 
		c = inputFile.get();		
	}

	L = atoi(number.c_str());
	cout << "The number L is " << L << endl;
	number.clear();

	mask = (int*)malloc(L*sizeof(int));

	/* Read parameter D */

	c = inputFile.get();
	while(c!=0x20)
	{ 
		number += c; 
		c = inputFile.get();		
	}

	D = atoi(number.c_str());

	cout << "The number D is " << D << endl;
	number.clear();

	/* Read parameter N */

	c = inputFile.get();
	while(c!='\n')
	{ 
		number += c; 
		c = inputFile.get();		
	}

	N = atoi(number.c_str());

	cout << "The number N is " << N << endl;
	number.clear();

	/* Read determinate string set */

	for(i=0; i<D; i++)
	{
	    getline(inputFile, line);
		determinateStrings[i] = line;
//		cout << determinateStrings[i] << endl;
	}

	/* Read non-determinate string set */

	for(i=0; i<N; i++)
	{

		for(j = 0; j<L; j++)
		{
			mask[j] = 0;
		}

		for(j=0;j<L;j++)
		{
			c = inputFile.get();
			if(c == '(')
			{
//                cout << '(';

				c = inputFile.get();
				while(c != ')')
				{
					/* Set masking bit*/
					index = c - 'a';
					mask[j] = mask[j] | mappingTable[index]; 
					c = inputFile.get();
				}
//				cout << hex << mask[j] << "  ";
//				cout << ')';
			}
			else
			{	
					/* Set masking bit*/
					index = c - 'a';
					mask[j] = mappingTable[index]; 			
//					cout << hex << mask[j] << "  ";
			}
		}

		/* Perform Matching againt array of determinate strings*/

		count = 0;

		for(j=0; j<D; j++)
		{
			for(k=0; k<L; k++)
			{
				index = determinateStrings[j].at(k)-'a';
				if(!(mappingTable[index] & mask[k]))
				{
					break;
				}
			}
			if(k == L)
			{
				count++;
			}
		}

		/* Store the number of matches into output file*/
		if (outputFile.is_open())
		{
			outputFile << "Case #" << i+1 <<":	"<<count<<endl ;
		}

		/* Consume white space until line break or end of file */
		while(c != '\n' && c!= EOF)
		{
				c = inputFile.get();				
		}
		cout << endl;
	}

	outputFile.close();
    inputFile.close();

  }

  else cout << "Unable to open file"; 

  return 0;
	
}


