#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <conio.h>
using namespace std;



int R;
int C;
char** Tiles;

bool IsPossible;



void ReplaceTiles();



int main()
{
	ifstream inputFileReader("input.txt");
	ofstream outputFileWriter("output.txt");

	if (!inputFileReader || !outputFileWriter)
	{
		return 1;
	}

	string inputLine;
	stringstream inputLineReader;

	getline(inputFileReader, inputLine);
	inputLineReader << inputLine;

	int T;
	inputLineReader >> T;

	for (int testCaseIndex = 0; testCaseIndex < T; testCaseIndex++)
	{
		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		inputLineReader >> R >> C;

		Tiles = new char* [R];

		for (int rowIndex = 0; rowIndex < R; rowIndex++)
		{
			Tiles[rowIndex] = new char [C];

			inputLineReader.clear();
			getline(inputFileReader, inputLine);
			inputLineReader << inputLine;

			for (int columnIndex = 0; columnIndex < C; columnIndex++)
			{
				inputLineReader >> Tiles[rowIndex][columnIndex];
			}
		}

		ReplaceTiles();

		outputFileWriter << "Case #" << (testCaseIndex + 1) << ":" << endl;

		if (IsPossible)
		{
			for (int rowIndex = 0; rowIndex < R; rowIndex++)
			{
				for (int columnIndex = 0; columnIndex < C; columnIndex++)
				{
					outputFileWriter << Tiles[rowIndex][columnIndex];
				}

				outputFileWriter << endl;
			}
		}
		else
		{
			outputFileWriter << "Impossible" << endl;
		}

		for (int rowIndex = 0; rowIndex < R; rowIndex++)
		{
			delete [] Tiles[rowIndex];
		}

		delete [] Tiles;
	}

	inputFileReader.close();
	outputFileWriter.close();

	return 0;
}



void ReplaceTiles()
{
	IsPossible = true;

	for (int rowIndex = 0; rowIndex < R - 1; rowIndex++)
	{
		int columnIndex = 0;

		while (columnIndex < C - 1)
		{
			if (Tiles[rowIndex][columnIndex] == '#' && Tiles[rowIndex][columnIndex + 1] == '#' &&
				Tiles[rowIndex + 1][columnIndex] == '#' && Tiles[rowIndex + 1][columnIndex + 1] == '#')
			{
				Tiles[rowIndex][columnIndex] = '/';
				Tiles[rowIndex][columnIndex + 1] = '\\';
				Tiles[rowIndex + 1][columnIndex] = '\\';
				Tiles[rowIndex + 1][columnIndex + 1] = '/';

				columnIndex += 2;
			}
			else
			{
				columnIndex++;
			}
		}
	}

	for (int rowIndex = 0; rowIndex < R; rowIndex++)
	{
		for (int columnIndex = 0; columnIndex < C; columnIndex++)
		{
			if (Tiles[rowIndex][columnIndex] == '#')
			{
				IsPossible = false;
				break;
			}
		}
	}
}