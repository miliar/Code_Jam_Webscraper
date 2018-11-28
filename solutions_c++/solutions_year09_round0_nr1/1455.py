#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#define MAX_WORD_LENGTH 15

using namespace std;

int main(void)
{
	bool                             match                     = false;
	char                             letter                    = 0;
	char                             word[MAX_WORD_LENGTH + 1] = { 0 };
	ifstream                         input;
	int                              i                         = 0;
	int                              letterCount               = 0;
	int                              possibleWords             = 0;
	int                              testCases                 = 0;
	int                              wordCount                 = 0;
	int                              wordLength                = 0;
	ofstream                         output;
	pair < bool, string >            dictionaryEntry;
	string                           possibleWord;
	unsigned int                     dictionaryIndex           = 0;
	unsigned int                     possibleLetterIndex       = 0;
	vector < char >                  possibleLetter;
	vector < string >                possibleLetters;
	vector < pair < bool, string > > dictionary;

	//
	//  Open the files.
	//
	input.open("A-large.in", ios_base::in);
	if (false == input.is_open())
	{
		printf("Error opening input file A-small.in did not exist.");
		goto exit;
	}

	output.open("A-large.out", ios_base::out);
	if (false == output.is_open())
	{
		printf("Error opening output file A-small.out.");
		goto exit;
	}

	//
	//  Process the input file.
	//
	input >> wordLength >> wordCount >> testCases;
	input.getline(word, sizeof (word));

	//
	//  Read the dictionary.
	//
	for (i = 0; i < wordCount; i++)
	{
		memset(word, 0, sizeof (word));
		input.getline(word, sizeof (word));

		if (strlen(word) != wordLength)
		{
			printf("Error loading dictionary.");
			goto exit;
		}

		dictionaryEntry.first  = true;
		dictionaryEntry.second = word;
		dictionary.push_back(dictionaryEntry);
	}

	//
	//  Process the test cases.
	//
	for (i = 0; i < testCases; i++)
	{
		//
		//  Reset the dictionary flags denoting valid words.
		//
		for (dictionaryIndex = 0; dictionaryIndex < dictionary.size(); dictionaryIndex++)
			dictionary[dictionaryIndex].first = false;

		//
		//  Clear the possible letters vector holding the possible letters for each letter in
		//  the word.
		possibleWord.erase(possibleWord.begin(), possibleWord.end());
		possibleLetters.erase(possibleLetters.begin(), possibleLetters.end());

		for (letterCount = 0; letterCount < wordLength; letterCount++)
		{
			possibleLetter.erase(possibleLetter.begin(), possibleLetter.end());

			input >> letter;

			if ('(' == letter)
			{
				input >> letter;
				while (')' != letter)
				{
					possibleLetter.push_back(letter);
					input >> letter;
				}
			}
			else
			{
				possibleLetter.push_back(letter);
			}

			if (0 == letterCount)
			{
				for (dictionaryIndex = 0; dictionaryIndex < dictionary.size(); dictionaryIndex++)
				{
					for (possibleLetterIndex = 0; possibleLetterIndex < possibleLetter.size();
						possibleLetterIndex++)
					{
						if (dictionary[dictionaryIndex].second[letterCount] ==
							possibleLetter[possibleLetterIndex])
						{
							dictionary[dictionaryIndex].first = true;
							break;
						}
					}
				}
			}
			else
			{
				for (dictionaryIndex = 0; dictionaryIndex < dictionary.size(); dictionaryIndex++)
				{
					if (false == dictionary[dictionaryIndex].first)
						continue;

					match = false;
					for (possibleLetterIndex = 0; possibleLetterIndex < possibleLetter.size();
						possibleLetterIndex++)
					{
						if (dictionary[dictionaryIndex].second[letterCount] ==
							possibleLetter[possibleLetterIndex])
						{
							match = true;
							break;
						}
					}

					if (false == match)
						dictionary[dictionaryIndex].first = false;
				}
			}

			possibleWord.push_back(letter);
		}

		possibleWords = 0;
		for (dictionaryIndex = 0; dictionaryIndex < dictionary.size(); dictionaryIndex++)
		{
			if (true == dictionary[dictionaryIndex].first)
				possibleWords++;
		}

		output << "Case #" << (i + 1) << ": " << possibleWords << endl;
	}

	exit : ;

	//
	//  Close the files.
	//
	if (input.is_open())
		input.close();

	if (output.is_open())
		output.close();

	return 0;
}