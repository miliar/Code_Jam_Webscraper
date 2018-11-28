
/*
Written by Jack Vucemillo.
On 15/04/2011.
Last known email address: shadow.wraith.12@gmail.com
*/


#include <iostream>
#include <fstream>
#include <string>
#include <map>


int main()
{
	// create googlerese to english dictionary
	// extracted from the example input/output and coded by hand
	std :: map<char, char> googlereseToEnglishDictionary;
	googlereseToEnglishDictionary[' '] = ' ';
	googlereseToEnglishDictionary['y'] = 'a';
	googlereseToEnglishDictionary['n'] = 'b';
	googlereseToEnglishDictionary['f'] = 'c';
	googlereseToEnglishDictionary['i'] = 'd';
	googlereseToEnglishDictionary['c'] = 'e';
	googlereseToEnglishDictionary['w'] = 'f';
	googlereseToEnglishDictionary['l'] = 'g';
	googlereseToEnglishDictionary['b'] = 'h';
	googlereseToEnglishDictionary['k'] = 'i';
	googlereseToEnglishDictionary['u'] = 'j';
	googlereseToEnglishDictionary['o'] = 'k';
	googlereseToEnglishDictionary['m'] = 'l';
	googlereseToEnglishDictionary['x'] = 'm';
	googlereseToEnglishDictionary['s'] = 'n';
	googlereseToEnglishDictionary['e'] = 'o';
	googlereseToEnglishDictionary['v'] = 'p';
	googlereseToEnglishDictionary['z'] = 'q';
	googlereseToEnglishDictionary['p'] = 'r';
	googlereseToEnglishDictionary['d'] = 's';
	googlereseToEnglishDictionary['r'] = 't';
	googlereseToEnglishDictionary['j'] = 'u';
	googlereseToEnglishDictionary['g'] = 'v';
	googlereseToEnglishDictionary['t'] = 'w';
	googlereseToEnglishDictionary['h'] = 'x';
	googlereseToEnglishDictionary['a'] = 'y';
	googlereseToEnglishDictionary['q'] = 'z';


	// open/create the input/output files
	std :: string filenameBase("A-small-attempt0");
	std :: fstream inFile(filenameBase + ".in", std :: ios :: in);
	std :: fstream outFile(filenameBase + ".out", std :: ios :: out | std :: ios :: trunc);


	// read the number of problems
	int problemCount;
	inFile >> problemCount;

	// lazily go to the new line and skip the whitespace on this line
	std :: getline(inFile, std :: string());


	// for each problem in the set
	for(int problem = 0; problem < problemCount; problem ++)
	{
		// get the line
		std :: string wholeLine;
		std :: getline(inFile, wholeLine);


		// output the header for the line
		outFile << "Case #" << problem + 1 << ": ";

		// translate the input until a character that isn't recognised is found
		// (because i'm lazy and cbf finding how to manipulate getline and stuff properly)
		for(int a = 0; a < wholeLine.size(); a ++)
			outFile << googlereseToEnglishDictionary[wholeLine[a]];


		// every one but the last, output a newline character
		if(problem + 1 < problemCount)
			outFile << std :: endl;
	}


	// close the input/output files
	inFile.close();
	outFile.close();
}
