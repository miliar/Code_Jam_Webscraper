#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <queue>

using namespace std;
using namespace stdext;

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile);

int getCode(int mask[4])
{
	if (mask[0] == 4 || (mask[0] == 3 && mask[2] > 0))
		return 0;
	if (mask[1] == 4 || (mask[1] == 3 && mask[2] > 0))
		return 1;

	return -1;
}

void findChar(char c, int mask[])
{
	if (c == 'X')
		++mask[0];
	else if (c == 'O')
		++mask[1];
	else if (c == 'T')
		++mask[2];
	else if (c == '.')
		++mask[3];
}

string getStatus(int code)
{
	if (code == 0)
		return "X won";
	else if (code == 1)
		return "O won";
	else if (code == 2)
		return "Draw";
	else
		return "Game has not completed";
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	//string fileIn("practice");
	//string fileIn("small");
	string fileIn("large");

	if (!openFileHandles(readFile, fileIn + ".txt", writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	const int rows = 4, cols = 4;
	for (int t = 0; t < T; ++t)
	{
		char arr[rows][cols];
		// TODO: start here
		for (int r = 0; r < rows; ++r)
			for (int c = 0; c < cols; ++c)
				readFile >> arr[r][c];

		int code = -1;
		bool haveBlanks = false;

		// check horizontals
		for (int r = 0; r < rows; ++r)
		{
			if (code != -1)
				break;

			// 0:'X', 1:'O', 2:'T', 3:'.'
			int mask[4] = {0};

			// find characters
			for (int c = 0; c < cols; ++c)
				findChar(arr[r][c], mask);
			
			// any blanks?
			if (mask[3] > 0)
			{
				haveBlanks = true;
				continue;
			}

			code = getCode(mask);
		}

		// check verticals
		if (code == -1)
		{
			for (int c = 0; c < cols; ++c)
			{
				if (code != -1)
					break;

				// 0:'X', 1:'O', 2:'T', 3:'.'
				int mask[4] = {0};
				for (int r = 0; r < rows; ++r)
					findChar(arr[r][c], mask);

				code = getCode(mask);
			}
		}

		// check diagonals

		// left to right
		if (code == -1)
		{
			// 0:'X', 1:'O', 2:'T', 3:'.'
			int mask[4] = {0};
			for (int i = 0; i < 4; ++i)
				findChar(arr[i][i], mask);
			
			code = getCode(mask);
		}

		// right to left
		if (code == -1)
		{
			// 0:'X', 1:'O', 2:'T', 3:'.'
			int mask[4] = {0};
			for (int i = 0; i < 4; ++i)
				findChar(arr[i][3-i], mask);

			code = getCode(mask);
		}

		// determine the code
		if (code == -1 && !haveBlanks)  // draw
			code = 2;

		//  "Case #x: y"
		//cout << "Case #" << t+1 << ": " << getStatus(code) << endl;
		writeFile << "Case #" << t+1 << ": " << getStatus(code) << endl;
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile)
{
	// input file
	readFile.open(inFile.c_str());
	if (!readFile)
	{
		cout << "Could not find '" << inFile << "'\n\n";
		return false;
	}

	// output file
	writeFile.open(outFile.c_str());
	if (!writeFile)
	{
		cout << "Could not find '" << outFile << "'\n\n";
		return false;
	}

	return true;
}
