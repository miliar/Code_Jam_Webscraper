//============================================================================
// Name        : cpptrain.cpp
// Author      : Dante
// Version     :
// Copyright   : Open
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int processInput(ifstream& infile, unsigned int cases, unsigned int letters, unsigned int wordcount);

int main() {
	string line;
	stringstream myStream;
	ifstream infile;
	unsigned int cases, wordcount,letters;
	infile.open("./A-large.in");


	if (infile.is_open())
	{
		/* ok, proceed with reading data */
		// Read # of cases, words, and length:
		getline (infile,line);
		myStream<<line;
		myStream >> letters >> wordcount >> cases; // assign # of cases & words and length of words

		processInput(infile,cases,letters,wordcount);// << endl;

		infile.close();

	}

	else cout << "File not found" << endl;


	return 0;
}

int processInput(ifstream& infile, unsigned int cases, unsigned int letters,unsigned int wordcount)
{

	int tokencounter;
	unsigned int i,j,k,matchcount,totalmatch;
	bool block=false;
	string aliendic[wordcount]; // array of strings for dictionary words
	string alienblock;
	string alientoken[letters];
	string alienin;
	unsigned int caseloop;

	ofstream outfile("./output.txt");

	// Read alien dictionary:
	for(i=0;i<wordcount;i++)
	{
		getline (infile,aliendic[i]);

	}

	for(caseloop=0;caseloop<cases;caseloop++)
	{

		cout << "Case #" << caseloop+1 << ": ";
		outfile << "Case #" << caseloop+1 << ": ";
		matchcount=0;
		totalmatch=0;
		tokencounter=0;

		// Read next word to analyze:
		getline(infile,alienin);


		// Extract tokens:

		for(i=0;i<alienin.length();i++)
		{

			// Check for brackets:
			switch (alienin[i])
			{
			case 40: // '(' start block:
				block=true;
				break;
			case 41: // ')' end block:
				block=false;							// not inside of token block anymore
				alientoken[tokencounter]+=alienblock;	// copy token block onto alientoken string
				alienblock.clear(); 					// clear alienblock
				tokencounter++;							// move to next string
				break;
			default:
				alienblock+=alienin[i];
				if(!block)
				{
					alientoken[tokencounter]+=alienblock;
					tokencounter++;
					alienblock.clear();
				}
				break;
			}
		}


// MAIN ALGORITHM BEGIN //
		// Combine tokens and compare against string:
		for(k=0;k<wordcount;k++)  						// Take dictionary word
		{
			for(j=0;j<letters;j++)  					// Look at token by token
			{
				for(i=0;i<alientoken[j].length();i++) 	// Take characters from each token
				{
					if(aliendic[k][j] == alientoken[j][i]){  // Compare each character against the one from the dictionary
						matchcount++;						// If they match, increase the number of matches
						break;
					}
				}
			}

			if(matchcount==letters){					// If the matches equal the number of tokens,
				totalmatch++;							// increase the total count
			}
			matchcount=0;								// Reset 'small' matches
		}

// MAIN ALGORITHM END //

		for(i=0;i<letters;i++)
		{
			alientoken[i].clear();						// Clear tokens array
		}
		alienblock.clear();								// Clear alienblock
		cout << totalmatch << endl;						// print number of matches
		outfile << totalmatch << endl;
	}

	outfile.close();

	return 0;


}
