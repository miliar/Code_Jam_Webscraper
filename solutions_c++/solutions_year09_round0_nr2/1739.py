#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int findBasinNumber( unsigned int row,
				    unsigned int col,
					unsigned int H,
					unsigned int W,
					vector < vector < int > >& m,
					vector < vector < int > >& labels) {

	int minValue = 100000;
	if (row > 0) minValue = min(minValue, m[row-1][col]);
	if (col > 0) minValue = min(minValue, m[row][col-1]);
	if (col < W - 1) minValue = min(minValue, m[row][col+1]);
	if (row < H - 1) minValue = min(minValue, m[row+1][col]);
		
	if (minValue >= m[row][col]) return labels[row][col];

	if (row > 0 && m[row-1][col] == minValue) 
	{
		return findBasinNumber(row-1, col, H, W, m, labels);		
	}
	else if (col > 0 && m[row][col-1] == minValue) 
	{
		return findBasinNumber(row, col-1, H, W, m, labels);
	}
	else if (col < W - 1 && m[row][col+1] == minValue)
	{
		return findBasinNumber(row, col+1, H, W, m, labels);
	}
	else if (row < H - 1 && m[row+1][col] == minValue)
	{
		return findBasinNumber(row+1, col, H, W, m, labels);
	}
	return -1;
}

/*
bool updateIfInSomeBasin( unsigned int row,
						  unsigned int col,
						  unsigned int H,
						  unsigned int W,
						  vector < vector < int > >& m,
						  vector < vector < int > >& labels) {
	int minValue = 100000;
	if (row > 0) minValue = min(minValue, m[row-1][col]);
	if (col > 0) minValue = min(minValue, m[row][col-1]);
	if (col < W - 1) minValue = min(minValue, m[row][col+1]);
	if (row < H - 1) minValue = min(minValue, m[row+1][col]);
		
	if (minValue >= m[row][col]) return false;

	if (row > 0 && m[row-1][col] == minValue && labels[row-1][col] != -1) 
	{
		labels[row][col] = labels[row-1][col];
		return true;
	}
	else if (col > 0 && m[row][col-1] == minValue && labels[row][col-1] != -1) 
	{
		labels[row][col] = labels[row][col-1];
		return true;
	}
	else if (col < W - 1 && m[row][col+1] == minValue && labels[row][col+1] != -1)
	{
		labels[row][col] = labels[row][col+1];
		return true;
	}
	else if (row < H - 1 && m[row+1][col] == minValue && labels[row+1][col] != -1)
	{
		labels[row][col] = labels[row+1][col];
		return true;
	}
	return false;
}
*/

void updateLabels(unsigned int label,
				  unsigned int row,
				  unsigned int col,
				  unsigned int H,
				  unsigned int W,
				  vector < vector < int > >& m,
				  vector < vector < int > >& labels) {
	//if (labels[row][col] != -1) return;
    labels[row][col] = label;

	bool isSink = true;
	if (row > 0 && m[row-1][col] < m[row][col]) isSink = false;
	if (col > 0 && m[row][col-1] < m[row][col]) isSink = false;
	if (col < W - 1 && m[row][col+1] < m[row][col]) isSink = false;
	if (row < H - 1 && m[row+1][col] < m[row][col]) isSink = false;
	if (isSink) {		
		return;
	}
	int minValue = 100000;
	if (row > 0) minValue = min(minValue, m[row-1][col]);
	if (col > 0) minValue = min(minValue, m[row][col-1]);
	if (col < W - 1) minValue = min(minValue, m[row][col+1]);
	if (row < H - 1) minValue = min(minValue, m[row+1][col]);
		
	if (row > 0 && m[row-1][col] == minValue) updateLabels(label, row-1, col, H, W, m, labels);
	else if (col > 0 && m[row][col-1] == minValue) updateLabels(label, row, col-1, H, W, m, labels);
	else if (col < W - 1 && m[row][col+1] == minValue) updateLabels(label, row, col+1, H, W, m, labels);
	else if (row < H - 1 && m[row+1][col] == minValue) updateLabels(label, row+1, col, H, W, m, labels);
}

void task2(const char* in_filename, const char* out_filename)
{
	ifstream in(in_filename);
	ofstream out(out_filename);
	if (in.is_open())
	{
		unsigned int T, H, W;
		in >> T;
		// T - maps count		
		for (unsigned int caseNumber = 1; caseNumber <= T; ++caseNumber) {
			in >> H >> W; // heigth, width
			vector < vector < int > > m(H, vector<int>(W)), labels(H, vector<int>(W, -1));
			for (unsigned int i = 0; i < H; ++i) {
				for (unsigned int j = 0; j < W; ++j) {
					in >> m[i][j];
				}
			}

			unsigned int nextLabel = 0;
			for (unsigned int i = 0; i < H; ++i) {
				for (unsigned int j = 0; j < W; ++j) {
					if (labels[i][j] == -1) {
						int basinNumber = findBasinNumber(i, j, H, W, m, labels);						
						if (basinNumber == -1) {
							updateLabels(nextLabel, i, j, H, W, m, labels);
							++nextLabel;
						}
						else
						{
							labels[i][j] = basinNumber;
						}
					}
				}
			}
			
			out << "Case #" << caseNumber << ": " << endl;
			for (unsigned int i = 0; i < H; ++i) {
				for (unsigned int j = 0; j < W; ++j) {
					out << static_cast<char>('a' + labels[i][j]) << " ";
				}
				out << endl;
			}			
		}
	}
	else
	{
		throw "File not found";
	}
	in.close();
	out.close();
}


int _tmain(int argc, _TCHAR* argv[])
{
	task2("D:\\B-small-attempt1.in", "D:\\B-small-attempt1.out");
	//task2("D:\\bbb.in", "D:\\bbb.out");
	return 0;
}

