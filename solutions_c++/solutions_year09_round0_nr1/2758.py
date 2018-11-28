// Google Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std; // for cout,cin and string

int CalculatePossibilities( unsigned int L, unsigned int D, string * dictionary, string word );
bool CheckForWord (unsigned int L, string dictionaryWord, string word);
bool CheckForLetter (string word, char letter);

unsigned int posn = 0;
ifstream inputFile;
ofstream outputFile;

int main()
{
	inputFile.open ("C:\\Documents and Settings\\AnnamariaD\\input.txt");
	outputFile.open("C:\\Documents and Settings\\AnnamariaD\\Output1.txt");

	//There are D words
	//All words are length L
	//There are N test cases
	unsigned int nL, nD, nN;
	inputFile >> nL;
	inputFile >> nD;
	inputFile >> nN;

	//The dictionary of words
	string * pstrDictionary = new string[nD];

	//A word to translate
	string strWord;

	//Read D words for the dictionary
	for (unsigned int iii = 0; iii < nD; iii++)
	{
		inputFile >> pstrDictionary[iii];
	}

	int nTemp;
	//Read N words for the test cases
	for (unsigned int iii = 0; iii < nN; iii++)
	{
		inputFile >> strWord;
		nTemp =  CalculatePossibilities( nL, nD, pstrDictionary, strWord );
		outputFile << "Case #" << (iii + 1) << ": " << nTemp << endl;
	}

	delete[] pstrDictionary;

	inputFile.close();
	outputFile.close();
	return 0;
}

int CalculatePossibilities( unsigned int L, unsigned int D, string * dictionary, string word )
{
	//the total count of matches
	int count = 0;
	bool matchLetter = false;
	bool matchWord = false;

	//go through each dictionary word
	for (unsigned int iii = 0; iii < D; iii++)
	{
		matchWord = CheckForWord (L, dictionary[iii], word);

		//if there's a matching word, add one
		if (matchWord == true)
			count++;

	}	//next dictionary word (or end)

	return count;
}

bool CheckForWord (unsigned int L, string dictionaryWord, string word)
{
	bool matchLetter = false;
	posn = 0;

	//go through each letter of the dictionary word
	for (unsigned int jjj = 0; jjj < L; jjj++)
	{
		//Check if word's phrase at current posn matches the current letter
		matchLetter = CheckForLetter ( word,dictionaryWord[jjj] );
		
		//Do not want to go onto the next letter of the dictionary word
		//if the last one didn't match
		if (matchLetter == false)
			break;
	}	//next dictionary word's letter (or end)
	return matchLetter;
}


//Checks if phrase (current position in word) matches letter
bool CheckForLetter (string word, char letter)
{
	bool inPhrase = false;
	bool matchLetter = false;

	//incrementing through the translation word (a phrase in it)
	for (; posn < word.length() ; posn++)
	{
		if ( word[posn] == '(' )
			inPhrase = true;
		else if ( word[posn] == letter )
		{
			matchLetter = true;

			//if we are in a phrase, we want to finish incrementing
			//if we're not in a phrase, we don't want to finish incrementing
			if (inPhrase == false)
			{
				posn++;
				return matchLetter;
			}
		}
		//End of phrase. Stop incrementing.
		else if ( word[posn] == ')' )
		{
			inPhrase = false;
			posn++;
			break;
		}
		else if ( inPhrase == false )
		{
			posn++;
			return false;
		}
				
	}	//end of phrase

	return matchLetter;
}