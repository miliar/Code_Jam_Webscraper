#include <iostream>
#include <fstream>
#include <string>

int main (int argc, char * const argv[]) {
	
	
	std::ifstream instream("A-large.in.txt");
	std::ofstream outstream("largeOutput.txt");
	
	int numLetters;
	int numWords;
	int numTestCases;
	
	instream >> numLetters >> numWords >> numTestCases;
	
	std::string dictionary[numWords];
	std::string dictString = "";
	
	char extra[100];
	instream.getline(extra,	100);
	
	// read in all the recognized words
	for(int wordNum = 0; wordNum < numWords; wordNum++)
	{
		char word[20];
		instream.getline(word, 20);
		dictionary[wordNum] = word;
		dictString += word;
	}
	
	
	for(int testCase = 0; testCase < numTestCases; testCase ++)
	{
		char pattern[500];
		int numPossibleMatches = 0;
		
		// read in the pattern word (test case)
		instream.getline(pattern, 500);
		
		// break it into parts, there will be one part for every letter
		std::string parts[numLetters];
		
		int partNum = 0;
		int curr = 0;
		
		int numPossibilities = 1;
		
		while(pattern[curr] != '\0')
		{
			// if its the start of a section, save all the characters together in one part
			if(pattern[curr] == '(')
			{
				// move to the next character and add it to this part
				curr++;
				parts[partNum] = pattern[curr];
				curr++;
				while(pattern[curr] != ')')
				{
					parts[partNum] += pattern[curr];
					curr++;
				}
				
			}
			else
			{
				parts[partNum] = pattern[curr];
			}
			
			numPossibilities *= parts[partNum].size();
			
			curr++;
			partNum++;
		}
		
		// sieve the dictionary using the parts.
		std::string allPossibilities[numWords];
		for(int c = 0; c < numWords; c++)
		{
			allPossibilities[c] = dictionary[c];
		}
		
		// go through each letter, keeping words that match at that letter
		for(int i = 0; i < numLetters; i++)
		{
			int currentPossibilityIndex = 0;
			int possleng = parts[i].size();
			std::string temp[numWords];
			
			for(int k = 0; k < possleng; k++)
			{
				char mychar = (parts[i].c_str())[k];
				for(int d = 0; d < numWords; d++)
				{
					if(mychar == (allPossibilities[d].c_str())[i])
					{
						temp[currentPossibilityIndex] = allPossibilities[d];
						currentPossibilityIndex++;
					}
				}
			}
			
			for(int c = 0; c < numWords; c++)
			{
				allPossibilities[c] = temp[c];
			}
			numPossibleMatches = currentPossibilityIndex;
		}
		
		outstream << "Case #" << testCase+1 << ": " << numPossibleMatches << std::endl;
	}

	

    return 0;
}
