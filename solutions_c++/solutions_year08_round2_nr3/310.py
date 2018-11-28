#include <iostream>
#include <fstream>
#include <string>

const std::string INPUT_FILE = "C-small-attempt0.in";
const std::string OUTPUT_FILE = "C-small-attempt0.out";

int main ()
{
	std::ifstream infile;
	std::ofstream outfile;


	infile.open(INPUT_FILE.c_str());
	outfile.open(OUTPUT_FILE.c_str());

	if (!infile || !outfile)
	{
		std::cout << "file io error"<<std::endl;
		return 1;
	}

	int numCases;

	infile >> numCases;
	std::cout<<"Number of test cases: "<<numCases<<std::endl;

	for (int c =1; c<= numCases; c++)
	{
		int deckSize;

		infile>> deckSize;

		
		int* theDeck = new int[deckSize+1]; // create a deck of cards with size n

		for (int i=1; i <= deckSize; i++)  // set them to unmarked
			theDeck[i]=-1;

		//build the correct deck
		int deckPos =1;

		for (int i=1; i <= deckSize; i++)
		{
			int count =0;

			while (count < i)
			{
				if (theDeck[deckPos] == -1) // if space is empty
				{
					count++;
					if (count == i)
						break;

					deckPos++;
					if (deckPos > deckSize) // wrap around to beginning of deck
						deckPos =1;

					
				}
				else // space is not empty, skip it
				{
					deckPos++;
					if (deckPos > deckSize) // wrap around to beginning of deck
						deckPos =1;
				}
			}

			theDeck[deckPos] = i;
			
		}

		//read in the indicies of the array we need to output
		int numIndicies;
		infile >> numIndicies;

		int currIndex;

		std::cout<<"Case #"<<c<<": ";
		outfile<<"Case #"<<c<<": ";
		for (int i =0; i<numIndicies; i++)
		{
			infile>> currIndex;

			std::cout<<theDeck[currIndex]<<' ';
			outfile<<theDeck[currIndex]<<' ';
		}

		delete[] theDeck;
		std::cout<<std::endl;
		outfile<<std::endl;
	}


	infile.close();
	outfile.close();
	return 0;
}