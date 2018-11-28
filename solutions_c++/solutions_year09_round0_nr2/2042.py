#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

ifstream infile;
ofstream outfile;

int matrix[100][100];
char outMatrix[100][100];
char currentLetter;

int getTestCaseNumber() {
	int retval;
	string firstLine;
	getline(infile, firstLine);
	
	istringstream iss(firstLine);
	iss >> retval;
	return retval;
}

void getHeightWidth(int* height, int* width) {
	string dimensionLine;
	getline(infile, dimensionLine);
	
	istringstream iss(dimensionLine);
	iss >> *height;
	iss >> *width;
}

void fillMatrix(int height, int width)
{
	for (int i=0; i<height; i++) 
	{
		string currentLine;
		getline(infile, currentLine);
		istringstream iss(currentLine);
	
		for (int j=0; j< width; j++)
		{
			iss >> matrix[i][j];
			outMatrix[i][j] = ' ';
		}
	}
}

void replace(int height, int width, char orig, char newChar)
{
	for (int i=0; i<height; i++)
	{
		for (int j=0; j<width; j++)
		{
			if (outMatrix[i][j] == orig)
				outMatrix[i][j] = newChar;
		}
	}
}

void fillOutflow(int y, int x, int height, int width)
{
	if (outMatrix[y][x] != ' ')
		return;
	
	int up = 65535;
	int down = 65535;
	int left= 65535;
	int right = 65535;
	int center = matrix[y][x];
	outMatrix[y][x] = currentLetter;
	
	if ((y-1) >= 0)
		up = matrix[y-1][x];
	if ((x-1) >= 0)
		left = matrix[y][x-1];
	if ((x+1) <= (width -1))
		right = matrix[y][x+1];
	if ((y+1) <= (height - 1))
		down = matrix[y+1][x];
	
	int flowY = y-1;
	int flowX = x;
	int min = up;
	if (left < min) {
		min = left;
		flowY = y;
		flowX = x-1;
	}
	if (right < min) {
		min = right;
		flowY = y;
		flowX = x+1;
	}
	if (down < min) {
		min = down;
		flowY = y+1;
		flowX = x;
	}
	if (center <= min) {
		currentLetter ++;
	}
	else
	{
		if (outMatrix[flowY][flowX] == ' ') {
			fillOutflow(flowY, flowX, height, width);
		}
		else { // need to update all currentLetter with the outflowed letter
			replace(height, width, currentLetter, outMatrix[flowY][flowX]);

		}
	}
	
}

void fillOutMatrix(int height, int width)
{
	currentLetter = 'a';
	for (int i=0; i<height; i++)
	{
		for (int j=0; j<width; j++)
		{
			fillOutflow(i,j,height, width);
		}
	}
}

void printOutMatrix(int height, int width)
{
	for (int i=0; i<height; i++)
	{
		for (int j=0; j<width; j++)
		{
			outfile << outMatrix[i][j] <<"  ";
		}
		outfile << endl;
	}
}


int main (int argc, char * const argv[]) {
	infile.open("B-large.in");
	outfile.open("B-large.out");
	
	int testcaseNumber = getTestCaseNumber();
	for (int i=0; i< testcaseNumber; i++)
	{
		int height = 0;
		int width = 0;
		getHeightWidth(&height, &width);
		
		fillMatrix(height, width);
		fillOutMatrix(height, width);
		
		outfile << "Case #" << i+1 << ": "<<endl;
		printOutMatrix(height, width);
	}
		
	infile.close();	
	outfile.close();
	
    return 0;
}
