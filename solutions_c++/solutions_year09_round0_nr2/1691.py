#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

const char alpha[] = {'a','b','c','d','e','f','g',
                      'h','i','j','k','l','m','n',
					  'o','p','q','r','s','t','u',
					  'v','w','x','y','z'};


void computeResult(int **altitude, char **result, int ** flowChart, int numRows, int numColumns, int startRow, int startColumn, int sequence)
{
	if (altitude[startRow][startColumn] < 0) 
		return;
	result[startRow][startColumn] = alpha[sequence];
	altitude[startRow][startColumn] = -1;

	int flow = flowChart[startRow][startColumn];
	
	if (flow != 4) {
		int deltaX, deltaY;
		if (flow == 0) {
			deltaX = -1;
			deltaY = 0;
		}
		if (flow == 1) {
			deltaX = 0;
			deltaY = -1;
		}
		if (flow == 2) {
			deltaX = 0;
			deltaY = 1;
		}
		if (flow == 3) {
			deltaX = 1;
			deltaY = 0;
		}
		computeResult(altitude, result, flowChart, numRows, numColumns, startRow + deltaX, startColumn + deltaY, sequence);
	}


	if (startRow - 1 >= 0) {
		if (flowChart[startRow - 1][startColumn] == 3)
			computeResult(altitude, result, flowChart, numRows, numColumns, startRow - 1, startColumn, sequence);
	}

	if (startColumn - 1 >= 0) {
		if (flowChart[startRow][startColumn - 1] == 2)
			computeResult(altitude, result, flowChart, numRows, numColumns, startRow, startColumn - 1, sequence);
	}

	if (startColumn + 1 < numColumns) {
		if (flowChart[startRow][startColumn + 1] == 1)
			computeResult(altitude, result, flowChart, numRows, numColumns, startRow, startColumn + 1, sequence);
	}

	if (startRow + 1 < numRows) {
		if (flowChart[startRow+1][startColumn] == 0)
			computeResult(altitude, result, flowChart, numRows, numColumns, startRow + 1, startColumn, sequence);
	}
	return;
}


int main()
{
	ifstream in;
	in.open("B-large.in");
    ofstream out;
	out.open("result.txt");
    
	string temp;
	getline(in, temp);

	int cases = atoi(temp.c_str());

	for (int count = 0; count < cases; count++) {
		getline(in, temp);
		int split = temp.find(" ",0);
		const int numRows = atoi(temp.substr(0, split).c_str());
		const int numColumns = atoi(temp.substr(split + 1).c_str());

		int **altitude = new int *[numRows];
		for (int i = 0; i < numRows; i++)
			altitude[i] = new int[numColumns];

		int **flowChart = new int *[numRows];
		for (int i = 0; i < numRows; i++)
			flowChart[i] = new int[numColumns];

		

		char **result = new char *[numRows];
		for (int i = 0; i < numRows; i++)
			result[i] = new char[numColumns];

		for (int i = 0; i < numRows; i++)
			for (int j = 0; j < numColumns; j++) {
				result[i][j] = '0';
			}

		for (int i = 0; i < numRows; i++) {
			getline(in, temp);
			int start = 0;
			for (int j = 0; j < numColumns; j++) {
				if (j == numColumns - 1)
					altitude[i][j] = atoi(temp.substr(start).c_str());
				else {
					int end = temp.find(" ",start);
					altitude[i][j] = atoi(temp.substr(start, end - start).c_str());
					start = end + 1;
				}
			}
		}

		//0:North, 1:West, 2:East, 3:South, 4:sink

		for (int i = 0; i < numRows; i++)
			for (int j = 0; j < numColumns; j++) {
			    int min = 999999;
				if (i - 1 >= 0) {
					if (altitude[i-1][j] < altitude[i][j] && altitude[i-1][j] < min) {
						min = altitude[i-1][j];
						flowChart[i][j] = 0;
					}
				}
				if (j - 1 >= 0) {
					if (altitude[i][j-1] < altitude[i][j] && altitude[i][j-1] < min) {
						min = altitude[i][j-1];
						flowChart[i][j] = 1;
					}
				}
				if (j + 1 < numColumns) {
					if (altitude[i][j+1] < altitude[i][j] && altitude[i][j+1] < min) {	
						min = altitude[i][j+1];
						flowChart[i][j] = 2;
					}
				}
				if (i + 1 < numRows) {
					if (altitude[i+1][j] < altitude[i][j] && altitude[i+1][j] < min) {
						min = altitude[i+1][j];
						flowChart[i][j] = 3;
					}
				}
				if (min == 999999)
					flowChart[i][j] = 4;
			}

		int sequence = -1;


		for (int i = 0; i < numRows; i++)
			for (int j = 0; j < numColumns; j++) {
				if (altitude[i][j] >= 0) 
					sequence++;
				computeResult(altitude, result, flowChart, numRows, numColumns, i, j, sequence);
			}

		out << "Case #" << count + 1 << ":" << endl;
		for (int i = 0; i < numRows; i++) {
			for (int j = 0; j < numColumns; j++) {
				if (j != numColumns - 1)
				    out << result[i][j] << " ";
				else
					out << result[i][j];
			}
			out << endl;
		}

		for (int i = 0; i < numRows; i++) {
			delete [] altitude[i];
			delete [] result[i];
			delete [] flowChart[i];
		}

		delete [] altitude;
		delete [] result;
		delete [] flowChart;
	}

	in.close();
	out.close();

	return 0;
}




